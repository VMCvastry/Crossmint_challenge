from __future__ import annotations
from .celestial_object import CelestialObject
from enum import Enum


class ComethDirection(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


# def get_direction(direction) -> ComethDirection:
#     if direction == "UP":
#         return ComethDirection.UP
#     elif direction == "DOWN":
#         return ComethDirection.DOWN
#     elif direction == "LEFT":
#         return ComethDirection.LEFT
#     elif direction == "RIGHT":
#         return ComethDirection.RIGHT
#     else:
#         raise ValueError(f"Invalid direction name: {direction}")


_directions = ["UP", "DOWN", "LEFT", "RIGHT"]


def get_direction(direction: str) -> ComethDirection:
    return ComethDirection(_directions.index(direction))


def get_name(direction: ComethDirection) -> str:
    return _directions[direction.value]


class Cometh(CelestialObject):
    def __init__(self, r, c, direction):
        super().__init__(r, c)
        self.direction: ComethDirection = ComethDirection.get_direction(direction)

    def get_create_params(self):
        return {
            **self._get_basic_params(),
            "direction": ComethDirection.get_name(self.direction),
        }
