import requests

USERNAME = "xpadro"
USER_TOKEN = "ad3nw987wn98en"

API_CREATE_USER = "https://pixe.la/v1/users"
API_CREATE_GRAPH = f"https://pixe.la/v1/users/{USERNAME}/graphs"
API_ADD_PIXEL = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"


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
content = add_pixel("20240816", "2")

print(content.text)
