from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from flight_data import FlightData



#get Google sheet data
data_manager = DataManager()
# sheet_data = data_manager.get_sheet_data()

# hard coded it to avoid reaching API requests limit
sheet_data = [
    {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
    {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
    {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
    {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
    {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
    {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
    {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
    {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
    {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}
]
print(sheet_data)


for entry in sheet_data:
    if not entry["iataCode"]:
        city = entry["city"]
        flight_search = FlightSearch()
        city_iata_code = flight_search.find_iata_code(city)
        entry["iataCode"] = city_iata_code

data_manager.sheet_data = sheet_data
data_manager.update_iata_codes()

for row in sheet_data:
    flight_data = FlightData()
    flight_info = flight_data.get_city_deal(row["iataCode"])
    routes_data = flight_info["route"]

    departure_city_name = routes_data[0]['cityFrom']
    departure_airport_iata_code = routes_data[0]['flyFrom']
    arrival_city_name= routes_data[0]['cityTo']
    arrival_airport_iata_code= routes_data[0]['flyTo']
    outbound_date= routes_data[0]['local_departure'].split("T")[0]
    inbound_date= routes_data[1]['local_arrival'].split("T")[0]
    round_trip_price = flight_info['price']

    print(f"Low price alert! Only £{round_trip_price} to fly from "
          f"{departure_city_name}-{departure_airport_iata_code} "
          f"to {arrival_city_name}-{arrival_airport_iata_code}, from {outbound_date} to {inbound_date}.")