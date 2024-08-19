from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
prices = data_manager.read_data()
print(prices)

flight_searcher = FlightSearch()
locations = flight_searcher.get_locations("Paris")
print(f"locations: {locations}")

