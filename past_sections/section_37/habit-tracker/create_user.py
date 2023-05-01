import requests
import config

USERNAME = "tiptil"
TOKEN = config.pixela_token

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}





#create new account in Pixela's API
pixela_response = requests.post(url=pixela_endpoint, json=user_params)
print(pixela_response.text)