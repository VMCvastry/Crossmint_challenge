import requests
from celestial_objects import CelestialObject


class Materializer:
    def __init__(self):
        self.candidate_id = "7d2eedb3-970b-46a6-aed8-8e8468df09a4"

    class TooManyRequests(Exception):
        pass

    def get_grid(self):
        r = requests.get(
            f"https://challenge.crossmint.io/api/map/{self.candidate_id}/goal"
        )
        return r.json()["goal"]

    def create_object(self, o: CelestialObject):
        headers = {"Content-Type": "application/json"}
        r = requests.post(
            f"https://challenge.crossmint.io/api/{o.get_endpoint()}/",
            json={"candidateId": self.candidate_id, **o.get_create_params()},
            headers=headers,
        )
        validate_response(r)

    def delete_object(self, o: CelestialObject):
        headers = {"Content-Type": "application/json"}
        r = requests.delete(
            f"https://challenge.crossmint.io/api/polyanets/",
            json={"candidateId": self.candidate_id, **o.get_delete_params()},
            headers=headers,
        )
        validate_response(r)


def validate_response(r):
    if r.status_code == 429:
        raise Materializer.TooManyRequests()
    elif r.status_code != 200:
        raise Exception("Error: " + r.text)
    if r.text != "{}":
        print(r.text, "TEXT")
