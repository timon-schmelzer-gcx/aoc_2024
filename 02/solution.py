from itertools import pairwise
from pathlib import Path


def read(p: Path = Path("input.txt")):
    reports = []

    for row in p.read_text().split("\n"):
        if row:
            reports.append([int(r) for r in row.split()])

    return reports


def is_save_report(report: list[int]) -> bool:
    if not (report == sorted(report) or report == sorted(report, reverse=True)):
        return False

    for a, b in pairwise(report):
        if not 1 <= abs(a - b) <= 3:
            return False

    return True

def is_save_report_tolerant(report: list[int]) -> bool:
    if is_save_report(report):
        return True

    n_levels = len(report)

    for i in range(n_levels):
        fixed_report = report.copy()

        del fixed_report[i]
        if is_save_report(fixed_report):
            return True

    return False


if __name__ == "__main__":
    reports = read()

    print(sum(is_save_report(r) for r in reports))
    print(sum(is_save_report_tolerant(r) for r in reports))
