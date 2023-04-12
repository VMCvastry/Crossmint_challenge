from materializer import Materializer
from megaverse import Megaverse


if __name__ == "__main__":
    """
    Parkour to the moon!

    We are assuming the input grid is valid, eg there are no moons isolated.

    Code was tested until commit "Working Challenge" after that the api was disabled,
    however the subsequent commits were only refactoring the code.
    """
    materializer = Materializer()
    megaverse = Megaverse.from_strings(materializer.get_grid())
    megaverse.materialize_megaverse(materializer)
