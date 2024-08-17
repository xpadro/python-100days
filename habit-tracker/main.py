import requests
from datetime import datetime as dt


USERNAME = "xpadro"
USER_TOKEN = "ad3nw987wn98en"

API_BASE_URL = "https://pixe.la/v1"
API_CREATE_USER = f"{API_BASE_URL}/users"
API_CREATE_GRAPH = f"{API_BASE_URL}/users/{USERNAME}/graphs"
API_ADD_PIXEL = f"{API_BASE_URL}/users/{USERNAME}/graphs/graph1"


def create_user():
    parameters = {
        "token": USER_TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=API_CREATE_USER, json=parameters)
    return response


def call_api(url, parameters):
    headers = {
        "X-USER-TOKEN": USER_TOKEN
    }

    response = requests.post(url=url, json=parameters, headers=headers)
    return response


def create_graph():
    parameters = {
        "id": "graph1",
        "name": "first-graph",
        "unit": "commit",
        "type": "int",
        "color": "sora"
    }

    return call_api(API_CREATE_GRAPH, parameters)


def add_pixel(date, num_commits):
    parameters = {
        "date": date,
        "quantity": num_commits
    }

    return call_api(API_ADD_PIXEL, parameters)


# content = create_user()
# content = create_graph()

today = dt.now().strftime("%Y%m%d")
content = add_pixel(today, "2")
print(content.text)
