from __future__ import annotations

from celestial_objects import *


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
