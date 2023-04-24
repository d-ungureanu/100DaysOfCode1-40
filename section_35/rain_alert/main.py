import requests
import config

api_key = config.api_key
leeds_lat = 53.800755
leeds_lon = -1.549077
api_url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": 53.800755,
    "lon": -1.549077,
    "appid": "***REMOVED***"
}

response = requests.get(url=api_url, params=parameters)
response.raise_for_status()
print(response.status_code)
print(response.json())
