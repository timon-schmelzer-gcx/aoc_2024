from collections import defaultdict
from pathlib import Path


def read(p: Path = Path("input.txt")) -> defaultdict[str, int]:
    stones: defaultdict[str, int] = defaultdict(int)

    for s in p.read_text().split("\n")[0].split():
        stones[s] += 1

    return stones


def blink(stones: defaultdict[str, int], iterations: int) -> int:
    for _ in range(iterations):
        new_stones: defaultdict[str, int] = defaultdict(int)

        for s, n in stones.items():
            if s == "0":
                new_stones["1"] += n
            elif len(s) % 2 == 0:
                center = len(s) // 2
                first, last = s[:center], s[center:]

                while last.startswith("0") and len(last) > 1:
                    last = last.removeprefix("0")

                new_stones[first] += n
                new_stones[last] += n
            else:
                new_stones[str(int(s) * 2024)] += n

        stones = new_stones

    return sum(stones.values())


if __name__ == "__main__":
    stones = read()

    print(blink(stones, iterations=25))
    print(blink(stones, iterations=75))
