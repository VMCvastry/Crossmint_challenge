from __future__ import annotations

import time

from celestial_objects import *
from materializer import Materializer


def parse_attribute(name: str) -> str:
    return name.split("_")[0]


def create_obj_from_string(r, c, name) -> CelestialObject | None:
    if name == "SPACE":
        return None
    elif name == "POLYANET":
        return Polyanet(r, c)
    elif "COMETH" in name:
        direction = parse_attribute(name)
        try:
            return Cometh(r, c, direction)
        except ValueError:
            raise ValueError(f"Invalid direction for Cometh: {direction}")
    elif "SOLOON" in name:
        color = parse_attribute(name)
        try:
            return Soloon(r, c, color)
        except ValueError:
            raise ValueError(f"Invalid color for Soloon: {color}")
    else:
        raise ValueError(f"Invalid celestial object name: {name}")


class Megaverse:
    def __init__(self):
        self.grid: list[list[CelestialObject | None]] = []

    @classmethod
    def from_strings(cls, strings: list[list[str]]) -> Megaverse:
        megaverse = cls()
        for r, line in enumerate(
            strings
        ):  # A nested list comprehension would be more elegant but less readable.
            row = [create_obj_from_string(r, c, name) for c, name in enumerate(line)]
            megaverse.grid.append(row)
        return megaverse

    def perform_action_on_object_type(
        self, obj_type: type[CelestialObject], action: callable[[CelestialObject], None]
    ):
        backoff_time = 1
        num_retries = 0
        for row in self.grid:
            for cell in row:
                if cell is not None and isinstance(cell, obj_type):
                    while True:
                        try:
                            action(cell)
                            backoff_time = 1
                            num_retries = 0
                        except Materializer.TooManyRequests:
                            if num_retries > 10:
                                raise Materializer.RequestsImpasse
                            num_retries += 1
                            backoff_time *= 2
                            time.sleep(backoff_time)
                            continue
                        break

    def materialize_megaverse(self, materializer: Materializer):
        # Assuming that the input grid is valid.
        self.perform_action_on_object_type(Polyanet, materializer.create_object)
        # Soloons must be created after Polyplanets.
        self.perform_action_on_object_type(Soloon, materializer.create_object)
        self.perform_action_on_object_type(Cometh, materializer.create_object)

    def dematerialize_megaverse(self, materializer: Materializer):
        self.perform_action_on_object_type(Soloon, materializer.delete_object)
        # Polyplanets must be deleted after Soloons.
        self.perform_action_on_object_type(Polyanet, materializer.delete_object)
        self.perform_action_on_object_type(Cometh, materializer.delete_object)

    def clear_all(self, materializer: Materializer):
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                materializer.delete_object(CelestialObject(r, c))

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)
