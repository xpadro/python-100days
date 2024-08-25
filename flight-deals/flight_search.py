import os
import requests
from datetime import datetime as dt
from datetime import timedelta as delta
from flight_data import FlightData

AUTH_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
GET_LOCATIONS = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
GET_FLIGHT_OFFERS = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:

    def __init__(self):
        self.api_key = os.getenv("FLIGHTS_API_KEY")
        self.api_secret = os.getenv("FLIGHTS_API_SECRET")
        self.token = self._get_token()

    def _get_token(self):
        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        return requests.post(AUTH_TOKEN_ENDPOINT, headers=headers, data=data).json()['access_token']

    @staticmethod
    def _map_response(data):
        cheapest_flight = None
        lowest_price = None

        for item in data["data"]:
            price = item["price"]["grandTotal"]

            if lowest_price is None or price < lowest_price:
                # Cheapest flight in first itinerary and segment
                origin = item["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                destination = item["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                from_date = item["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                to_date = item["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                cheapest_flight = FlightData(price, origin, destination, from_date, to_date)

        return cheapest_flight

    def get_iata_code(self, city):
        """

        :param city:
        :return: The IATA code for the first matching city. If response is empty, returns "N/A".
        If city is not found, returns "NOT FOUND"
        """
        print(f"Retrieving IATA code for: {city}...")

        params = {
            "max": "2",  # Avoid reaching trial quota
            "keyword": city
        }

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        response = requests.get(GET_LOCATIONS, params=params, headers=headers)

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code

    def find_cheapest_flight(self, origin_code, destination_code):
        tomorrow = (dt.today() + delta(days=1)).strftime("%Y-%m-%d")
        in_six_months = (dt.now() + delta(days=(6 * 30))).strftime("%Y-%m-%d")

        params = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": tomorrow,
            "returnDate": in_six_months,
            "adults": 1,
            "currencyCode": "GBP",
            "max": 2
        }

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        response = requests.get(GET_FLIGHT_OFFERS, params=params, headers=headers)
        return self._map_response(response.json())
