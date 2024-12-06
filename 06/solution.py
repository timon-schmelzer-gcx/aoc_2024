from itertools import cycle
from pathlib import Path

GUARD = {"^": (0, -1), ">": (+1, 0), "v": (0, +1), "<": (-1, 0)}


def read(p: Path = Path("input.txt")) -> tuple[set[tuple[int, int]], tuple[int, int]]:
    obsticles: set[tuple[int, int]] = set()
    guard_pos: tuple[int, int]

    for y, row in enumerate(p.read_text().split("\n")):
        if row:
            for x, c in enumerate(row):
                if c == "#":
                    obsticles.add((x, y))
                elif c in GUARD:
                    guard_pos = (x, y)

    return obsticles, guard_pos


def is_in_range(pos: tuple[int, int], min_x: int, max_x: int, min_y: int, max_y: int):
    return not (pos[0] < min_x or pos[0] > max_x or pos[1] < min_y or pos[1] > max_y)


def part_one(
    obsticles: set[tuple[int, int]],
    guard_pos: tuple[int, int],
    min_x: int,
    max_x: int,
    min_y: int,
    max_y: int,
) -> int:
    visited: set[tuple[int, int]] = set()
    dirs = cycle(GUARD.values())
    cur_dir = next(dirs)

    while is_in_range(guard_pos, min_x, max_x, min_y, max_y):
        visited.add(guard_pos)
        next_pos = guard_pos[0] + cur_dir[0], guard_pos[1] + cur_dir[1]
        if next_pos in obsticles:
            cur_dir = next(dirs)
        else:
            guard_pos = next_pos

    return len(visited)


def part_two(
    obsticles: set[tuple[int, int]],
    initial_guard_pos: tuple[int, int],
    min_x: int,
    max_x: int,
    min_y: int,
    max_y: int,
) -> int:
    n_loops = 0

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            t = (x, y)
            if t not in obsticles and t != initial_guard_pos:
                better_obsticles = obsticles.copy()
                better_obsticles.add(t)

                # tuple of two tuples, containing current position and current direction, example:
                # {((5, 3), (-1, 0)), ((4, 3), (-1, 0))}
                visited: set[tuple[tuple[int, int], tuple[int, int]]] = set()

                dirs = cycle(GUARD.values())
                cur_dir = next(dirs)

                guard_pos = initial_guard_pos

                while is_in_range(guard_pos, min_x, max_x, min_y, max_y):
                    tt = (guard_pos, cur_dir)

                    if tt in visited:
                        n_loops += 1
                        break

                    visited.add(tt)
                    next_pos = guard_pos[0] + cur_dir[0], guard_pos[1] + cur_dir[1]
                    if next_pos in better_obsticles:
                        cur_dir = next(dirs)
                    else:
                        guard_pos = next_pos

    return n_loops


if __name__ == "__main__":
    obsticles, guard_pos = read()

    MIN_X = min(a for a, _ in obsticles)
    MAX_X = max(a for a, _ in obsticles)
    MIN_Y = min(b for _, b in obsticles)
    MAX_Y = max(b for _, b in obsticles)

    print(part_one(obsticles, guard_pos, MIN_X, MAX_X, MIN_Y, MAX_Y))
    print(part_two(obsticles, guard_pos, MIN_X, MAX_X, MIN_Y, MAX_Y))
