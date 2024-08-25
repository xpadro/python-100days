import os
import requests


class DataManager:
    """
    Manages the access to preferred city data from Google Sheets
    """
    def __init__(self):
        self.token = os.getenv("SHEETS_API")

    def read_data(self) -> list:
        """
        Retrieves the data about preferred cities
        :return: list of city data
        """
        content = requests.get(f"https://api.sheety.co/{self.token}/flightDealsPython/prices")
        return content.json()['prices']

    def update_data(self, row_id, iata_code):
        """
        Updates the IATA code from the city located in the specified row from Google Sheets
        :param row_id:
        :param iata_code:
        :return: None
        """
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
