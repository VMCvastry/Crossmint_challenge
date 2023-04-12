import requests

candidate_id = "7d2eedb3-970b-46a6-aed8-8e8468df09a4"

# For phase one i just tested the api and didnt put much effort into making clean code.
# For phase two i refactored everything.


class TooManyRequests(Exception):
    pass


def validate_response(r):
    if r.status_code == 429:
        raise TooManyRequests()
    elif r.status_code != 200:
        raise Exception("Error: " + r.text)
    if r.text != "{}":
        print(r.text, "TEXT")


def get_grid():
    r = requests.get(f"https://challenge.crossmint.io/api/map/{candidate_id}/goal")
    return r.json()["goal"]


def create_polyanet(r, c):
    headers = {"Content-Type": "application/json"}
    r = requests.post(
        f"https://challenge.crossmint.io/api/polyanets/",
        json={"row": r, "column": c, "candidateId": candidate_id},
        headers=headers,
    )
    validate_response(r)


def delete_polyanet(r, c):
    headers = {"Content-Type": "application/json"}
    r = requests.delete(
        f"https://challenge.crossmint.io/api/polyanets/",
        json={"row": r, "column": c, "candidateId": candidate_id},
        headers=headers,
    )
    validate_response(r)


def achieve_goal():
    grid = get_grid()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "POLYANET":
                while 1:
                    try:
                        create_polyanet(r, c)
                    except TooManyRequests:
                        continue
                    break


def clear_grid():
    grid = get_grid()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "POLYANET":
                while 1:
                    try:
                        delete_polyanet(r, c)
                    except TooManyRequests:
                        continue
                    break


if __name__ == "__main__":
    print(get_grid())
    achieve_goal()
    # clear_grid()
    # print(delete_polyanet(5, 5))
