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

    def get_locations(self, city):
        token = self.token
        print(f"token: {token}")

        params = {
            "include": "AIRPORTS",
            "max": "2",  # Avoid reaching trial quota
            "keyword": city
        }

        headers = {
            "Authorization": f"Bearer {token}"
        }

        content = requests.get(GET_LOCATIONS, params=params, headers=headers)
        return content.json()
