from __future__ import annotations

from celestial_objects import *
from materializer import Materializer


def parse_attribute(name: str) -> str:
    return name.split("_")[0]


class Megaverse:
    def __init__(self):
        self.grid: list[list[CelestialObject | None]] = []

    @classmethod
    def from_strings(cls, strings: list[list[str]]) -> Megaverse:
        megaverse = cls()
        for r, line in enumerate(strings):
            row = []
            for c, name in enumerate(line):
                if name == "SPACE":
                    row.append(None)
                elif name == "POLYANET":
                    row.append(Polyanet(r, c))
                elif "COMETH" in name:
                    direction = parse_attribute(name)
                    row.append(Cometh(r, c, direction))
                elif "SOLOON" in name:
                    color = parse_attribute(name)
                    row.append(Soloon(r, c, color))
                else:
                    raise ValueError(f"Invalid celestial object name: {name}")
            megaverse.grid.append(row)
        return megaverse

    def perform_action_on_object_type(
        self, obj_type: type[CelestialObject], action: callable[[CelestialObject], None]
    ):
        for row in self.grid:
            for cell in row:
                if cell is not None and isinstance(cell, obj_type):
                    while 1:
                        try:
                            action(cell)
                            print(action, cell)
                        except Materializer.TooManyRequests:
                            continue
                        break

    def materialize_megaverse(self, materializer: Materializer):
        # Assuming that the input grid is valid
        self.perform_action_on_object_type(Polyanet, materializer.create_object)
        # Soloons must be created after Polyplanets
        self.perform_action_on_object_type(Soloon, materializer.create_object)
        self.perform_action_on_object_type(Cometh, materializer.create_object)

    def dematerialize_megaverse(self, materializer: Materializer):
        self.perform_action_on_object_type(Soloon, materializer.delete_object)
        # Polyplanets must be deleted after Soloons
        self.perform_action_on_object_type(Polyanet, materializer.delete_object)
        self.perform_action_on_object_type(Cometh, materializer.delete_object)

    def clear_all(self, materializer: Materializer):
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                materializer.delete_object(CelestialObject(r, c))

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)
