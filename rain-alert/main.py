import requests

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "YOUR_API_KEY"

PARAMETERS = {
    "lat": 41.548630,
    "lon": 2.107440,
    "appid": API_KEY,
    "cnt": 4
}

question_data = []

try:
    response = requests.get(URL, params=PARAMETERS)
    response.raise_for_status()
    body = response.json()
    rain_forecast = False

    for item in body["list"]:
        main_condition = item["weather"][0]
        id = main_condition["id"]
        description = main_condition["description"]
        print(f"{id} - {description}")
        if int(id) < 700:
            rain_forecast = True

    if rain_forecast:
        print("Bring an umbrella")
except Exception as e:
    print("Exception while calling weather API")
    print(e)