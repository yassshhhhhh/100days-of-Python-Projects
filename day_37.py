import requests
import datetime

GRAPH = "https://pixe.la/v1/users/yashraj07/graphs/graph1.html"
TOKEN = "chigg40nigga40igga40"
USERNAME = "yashraj07"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Updating Graph.
graph_update = {
    "name": "Gym",
    "unit": "Hours",
    "type": "float",
    "color": "momiji",
}
# response = requests.put(url=f"{graph_endpoint}/{GRAPH_ID}", json=graph_update, headers=headers)
# print(response.text)

current_date = datetime.datetime.now()
date_format = current_date.strftime("%Y%m%d")

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": date_format,
    "quantity": input("How many hours did you spent in the gym today?: "),
}
# For Posting Pixels
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixel_endpoint}/{date_format}"
pixel_update = {
    "quantity": "11.3",
}
# For Updating Pixels
# response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)
# print(response.text)

# For Deleting Pixels.
# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)
