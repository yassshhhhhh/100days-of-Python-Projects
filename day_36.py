import requests
import smtplib

MY_EMAIL = "singhthakuryashraj01@gmail.com"
PASSWORD = "pqkysdrgytnubuci"

STOCK = "TSLA"
COMPANY_NAME = "tesla"
API_KEY = "Z9WW2LBKYO3W88Y0"
API_ENDPOINT = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "daily",
    "apikey": API_KEY,
}
response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
print(f"Status Code: {response.status_code}")

stock_data = response.json()
counter = 0
dby_date = ""
yesterday_stock_opening_price = None
yesterday_stock_closing_price = None
day_before_yesterday_stock_opening_price = None
day_before_yesterday_stock_closing_price = None

for daily_data in stock_data["Time Series (Daily)"]:
    # print(daily_data)
    counter += 1
    if counter == 1:
        yesterday_stock_opening_price = float(stock_data["Time Series (Daily)"][daily_data]["1. open"])
        yesterday_stock_closing_price = float(stock_data["Time Series (Daily)"][daily_data]["4. close"])
    elif counter == 2:
        dby_date = daily_data
        day_before_yesterday_stock_opening_price = float(stock_data["Time Series (Daily)"][daily_data]["1. open"])
        day_before_yesterday_stock_closing_price = float(stock_data["Time Series (Daily)"][daily_data]["4. close"])
    elif counter > 2:
        break
print(dby_date)
print(f"Y- Opening Price: {yesterday_stock_opening_price}")
print(f"Y- Closing Price: {yesterday_stock_closing_price}")
print(f"DBY- Opening Price: {day_before_yesterday_stock_opening_price}")
print(f"DBY- Closing Price: {day_before_yesterday_stock_closing_price}")

stock_percentage = (yesterday_stock_closing_price / day_before_yesterday_stock_closing_price) * 100
if yesterday_stock_closing_price < day_before_yesterday_stock_closing_price:
    stock_percentage -= 100
    print(stock_percentage)

if stock_percentage <= -5 or stock_percentage >= 5:
    news_parameters = {
        "q": COMPANY_NAME,
        "from": "2024-06-17",
        "sortBy": "publishedAt",
        "apikey": "a1e2f58216b54bb0ac389d1fed473e9b",
        "language": "en"
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()
    total_message = ""

    for news in range(3):
        title = news_data["articles"][news]["title"]
        description = news_data["articles"][news]["description"]
        message = f"Headline: {title}\nBrief: {description}\n"
        total_message += message

    print(total_message)
    subject = ""

    if stock_percentage > 0:
        subject += f"Tesla: 🔺{stock_percentage}%"
    else:
        subject += f"Tesla: 🔻{stock_percentage}%"

    print(subject)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:{subject} \n\n{total_message}")
else:
    print("Not Much.")

