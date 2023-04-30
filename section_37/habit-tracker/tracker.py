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


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Steps Graph",
    "unit": "steps",
    "type": "int",
    "timezone": "GMT",
    "color": "sora"  # blue
}

graph_auth_header ={
    "X-USER-TOKEN": TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_auth_header)
print(graph_response.text)
