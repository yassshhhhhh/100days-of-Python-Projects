# Kanye quotes
# from tkinter import *
# import requests


# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     quote = data["quote"]
#     canvas.itemconfig(quote_text, text=quote)


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)

# window.mainloop()

# --------------------------------------------------------------------------------------------------------
# ISS overhead notifier.
import requests
from datetime import datetime
import smtplib

LAT = 17.385044
LONG = 78.486671
URL = "https://api.sunrisesunset.io/json"
MY_EMAIL = "singhthakuryashraj01@gmail.com"
PASSWORD = "pqkysdrgytnubuci"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_position = (iss_longitude, iss_latitude)
print(iss_position)


def compare_position(iss_lat, iss_long):
    if (LAT - 5) <= iss_lat <= (LAT + 5) and (LONG - 5) <= iss_long <= (LONG + 5):
        print("The International space station can be visible in the sky today.")
        return True
    else:
        print("Not today pal!")
        return False


parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
    "tzid": "Indian/Maldives"
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

is_visible = compare_position(iss_latitude, iss_longitude)

if is_visible:
    if time_now >= sunset or time_now <= sunrise:   # To determine whether it's dark or not.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:ISS Location\n\nThe International space station can be visible in the sky today."
                                    f"\nLatitude: {iss_latitude}, Longitude: {iss_longitude}.\n"
                                    f"To witness look up in the sky.")
