import os
import requests

AUTH_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
GET_LOCATIONS = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


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
