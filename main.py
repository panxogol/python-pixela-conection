# --- IMPORTS ---
import requests as req
from constants import *


# --- CONSTANTS ---
PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USER_PARAMS = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# --- FUNCTIONS ---
def main():
    # Create user
    # res = req.post(url=PIXELA_USER_ENDPOINT, json=PIXELA_USER_PARAMS)
    # print(res.text)

    # Create new graph
    graph_endpoint = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USER}/graps"
    headers = {
        "X_USER_TOKEN": PIXELA_TOKEN,
    }
    graph_config = {
        "id": "code_lines",
        "name": "lines of code written",
        "unit": "lines",
        "type": "int",
        "color": "kuro",
    }

    res = req.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(res.text)


# --- RUN ---
if __name__ == '__main__':
    main()
