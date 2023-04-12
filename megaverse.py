from __future__ import annotations

from celestial_objects import *


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
