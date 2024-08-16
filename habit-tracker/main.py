import requests

API_CREATE_USER = "https://pixe.la/v1/users"
API_CREATE_GRAPH = "https://pixe.la/v1/users/xpadro/graphs"
USER_TOKEN = "ad3nw987wn98en"


def create_user():
    parameters = {
        "token": USER_TOKEN,
        "username": "xpadro",
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=API_CREATE_USER, json=parameters)
    return response


def create_graph():
    parameters = {
        "id": "graph1",
        "name": "first-graph",
        "unit": "commit",
        "type": "int",
        "color": "sora"
    }

    headers = {
        "X-USER-TOKEN": USER_TOKEN
    }

    response = requests.post(url=API_CREATE_GRAPH, json=parameters,  headers=headers)
    return response


# User is already created
#content = create_user()
# print(content.text)

content = create_graph()
print(content.text)