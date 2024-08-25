import time
from data_manager import DataManager
from flight_search import FlightSearch


def update_iata_codes(cities, flights, data_storage):
    for row in cities:
        iata_code = flights.get_iata_code(row["city"])
        data_storage.update_data(row["id"], iata_code)

        # slowing down requests to avoid rate limit
        time.sleep(2)


data_manager = DataManager()
flight_searcher = FlightSearch()

data = data_manager.read_data()

# update_iata_codes(data, flight_searcher, data_manager)

for city in data:
    cheapest_flight = flight_searcher.find_cheapest_flight("LON", city["iataCode"])
    print(f"Destination: {cheapest_flight.destination} : Price: £{cheapest_flight.price}")

    # slowing down requests to avoid rate limit
    time.sleep(2)
