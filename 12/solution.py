from collections import defaultdict
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


def add_fences(n_neighbors: int) -> int:
    if n_neighbors == 1:
        return 3
    elif n_neighbors == 2:
        return 2
    elif n_neighbors == 3:
        return 1
    elif n_neighbors == 4:
        return 0
    elif n_neighbors == 0:
        return 4
    else:
        raise ValueError("Neighbors must be between 0 and 4, is", n_neighbors)


def read(p: Path = Path("input.txt")) -> dict[tuple[int, int], str]:
    garden: dict[tuple[int, int], str] = {}

    for y, row in enumerate(p.read_text().split("\n")):
        if row:
            for x, c in enumerate(row):
                location = (x, y)
                garden[location] = c

    return garden


def assign_clusters(
    garden: dict[tuple[int, int], str],
) -> defaultdict[tuple[str, int], set[tuple[int, int]]]:
    assignments: dict[tuple[int, int], tuple[str, int]] = {}

    for location, plant_id in garden.items():
        # skip already assigned
        if location not in assignments:
            # find cluster
            plant_cluster: set[tuple[int, int]] = set([location])

            while True:
                next_plant_cluster = plant_cluster.copy()
                for loc in plant_cluster:
                    for dir in DIRS:
                        next_loc = (loc[0] + dir[0], loc[1] + dir[1])

                        if next_loc in garden and garden[next_loc] == plant_id:
                            next_plant_cluster.add(next_loc)

                if next_plant_cluster == plant_cluster:
                    # no new cluster members have been found
                    break

                else:
                    plant_cluster = next_plant_cluster

            if not assignments or not any(
                c[0] == plant_id for c in assignments.values()
            ):
                # first cluster, start with 0
                comb_id = (plant_id, 0)
            else:
                # if available, increase by 1
                max_id = max([c[1] for c in assignments.values() if c[0] == plant_id])
                comb_id = (plant_id, max_id + 1)

            # add assignments
            for loc in plant_cluster:
                assignments[loc] = comb_id

    garden_clusters: defaultdict[tuple[str, int], set[tuple[int, int]]] = defaultdict(
        set
    )

    for loc, group in assignments.items():
        garden_clusters[group].add(loc)

    return garden_clusters


def score(garden_clusters: defaultdict[tuple[str, int], set[tuple[int, int]]]) -> int:
    s = 0

    for cluster, locations in garden_clusters.items():
        multiplier = len(locations)
        fences = 0

        for loc in locations:
            neighbors = 0
            for dir in DIRS:
                new_loc = (loc[0] + dir[0], loc[1] + dir[1])
                if new_loc in locations:
                    neighbors += 1

            fences += add_fences(neighbors)

        s += multiplier * fences

    return s


if __name__ == "__main__":
    garden = read()

    garden_clusters = assign_clusters(garden)
    print(score(garden_clusters))
