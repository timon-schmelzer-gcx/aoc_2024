from collections import defaultdict
from itertools import pairwise
from pathlib import Path


def read(p: Path = Path("input.txt")) -> tuple[defaultdict[int, list], list[list[int]]]:
    rules: defaultdict[int, list] = defaultdict(list)
    instructions: list[list[int]] = []

    rule_mode = True

    for row in p.read_text().split("\n")[:-1]:
        if not row:
            rule_mode = False
        else:
            if rule_mode:
                before, after = row.split("|")
                rules[int(before)].append(int(after))
            else:
                instructions.append([int(val) for val in row.split(",")])

    return rules, instructions


def is_valid_instruction(instructs: list[int], rules: defaultdict[int, list]) -> bool:
    return all(b in rules[a] for a, b in pairwise(instructs))


def part_one(rules: defaultdict[int, list], instructions: list[list[int]]) -> int:
    res = []

    for instructs in instructions:
        if is_valid_instruction(instructs, rules):
            res.append(instructs[len(instructs) // 2])

    return sum(res)


def part_two(rules: defaultdict[int, list], instructions: list[list[int]]) -> int:
    res = []

    for instructs in instructions:
        is_valid = is_valid_instruction(instructs, rules)

        if is_valid:
            continue

        while not is_valid:
            for a, b in pairwise(instructs):
                if b not in rules[a]:
                    idx_a = instructs.index(a)
                    instructs = [i if i != b else a for i in instructs]
                    instructs[idx_a] = b

                    is_valid = is_valid_instruction(instructs, rules)

                    break

        res.append(instructs[len(instructs) // 2])

    return sum(res)


if __name__ == "__main__":
    rules, instructions = read()

    print(part_one(rules, instructions))
    print(part_two(rules, instructions))
