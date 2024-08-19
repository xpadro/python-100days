from data_manager import DataManager

manager = DataManager()
prices = manager.read_data()
print(prices)
