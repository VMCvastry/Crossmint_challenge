class CelestialObject:
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self._endpoint = None

    def _get_basic_params(self):
        return {"row": self.row, "column": self.column}

    def get_delete_params(self):
        return self._get_basic_params()

    # abstract method
    def get_create_params(self):
        raise NotImplementedError()

    def get_endpoint(self):
        if self._endpoint is None:
            raise NotImplementedError()
        return self._endpoint
