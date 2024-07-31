import requests

URL = "https://opentdb.com/api.php"

PARAMETERS = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

question_data = []

try:
    response = requests.get(URL, params=PARAMETERS)
    response.raise_for_status()
    question_data = response.json()["results"]
except:
    print("Exception while calling opentdb API")
