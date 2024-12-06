import copy
import re
from pathlib import Path

PATTERN_DO = r"do()"
PATTERN_DONT = r"don't()"
PATTERN_MUL = r"mul\((\d{1,3},\d{1,3})\)"

MAX_MUL_CHARS = len("mul(999,999)")
MUL_START = PATTERN_MUL[:3]


def read(p: Path = Path("input.txt")):
    return p.read_text()[:-1]


def mul(g: str) -> int:
    a, b = g.split(",")
    a_int, b_int = int(a), int(b)

    return a_int * b_int


def mul_instructions(memory: str) -> int:
    s = 0

    p = re.compile(PATTERN_MUL)
    m = p.findall(memory)
    for g in m:
        s += mul(g)

    return s


def many_instructions(memory: str) -> int:
    apply_muls = True

    p = re.compile(PATTERN_MUL)
    s = 0

    for i in range(len(memory)):
        memory_step: str = copy.copy(memory)[i:]

        if memory_step.startswith(PATTERN_DO):
            apply_muls = True
        elif memory_step.startswith(PATTERN_DONT):
            apply_muls = False
        elif memory_step.startswith(MUL_START):
            group = p.findall(memory_step, endpos=MAX_MUL_CHARS)
            if group and apply_muls:
                s += mul(group.pop())

    return s


if __name__ == "__main__":
    memory = read()

    print(mul_instructions(memory))
    print(many_instructions(memory))
