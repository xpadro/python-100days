import os
import requests
from datetime import datetime as dt

TRACK_API_EXERCISE = "https://trackapi.nutritionix.com/v2/natural/exercise"
TRACK_APP_ID = os.getenv("TRACK_API_ID")
TRACK_API_KEY = os.getenv("TRACK_API_KEY")
SHEET_API_POST = os.getenv("SHEET_ENDPOINT")

GENDER = "male"
WEIGHT_KG = "50"
HEIGHT_CM = "180"
AGE = "40"

headers = {
    "x-app-id": TRACK_APP_ID,
    "x-app-key": TRACK_API_KEY,
}

body = {
    "query": "ran 3Km and cycled for 2Km",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

content = requests.post(TRACK_API_EXERCISE, json=body, headers=headers)
exercises = content.json()["exercises"]

now_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")
print(now_date)
print(now_time)

for exercise in exercises:
    sheet_row = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_API_POST, json=sheet_row)
    print(sheet_response.text)
