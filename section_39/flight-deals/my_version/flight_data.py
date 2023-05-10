from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import requests
import config

DEPARTURE_CITY = "LON"
TODAY = dt.today().date().strftime("%d/%m/%Y")
RETURN_FROM = (dt.today().date() + relativedelta(days=+7)).strftime("%d/%m/%Y")
RETURN_TO = (dt.today().date() + relativedelta(days=+28)).strftime("%d/%m/%Y")
SIX_MONTHS = (dt.today().date() + relativedelta(months=+6)).strftime("%d/%m/%Y")
TEQUILA_API_KEY = config.TEQUILA_API
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

tequila_header = {
    "apikey": TEQUILA_API_KEY
}

# print("________________________________________")
# print("today: ", TODAY)
# print("six months: ", SIX_MONTHS)
# print("Return from: ", RETURN_FROM)
# print("Return to: ", RETURN_TO)
# print("________________________________________")


class FlightData:
    def __init__(self):
        self.city_data = {}

    def get_city_deal(self, city_iata_code):
        search_params = {
            "fly_from": f"city:{DEPARTURE_CITY}",
            "fly_to": f"city:{city_iata_code}",
            "date_from": f"{TODAY}",
            "date_to": f"{SIX_MONTHS}",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "adults": 1,
            "curr": "GBP",
            "sort": "price"
        }
        response = requests.get(url=SEARCH_ENDPOINT, headers=tequila_header, params=search_params)
        data = response.json()["data"]
        city_data = data[0]
        return city_data
