import config
import requests

LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = config.TEQUILA_API

class FlightSearch:


    def find_iata_code(self, city_name: str):
        location_query_data = {
            "term": city_name,
            "location_types": "city"
        }

        tequila_header = {
            "apikey": TEQUILA_API_KEY
        }
        response =requests.get(url=LOCATION_ENDPOINT, params=location_query_data, headers=tequila_header)
        response_data=response.json()["locations"]
        iata_code = response_data[0]["code"]

        return iata_code
