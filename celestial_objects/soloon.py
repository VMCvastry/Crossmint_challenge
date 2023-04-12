from enum import Enum

from .celestial_object import CelestialObject


class SoloonColor(Enum):
    BLUE = "BLUE"
    RED = "RED"
    PURPLE = "PURPLE"
    WHITE = "WHITE"


class Soloon(CelestialObject):
    def __init__(self, r, c, color):
        super().__init__(r, c)
        self.color: SoloonColor = SoloonColor(color)
        self._endpoint = "soloons"

    def get_create_params(self):
        return {**self._get_basic_params(), "color": self.color.value.lower()}
