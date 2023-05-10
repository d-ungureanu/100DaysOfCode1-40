import datetime as dt
import requests
import config

USERNAME = "tiptil"
TOKEN = config.pixela_token
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

auth_header ={
    "X-USER-TOKEN": TOKEN
}


pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = dt.datetime.today().date().strftime("%Y%m%d")
pixel_config = {
    "date": today,
    "quantity": "272"
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=auth_header)
print(pixel_response.text)