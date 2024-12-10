from pathlib import Path

DIRS = [
    # E
    (1, 0),
    # S
    (0, 1),
    # W
    (-1, 0),
    # N
    (0, -1),
]


def read(
    p: Path = Path("input.txt"),
) -> dict[tuple[int, int], int]:
    heights: dict[tuple[int, int], int] = {}

    for y, row in enumerate(p.read_text().split("\n")):
        if row:
            for x, c in enumerate(row):
                heights[x, y] = int(c)

    return heights


if __name__ == "__main__":
    heights = read()

    unique_start_ends: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    unique_paths: list[list[tuple[int, int]]] = []

    for start_pos, h in heights.items():
        if h == 0:
            paths_to_check: list[list[tuple[int, int]]] = [[start_pos]]

            h_iter = 0

            while True:
                updated_paths = []
                h_iter += 1

                if h_iter > 9:
                    break

                for ptc in paths_to_check:
                    cur_pos = ptc[-1]

                    for dir in DIRS:
                        next_pos = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])
                        if next_pos in heights and heights[next_pos] == h_iter:
                            updated_paths.append(ptc + [next_pos])

                paths_to_check = updated_paths

            for p in paths_to_check:
                unique_start_ends.add((p[0], p[-1]))
                unique_paths.append(p)

    print(len(unique_start_ends))
    print(len(unique_paths))
