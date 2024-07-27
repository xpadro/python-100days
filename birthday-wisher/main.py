import datetime as dt
import pandas
import random
import smtplib

email = "your_email"
password = "your_app_password"


today = (dt.datetime.now().month, dt.datetime.now().day)

birthdays = pandas.read_csv("birthdays.csv")

# new_dict = {new_key: new_value for (index, row) in birthdays.iterrows()}
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in birthdays.iterrows()}

if today in birthdays_dict:
    person = birthdays_dict[today]
    print(person["name"])

    letter_num = random.randint(1, 3)
    file_name = f"letter_{letter_num}.txt"

    with open("letter_templates/" + file_name, "r") as f:
        letter = f.read()
        letter = letter.replace("[NAME]", person["name"])
        print(letter)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{letter}")


