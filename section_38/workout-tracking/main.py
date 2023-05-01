import time

import config
import requests
import datetime as dt

APP_ID = config.APP_ID
API_KEY = config.API_KEY
GENDER = "male"
WEIGHT = 145
HEIGHT = 195
AGE = 45

exercise_date = dt.datetime.today().strftime("%d/%m/%Y")
exercise_time = dt.datetime.now().strftime("%I:%M:%S %p")

user_input = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

auth_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}



response = requests.post(url=exercise_endpoint, json=exercise_params, headers=auth_header)
exercises_list = response.json()["exercises"]


ex_post_endpoint = "https://api.sheety.co/3bc96fed85239a14d1abfd3b7403c6e4/workoutsTracking/workouts"

sheety_auth_header = {
    "Authorization": "Bearer ThisIsMyToken"
}

for entry in exercises_list:

    exercise_date = dt.datetime.today().strftime("%d/%m/%Y")
    exercise_time = dt.datetime.now().strftime("%I:%M:%S %p")
    exercise_name = entry["name"].title()
    exercise_duration = entry["duration_min"]
    exercise_calories = entry["nf_calories"]
    exercise_id = entry["tag_id"]


    exercise_upload_data = {
        "workout": {
            "date": exercise_date,
            "time": exercise_time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories,
            "id": exercise_id
        }
    }
    ex_upload = requests.post(url=ex_post_endpoint, json=exercise_upload_data, headers=sheety_auth_header)
    print(ex_upload.json())
