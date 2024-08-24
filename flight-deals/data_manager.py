import os
import requests


class DataManager:
    def __init__(self):
        self.token = os.getenv("SHEETS_API")

    def read_data(self):
        content = requests.get(f"https://api.sheety.co/{self.token}/flightDealsPython/prices")
        return content.json()['prices']

    def update_data(self, row_id, iata_code):
        updated_data = {
            "price": {
                    "iataCode": iata_code
                }
        }

        result = requests.put(
            url=f"https://api.sheety.co/{self.token}/flightDealsPython/prices/{row_id}",
            json=updated_data
        )

        print(result.text)
