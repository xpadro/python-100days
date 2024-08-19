import os
import requests

SHEETS_ENDPOINT = os.getenv("SHEETS_API")


class DataManager:

    @staticmethod
    def read_data():
        content = requests.get(SHEETS_ENDPOINT)
        return content.json()['prices']
