from __future__ import annotations
from .celestial_object import CelestialObject
from enum import Enum


class ComethDirection(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Cometh(CelestialObject):
    def __init__(self, r, c, direction):
        super().__init__(r, c)
        self.direction: ComethDirection = ComethDirection(direction)
        self._endpoint = "comeths"

    def get_create_params(self):
        return {**self._get_basic_params(), "direction": self.direction.value.lower()}

    def __repr__(self):
        return f"Cometh({self.row}, {self.column}, {self.direction.value})"
