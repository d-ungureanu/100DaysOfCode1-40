from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint



#get Google sheet data
data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()

for entry in sheet_data:
    if not entry["iataCode"]:
        city = entry["city"]
        flight_search = FlightSearch()
        city_iata_code = flight_search.find_iata_code(city)
        entry["iataCode"] = city_iata_code

data_manager.sheet_data = sheet_data
data_manager.update_iata_codes()