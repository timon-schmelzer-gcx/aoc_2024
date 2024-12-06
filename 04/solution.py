from pathlib import Path

TARGET_WORD = "XMAS"

DIRS = [
    # E
    (1, 0),
    # SE
    (1, 1),
    # S
    (0, 1),
    # SW
    (-1, 1),
    # W
    (-1, 0),
    # NW
    (-1, -1),
    # N
    (0, -1),
    # NE
    (1, -1),
]


def read(p: Path = Path("input.txt")):
    arr = []

    for row in p.read_text().split("\n"):
        if row:
            arr.append(row)

    return arr


def part_one(mat: list[str], height: int, width: int) -> int:
    s: int = 0

    for cur_h in range(height):
        for cur_w in range(height):
            for d in DIRS:
                w: list[str] = []
                valid = True

                for i in range(0, len(TARGET_WORD)):
                    check_h = cur_h + d[0] * i
                    check_w = cur_w + d[1] * i

                    if (
                        check_h < 0
                        or check_h >= height
                        or check_w < 0
                        or check_w >= width
                    ):
                        valid = False
                        continue
                    else:
                        c = mat[check_h][check_w]
                        w.append(c)

                if valid:
                    sol = "".join(w)
                    if sol == TARGET_WORD:
                        s += 1
    return s


def part_two(mat: list[str], height: int, width: int) -> int:
    s: int = 0

    for cur_h in range(height):
        for cur_w in range(height):
            if mat[cur_h][cur_w] != "A":
                continue
            elif (
                cur_h - 1 < 0
                or cur_h + 1 >= height
                or cur_w - 1 < 0
                or cur_w + 1 >= width
            ):
                continue
            elif (
                (
                    mat[cur_h - 1][cur_w - 1] == "M"
                    and mat[cur_h + 1][cur_w + 1] == "S"
                    and mat[cur_h - 1][cur_w + 1] == "M"
                    and mat[cur_h + 1][cur_w - 1] == "S"
                )
                or (
                    mat[cur_h - 1][cur_w - 1] == "S"
                    and mat[cur_h + 1][cur_w + 1] == "M"
                    and mat[cur_h - 1][cur_w + 1] == "M"
                    and mat[cur_h + 1][cur_w - 1] == "S"
                )
                or (
                    mat[cur_h - 1][cur_w - 1] == "S"
                    and mat[cur_h + 1][cur_w + 1] == "M"
                    and mat[cur_h - 1][cur_w + 1] == "S"
                    and mat[cur_h + 1][cur_w - 1] == "M"
                )
                or (
                    mat[cur_h - 1][cur_w - 1] == "M"
                    and mat[cur_h + 1][cur_w + 1] == "S"
                    and mat[cur_h - 1][cur_w + 1] == "S"
                    and mat[cur_h + 1][cur_w - 1] == "M"
                )
            ):
                s += 1

    return s


if __name__ == "__main__":
    mat = read()

    height = len(mat)
    width = len(mat[0])

    print(part_one(mat, height, width))
    print(part_two(mat, height, width))
