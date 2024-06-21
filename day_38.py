import requests
import datetime
import os


APP_ID = os.environ["EV_APP_ID"]
API_KEY = os.environ["EV_API_KEY"]
API_ENDPOINT = os.environ["EV_API_ENDPOINT"]

exercises = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query_format = {
    "query": exercises,
}

response = requests.post(url=API_ENDPOINT, json=query_format, headers=headers)
response.raise_for_status()

print(response.status_code)

data = response.json()
today = datetime.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

sheety_endpoint = os.environ["EV_SHEETY_ENDPOINT"]
TOKEN = os.environ["EV_TOKEN"]

for exercise in data['exercises']:
    duration = exercise['duration_min']
    name = exercise['name'].title()
    calories = exercise['nf_calories']
    parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories,
        }
    }

    headers = {
        "Authorization": f"Basic {TOKEN}",
    }
    # response = requests.get(url=sheety_endpoint, headers=headers)
    # response.raise_for_status()
    # print(response.text)

    response = requests.post(url=sheety_endpoint, headers=headers, json=parameters)
    response.raise_for_status()
    print(response.text)
