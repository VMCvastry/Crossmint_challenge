from .celestial_object import CelestialObject


class Polyanet(CelestialObject):
    def __init__(self, r, c):
        super().__init__(r, c)
        self._endpoint = "polyanets"

    def get_create_params(self):
        return self._get_basic_params()

    def __repr__(self):
        return f"Polyanet({self.row}, {self.column})"
