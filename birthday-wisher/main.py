import datetime as dt
import pandas
import random
import smtplib

GMAIL_SMTP = "smtp.gmail.com"
EMAIL = "your_email"
PASSWORD = "your_app_password"
BIRTHDAYS_FILE = "birthdays.csv"
LETTER_TEMPLATES_PATH = "letter_templates/"


def load_birthdays():
    birthdays = pandas.read_csv(BIRTHDAYS_FILE)

    # new_dict = {new_key: new_value for (index, row) in birthdays.iterrows()}
    return {(row["month"], row["day"]): row for (index, row) in birthdays.iterrows()}


def send_email(letter):
    with smtplib.SMTP(GMAIL_SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Happy Birthday!\n\n{letter}")


def send_birthday_wisher(person_name):
    letter_num = random.randint(1, 3)
    file_name = f"letter_{letter_num}.txt"

    with open(LETTER_TEMPLATES_PATH + file_name, "r") as f:
        letter = f.read()
        letter = letter.replace("[NAME]", person_name["name"])
        send_email(letter)


today = (dt.datetime.now().month, dt.datetime.now().day)
birthdays_dict = load_birthdays()

if today in birthdays_dict:
    person = birthdays_dict[today]
    send_birthday_wisher(person)






