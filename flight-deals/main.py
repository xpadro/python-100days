from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
prices = data_manager.read_data()
print(prices)

flight_searcher = FlightSearch()
city_code = flight_searcher.get_locations("BARCELONA")
print(f"City Code: {city_code}")
