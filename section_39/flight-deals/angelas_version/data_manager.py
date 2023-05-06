from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ebb01654d5ee1ae99f728ad2b4f66044/flightDealsApp/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        # self.destination_data = data["prices"]
        self.destination_data = [
            { "city": "Paris", "iataCode": "PAR", "lowestPrice": 54, "id": 2 },
            { "city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3 },
            { "city": "Tokyo", "iataCode": "FLR", "lowestPrice": 79, "id": 4 },
            { "city": "Prague", "iataCode": "PRG", "lowestPrice": 60, "id": 5 },
            { "city": "Istanbul", "iataCode": "IST", "lowestPrice": 95, "id": 6 },
            { "city": "Bucharest", "iataCode": "BUH", "lowestPrice": 150, "id": 7 },
            { "city": "Amsterdam", "iataCode": "AMS", "lowestPrice": 80, "id": 8 },
            { "city": "Malaga", "iataCode": "AGP", "lowestPrice": 100, "id": 9 },
            { "city": "Lisbon", "iataCode": "LIS", "lowestPrice": 90, "id": 10 }
        ]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)