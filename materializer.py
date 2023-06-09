import requests
from celestial_objects import CelestialObject


class Materializer:
    def __init__(self):
        self.candidate_id = "7d2eedb3-970b-46a6-aed8-8e8468df09a4"

    class TooManyRequests(Exception):
        pass

    class RequestsImpasse(Exception):
        def __init__(self, message, errors):
            super().__init__(
                "Server not allowing any new request, impasse reached: " + message
            )
            self.errors = errors

    def get_grid(self) -> list[list[str]]:
        r = requests.get(
            f"https://challenge.crossmint.io/api/map/{self.candidate_id}/goal"
        )
        return r.json()["goal"]

    """
        Requests are pretty slow therefore a valid improvement
        would be to use asyncio to perform all the calls at the same time,
        of course this would mean that we would get way more TooManyRequests error to retry.
    """

    def perform_request(self, o: CelestialObject, params, request_func: callable):
        headers = {"Content-Type": "application/json"}
        r = request_func(
            f"https://challenge.crossmint.io/api/{o.get_endpoint()}/",
            json={"candidateId": self.candidate_id, **params},
            headers=headers,
        )
        validate_response(r)

    def create_object(self, o: CelestialObject):
        self.perform_request(o, o.get_create_params(), requests.post)

    def delete_object(self, o: CelestialObject):
        self.perform_request(o, o.get_delete_params(), requests.delete)


def validate_response(r):
    if r.status_code == 429:
        raise Materializer.TooManyRequests()
    elif r.status_code != 200:
        raise Exception("Error: " + r.text)
    if r.text != "{}":
        raise Exception("Unusual response: " + r.text)
