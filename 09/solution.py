from pathlib import Path


def read(p: Path = Path("input.txt")) -> list[int | None]:
    slots: list[int | None] = []

    pos_idx = 0
    file_id = 0

    is_file = True

    for row in p.read_text().split("\n"):
        if row:
            for c in row:
                steps = int(c)
                if is_file:
                    for _ in range(steps):
                        slots.append(file_id)
                    file_id += 1
                else:
                    for _ in range(steps):
                        slots.append(None)

                pos_idx += steps

                is_file = not is_file

    return slots


def display(slots: list[int | None]) -> None:
    print("".join(str(s) if s is not None else "." for s in slots))


def get_res(slots: list[int | None]) -> int:
    s = 0
    for i, num in enumerate(slots):
        if num is not None:
            s += i * num

    return s


def part_one(slots: list[int | None]) -> int:
    while True:
        first_empty_idx = slots.index(None)

        if all(a is None for a in slots[first_empty_idx:]):
            break

        last_file_id = [val for val in reversed(slots) if val][0]
        last_file_idx = len(slots) - list(reversed(slots)).index(last_file_id) - 1

        slots[first_empty_idx] = last_file_id
        slots[last_file_idx] = None

    return get_res(slots)


def part_two(slots: list[int | None]) -> int:
    seen: set[int] = set()

    try:
        while True:
            changed = False

            while not changed:
                last_file_id = [
                    val for val in reversed(slots) if val and val not in seen
                ][0]
                last_file_id_count = slots.count(last_file_id)
                last_file_idx = slots.index(last_file_id)

                cnt = 0
                for i, s in enumerate(slots[:last_file_idx]):
                    if s is None:
                        cnt += 1
                    else:
                        cnt = 0
                        continue

                    # gap is big enough
                    if cnt == last_file_id_count:
                        slots[
                            slots.index(last_file_id) : slots.index(last_file_id)
                            + last_file_id_count
                        ] = [None] * (last_file_id_count)
                        slots[i - last_file_id_count + 1 : i + 1] = [last_file_id] * (
                            last_file_id_count
                        )
                        changed = True
                        break

                seen.add(last_file_id)

    except IndexError:
        return get_res(slots)


if __name__ == "__main__":
    slots = read()

    print(part_one(slots))
    print(part_two(slots))
