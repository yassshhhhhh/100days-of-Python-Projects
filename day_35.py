import requests

LAT = 17.385044
LONG = 78.486671
API_KEY = "9e88940698f2ca4427b295ed8a405f58"
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
print(f"Status_code: {response.status_code}")

weather_data = response.json()

# for w_id in range(4):
#     weather_id = weather_data['list'][w_id]['weather'][0]['id']
#     print(f"Weather ID: {weather_id}")
#     if weather_id < 700:
#         print("Bring an Umbrella.")
#     # else:
#     #     print("Weather seems fine!")


will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    print(condition_code)
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella.")

