import os
import requests

SHEETS_ENDPOINT = os.getenv("SHEETS_API")


class DataManager:
    def __init__(self):
        self.endpoint = os.getenv("SHEETS_API")

    def read_data(self):
        content = requests.get(self.endpoint)
        return content.json()['prices']
