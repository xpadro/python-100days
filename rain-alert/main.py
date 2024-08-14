import os
import requests
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_SID')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_VIRTUAL_PHONE = os.environ.get('TWILIO_VIRTUAL_PHONE')
TWILIO_TARGET_PHONE = os.environ.get('TWILIO_TARGET_PHONE')

URL = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')

PARAMETERS = {
    "lat": 41.548630,
    "lon": 2.107440,
    "appid": WEATHER_API_KEY,
    "cnt": 4
}

question_data = []


def call_weather_api():
    response = requests.get(URL, params=PARAMETERS)
    response.raise_for_status()
    return response.json()


def is_rainy(condition):
    forecast = False

    main_condition = condition["weather"][0]
    condition_id = main_condition["id"]
    description = main_condition["description"]
    print(f"{condition_id} - {description}")

    if int(condition_id) < 700:
        forecast = True

    return forecast


def send_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_TOKEN)

    message = client.messages.create(
        body="It's going to rain. Bring an umbrella",
        from_=TWILIO_VIRTUAL_PHONE,
        to=TWILIO_TARGET_PHONE
    )

    print(message.sid)


def main():
    try:
        content = call_weather_api()

        rain_forecast = False

        for item in content["list"]:
            rain_forecast = is_rainy(item)

        if rain_forecast:
            print("Bring an umbrella")
            send_sms()
    except Exception as e:
        print("Exception while calling weather API")
        print(e)


main()
