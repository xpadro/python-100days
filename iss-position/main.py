import requests
import datetime as dt

BCN_LAT = 41.385063
BCN_LNG = 2.173404

PARAMETERS = {
    "lat": BCN_LAT,
    "lng": BCN_LNG,
    "formatted": 0
}


def call_iss_position_api():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        return response.json()
    except:
        print("Failed calling iss-position API")


def call_sunrise_api():
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
        response.raise_for_status()
        return response.json()
    except:
        print("Failed calling sunrise-sunset API")


def extract_hour(time_json):
    return int(time_json.split("T")[1].split(":")[0])


def is_close(current_coord, target_coord):
    margin_left = target_coord - 5
    margin_right = target_coord + 5

    return margin_left < current_coord < margin_right


def is_night():
    data = call_sunrise_api()
    sunrise_hour = extract_hour(data["results"]["sunrise"])
    sunset_hour = extract_hour(data["results"]["sunset"])
    now_hour = dt.datetime.now().hour

    return sunrise_hour > now_hour > sunset_hour


def is_iss_overlap():
    iss_data = call_iss_position_api()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    return is_close(BCN_LAT, iss_lat) and is_close(BCN_LNG, iss_lng)


is_night = is_night()

if is_night and is_iss_overlap():
    print("Look above!")
elif not is_night:
    print("Still daylight")
else:
    print("Not close")
