from __future__ import annotations
from .celestial_object import CelestialObject


class ComethDirection:
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    # UP = 0
    # DOWN = 1
    # LEFT = 2
    # RIGHT = 3

    @staticmethod
    def get_direction(direction: str) -> int:
        return ComethDirection.directions.index(direction)

    @staticmethod
    def get_name(direction: ComethDirection) -> str:
        return ComethDirection.directions[direction]


def get_direction(direction) -> ComethDirection:
    if direction == "UP":
        return ComethDirection.UP
    elif direction == "DOWN":
        return ComethDirection.DOWN
    elif direction == "LEFT":
        return ComethDirection.LEFT
    elif direction == "RIGHT":
        return ComethDirection.RIGHT
    else:
        raise ValueError(f"Invalid direction name: {direction}")


class Cometh(CelestialObject):
    def __init__(self, r, c, direction):
        super().__init__(r, c)
        self.direction: ComethDirection = ComethDirection.get_direction(direction)

    def get_create_params(self):
        return {
            **self._get_basic_params(),
            "direction": ComethDirection.get_name(self.direction),
        }
