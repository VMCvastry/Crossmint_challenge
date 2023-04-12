candidate_id = "7d2eedb3-970b-46a6-aed8-8e8468df09a4"


class CelestialObject:
    def __init__(self, r, c):
        self.row = r
        self.column = c

    def _get_basic_params(self):
        return {"row": self.row, "column": self.column, "candidateId": candidate_id}

    def get_delete_params(self):
        return self._get_basic_params()

    # abstract method
    def get_create_params(self):
        raise NotImplementedError()
