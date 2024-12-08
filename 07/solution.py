from dataclasses import dataclass
from functools import reduce
from itertools import product
from operator import add, mul
from pathlib import Path
from typing import Callable, Iterator


@dataclass
class Memory:
    ops_iter: Iterator

    def __call__(self, a: int, b: int) -> int:
        return next(self.ops_iter)(a, b)


OPS = [mul, add]


def op_concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def read(p: Path = Path("input.txt")) -> list[tuple[int, list[int]]]:
    equations: list[tuple[int, list[int]]] = []

    for row in p.read_text().split("\n"):
        if row:
            res, nums = row.split(": ")
            res_int = int(res)
            nums_int = [int(val) for val in nums.split()]

            equations.append((res_int, nums_int))

    return equations


def solve(equations: list[tuple[int, list[int]]], all_ops: list[Callable]) -> int:
    s = 0

    for res, nums in equations:
        for ops in product(all_ops, repeat=len(nums) - 1):
            cal = reduce(Memory(ops_iter=iter(ops)), nums)

            if cal == res:
                s += cal
                break
    return s


if __name__ == "__main__":
    equations = read()

    print(solve(equations, all_ops=OPS))
    print(solve(equations, all_ops=OPS + [op_concat]))
