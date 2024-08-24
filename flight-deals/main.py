import time
from data_manager import DataManager
from flight_search import FlightSearch


def update_iata_codes(flights, data_storage):
    city_prices = data_storage.read_data()

    for row in city_prices:
        iata_code = flights.get_locations(row["city"])
        data_storage.update_data(row["id"], iata_code)

        # slowing down requests to avoid rate limit
        time.sleep(2)


data_manager = DataManager()
flight_searcher = FlightSearch()

update_iata_codes(flight_searcher, data_manager)
