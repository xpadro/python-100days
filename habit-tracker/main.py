import requests
from datetime import datetime as dt


USERNAME = "xpadro"
USER_TOKEN = "ad3nw987wn98en"

API_BASE_URL = "https://pixe.la/v1"
API_CREATE_USER = f"{API_BASE_URL}/users"
API_CREATE_GRAPH = f"{API_BASE_URL}/users/{USERNAME}/graphs"
API_PIXEL = f"{API_BASE_URL}/users/{USERNAME}/graphs/graph1"


def create_user():
    parameters = {
        "token": USER_TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=API_CREATE_USER, json=parameters)
    return response


def call_post_api(url, parameters):
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

    return call_post_api(API_CREATE_GRAPH, parameters)


def add_pixel(add_date, num_commits):
    parameters = {
        "date": add_date,
        "quantity": num_commits
    }

    return call_post_api(API_PIXEL, parameters)


def update_pixel(update_date, num_commits):
    parameters = {
        "quantity": num_commits
    }

    headers = {
        "X-USER-TOKEN": USER_TOKEN
    }

    response = requests.put(url=f"{API_PIXEL}/{update_date}", json=parameters, headers=headers)
    return response


def format_date(date_to_format):
    return date_to_format.strftime("%Y%m%d")


# content = create_user()
# content = create_graph()
# content = add_pixel(format_date(dt.now()), "2")


date = dt(year=2024, month=8, day=16)
content = update_pixel(format_date(date), "3")

print(content.text)
