import requests
import config

api_key = config.api_key
leeds_lat = 53.800755
leeds_lon = -1.549077
ozd_lat = 48.219560
ozd_lon = 20.286920

api_url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": ozd_lat,
    "lon": ozd_lon,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url=api_url, params=parameters)
response.raise_for_status()

three_hours_list = response.json()["list"]

list_12h = three_hours_list[0:5]

weather_id_list = [int(entry["weather"][0]["id"]) for entry in list_12h]

will_rain = False

for weather_id in weather_id_list:
    if weather_id < 700:
        will_rain=True

if will_rain:
    print("Bring an umbrella.")

