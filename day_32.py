import smtplib
import datetime as dt
import random

MY_EMAIL = "singhthakuryashraj01@gmail.com"
PASSWORD = "pqkysdrgytnubuci"

current_date_and_time = dt.datetime.now()
current_day_of_week = current_date_and_time.weekday()
if current_day_of_week == 1:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Quotes on Tuesdays\n\n{random_quote}")


# my_email = "singhthakuryashraj01@gmail.com"
# password = "pqkysdrgytnubuci"
# 
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="thakuryashraj2002singh@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=2002, month=4, day=20)
# print(day_of_week, date_of_birth)
