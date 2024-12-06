import sys
from sys import argv
from pathlib import Path

def validate_and_format_day_arg():
    if len(argv) != 2:
        print("Need to have one additional argument (day number)")
        sys.exit()

    day_ = argv[1]

    try:
        day = int(day_)
    except ValueError:
        print(f"Seconds argument {day_} could not be converted to integer")
        sys.exit()

    if day < 1 or day > 25:
        print(f"Day argument must be between 1 and 25, is {day}")
        sys.exit()

    day_padded = f"{day:02}"
    return day_padded

if __name__ == "__main__":
    day_path = Path(validate_and_format_day_arg())

    # create folder and files
    day_path.mkdir(exist_ok=False)
    (day_path / "input.txt").touch()
    (day_path / "solution.py").write_text(r"""from pathlib import Path

def read(p: Path = Path("input.txt")):
    arr = []

    for row in p.read_text().split("\n"):
        if row:
            arr.append(row.split())

    return arr

if __name__ == "__main__":
    ...
""")
