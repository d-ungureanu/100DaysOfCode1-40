import requests
import config
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/3bc96fed85239a14d1abfd3b7403c6e4/flightDeals/prices"
SHEETY_AUTH_HEADER = {
    "Authorization": config.SHEETY_TOKEN
}


class DataManager:

    def __init__(self):
        self.sheet_data = {}

    def get_sheet_data(self):
        read_sheet = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_AUTH_HEADER)
        self.sheet_data = read_sheet.json()["prices"]
        return self.sheet_data

    def update_iata_codes(self):
        for city in self.sheet_data:
            upload_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            upload_response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                headers=SHEETY_AUTH_HEADER,
                json=upload_data
            )
            print("IATA code to upload: ", upload_response.text)
