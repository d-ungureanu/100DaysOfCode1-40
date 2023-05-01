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




today = dt.datetime.today().date().strftime("%Y%m%d")

pixel_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today}"

new_pixel_data = {
    "quantity": "7500"
}

pixel_response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=auth_header)
print(pixel_response.text)