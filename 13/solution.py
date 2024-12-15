from dataclasses import dataclass
from decimal import Decimal
from itertools import batched
from pathlib import Path


@dataclass
class SlotMachine:
    a_x: Decimal
    a_y: Decimal
    b_x: Decimal
    b_y: Decimal
    p_x: Decimal
    p_y: Decimal

    a_tokens: int = 3
    b_tokens: int = 1

    max_button_presses: int = 100

    # does not work for part two
    def solve_brute_force(self) -> int:
        best: int | None = None
        for n_a in range(self.max_button_presses + 1):
            for n_b in range(self.max_button_presses + 1):
                x_tot = n_a * self.a_x + n_b * self.b_x
                y_tot = n_a * self.a_y + n_b * self.b_y

                if x_tot == self.p_x and y_tot == self.p_y:
                    tokens = n_a * self.a_tokens + n_b * self.b_tokens

                    if best is None:
                        best = tokens
                    else:
                        best = min(tokens, best)

        return 0 if best is None else best

    def solve_smart(self, part_two: bool = False) -> int:
        if part_two:
            huge_number = 10000000000000
            self.p_x += huge_number
            self.p_y += huge_number

        n_b = (self.p_y - self.a_y * (self.p_x / self.a_x)) / (
            self.b_y - (self.b_x / self.a_x) * self.a_y
        )

        n_a = (self.p_x - self.b_x * n_b) / self.a_x

        # allow for small deviations from int
        if (
            round(n_a, 6) == round(n_a, 0)
            and round(n_b, 6) == round(n_b, 0)
            and n_a > 0
            and n_b > 0
        ):
            tokens = (
                int(round(n_a, 0)) * self.a_tokens + int(round(n_b, 0)) * self.b_tokens
            )
            return tokens

        return 0


def read(p: Path = Path("input.txt")) -> list[SlotMachine]:
    slot_machines: list[SlotMachine] = []

    for eq_one, eq_two, prize, _ in batched(p.read_text().split("\n"), 4):
        a_x = Decimal(eq_one.split("X+")[1].split(",")[0])
        a_y = Decimal(eq_one.split("Y+")[1])

        b_x = Decimal(eq_two.split("X+")[1].split(",")[0])
        b_y = Decimal(eq_two.split("Y+")[1])

        p_x = Decimal(prize.split("X=")[1].split(",")[0])
        p_y = Decimal(prize.split("Y=")[1])

        slot_machines.append(SlotMachine(a_x, a_y, b_x, b_y, p_x, p_y))

    return slot_machines


if __name__ == "__main__":
    slot_machines = read()

    print(sum(sm.solve_smart() for sm in slot_machines))
    print(sum(sm.solve_smart(part_two=True) for sm in slot_machines))
