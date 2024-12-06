from collections import Counter
from pathlib import Path


def read(p: Path = Path("input.txt")) -> tuple[list, list]:
    firsts, seconds = [], []

    for row in p.read_text().split("\n"):
        if row:
            one, two = row.split()
            firsts.append(int(one))
            seconds.append(int(two))

    return sorted(firsts), sorted(seconds)


if __name__ == "__main__":
    r = read()
    print(sum(abs(a - b) for a, b in zip(*r)))

    firsts, seconds = r
    seconds_counts = Counter(seconds)
    print(sum(a * seconds_counts.get(a, 0) for a in firsts))
