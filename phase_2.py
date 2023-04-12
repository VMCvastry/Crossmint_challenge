from materializer import Materializer
from megaverse import Megaverse


if __name__ == "__main__":  # Parkour to the moon!
    # We are assuming the input grid is valid, eg there are no moons isolated.
    m = Materializer()
    grid = m.get_grid()
    for row in grid:
        print(row)
    megaverse = Megaverse.from_strings(m.get_grid())
    megaverse.materialize_megaverse(m)
