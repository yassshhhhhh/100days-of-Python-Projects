# Monday Motivation emails.

# import smtplib
# import datetime as dt
# import random

# MY_EMAIL = "singhthakuryashraj01@gmail.com"
# PASSWORD = "pqkysdrgytnubuci"

# current_date_and_time = dt.datetime.now()
# current_day_of_week = current_date_and_time.weekday()
# if current_day_of_week == 1:
#     with open("quotes.txt") as file:
#         quotes = file.readlines()
#         random_quote = random.choice(quotes)
#     print(random_quote)

#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs=MY_EMAIL,
#                             msg=f"Subject:Quotes on Tuesdays\n\n{random_quote}")


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

# Birthday Wisher
##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "singhthakuryashraj01@gmail.com"
PASSWORD = "pqkysdrgytnubuci"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
rows = data.iterrows()

now = dt.datetime.now()
month = now.month
day = now.day
random_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# 2. Check if today matches a birthday in the birthdays.csv
for index, row in rows:
    if day == row.day and month == row.month:
        print(row["email"])
        print(row["name"])
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/{random.choice(random_letters)}") as file:
            content = file.read()
            replaced_text = content.replace("[NAME]", row["name"])
            # print(replaced_text)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=row["email"],
                                msg=f"Subject:Birthday Wishes\n\n{replaced_text}")

