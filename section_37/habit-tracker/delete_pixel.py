import datetime as dt
import requests
import config

USERNAME = "tiptil"
TOKEN = config.pixela_token
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

auth_header = {
    "X-USER-TOKEN": TOKEN
}

today = dt.datetime.today().date().strftime("%Y%m%d")

pixel_delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today}"

pixel_response = requests.delete(url=pixel_delete_endpoint, headers=auth_header)
print(pixel_response.text)
