from collections import defaultdict
from itertools import combinations
from pathlib import Path


def read(
    p: Path = Path("input.txt"),
) -> tuple[defaultdict[str, set[tuple[int, int]]], tuple[int, int, int, int]]:
    node_positions: defaultdict[str, set[tuple[int, int]]] = defaultdict(set)

    for y, row in enumerate(p.read_text().split("\n")):
        if row:
            for x, c in enumerate(row):
                if c != ".":
                    node_positions[c].add((x, y))

    return (node_positions, (0, x, 0, y - 1))


def is_in_range(pos: tuple[int, int], min_x: int, max_x: int, min_y: int, max_y: int):
    return not (pos[0] < min_x or pos[0] > max_x or pos[1] < min_y or pos[1] > max_y)


def part_one(
    node_positions: defaultdict[str, set[tuple[int, int]]],
    min_x: int,
    max_x: int,
    min_y: int,
    max_y: int,
) -> int:
    antinode_positions: set[tuple[int, int]] = set()

    for positions in node_positions.values():
        combs = combinations(positions, 2)

        for c in combs:
            a, b = c
            v_a_b = (b[0] - a[0], b[1] - a[1])
            v_b_a = (a[0] - b[0], a[1] - b[1])

            a_2 = (a[0] + v_b_a[0], a[1] + v_b_a[1])
            b_2 = (b[0] + v_a_b[0], b[1] + v_a_b[1])

            for t in [a_2, b_2]:
                if is_in_range(t, min_x, max_x, min_y, max_y):
                    antinode_positions.add(t)

    return len(antinode_positions)


def part_two(
    node_positions: defaultdict[str, set[tuple[int, int]]],
    min_x: int,
    max_x: int,
    min_y: int,
    max_y: int,
) -> int:
    antinode_positions: set[tuple[int, int]] = set()

    for positions in node_positions.values():
        for pos in positions:
            antinode_positions.add(pos)

        combs = combinations(positions, 2)

        for c in combs:
            a, b = c
            v_a_b = (b[0] - a[0], b[1] - a[1])
            v_b_a = (a[0] - b[0], a[1] - b[1])

            a_2 = (a[0] + v_b_a[0], a[1] + v_b_a[1])
            b_2 = (b[0] + v_a_b[0], b[1] + v_a_b[1])

            while is_in_range(a_2, min_x, max_x, min_y, max_y):
                antinode_positions.add(a_2)
                a_2 = (a_2[0] + v_b_a[0], a_2[1] + v_b_a[1])

            while is_in_range(b_2, min_x, max_x, min_y, max_y):
                antinode_positions.add(b_2)
                b_2 = (b_2[0] + v_a_b[0], b_2[1] + v_a_b[1])

    return len(antinode_positions)


if __name__ == "__main__":
    node_positions, (MIN_X, MAX_X, MIN_Y, MAX_Y) = read()

    print(part_one(node_positions, MIN_X, MAX_X, MIN_Y, MAX_Y))
    print(part_two(node_positions, MIN_X, MAX_X, MIN_Y, MAX_Y))
