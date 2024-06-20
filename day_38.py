import requests
import datetime

APP_ID = "a07bafdc"
API_KEY = "d2b2a77ede3f2ea2aca39863aa4d5c0a"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
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

sheety_endpoint = "https://api.sheety.co/45ba23757002f5ca89d08e8cedfa568a/workoutTracking/workouts"

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

    response = requests.post(url=sheety_endpoint, json=parameters)
    response.raise_for_status()
    print(response.text)
