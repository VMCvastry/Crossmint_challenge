from enum import Enum

from .celestial_object import CelestialObject


class SoloonColor(Enum):
    BLUE = 1
    RED = 2
    PURPLE = 3
    WHITE = 4


def get_color(color) -> SoloonColor:
    if color == "BLUE":
        return SoloonColor.BLUE
    elif color == "RED":
        return SoloonColor.RED
    elif color == "PURPLE":
        return SoloonColor.PURPLE
    elif color == "WHITE":
        return SoloonColor.WHITE
    else:
        raise ValueError(f"Invalid color name: {color}")


class Soloon(CelestialObject):
    def __init__(self, r, c, color):
        super().__init__(r, c)
        self.color: SoloonColor = get_color(color)

    def get_create_params(self):
        return {**self._get_basic_params(), "color": self.color.name}
