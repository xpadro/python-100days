import smtplib
import datetime as dt
import random

email = "your_email"
password = "your_app_password"


def get_quote():
    with open("quotes.txt", "r") as f:
        chosen_quote = f.read().splitlines()
        return random.choice(chosen_quote)


def send_quote(quote):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Today quote\n\n{quote}")


now = dt.datetime.now()
if now.weekday() == 6:
    today_quote = get_quote()
    send_quote(today_quote)

