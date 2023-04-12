from materializer import Materializer
from megaverse import Megaverse


if __name__ == "__main__":  # Parkour to the moon!
    # We are assuming the input grid is valid, eg there are no moons isolated.
    materializer = Materializer()
    megaverse = Megaverse.from_strings(materializer.get_grid())
    megaverse.materialize_megaverse(materializer)
