##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import datetime as dt
import random

data = pd.read_csv("birthdays.csv")
print(type(data))

today = dt.datetime.today()
print(today)
month = today.month
date = today.day
print(date)


letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

my_email = ""
password = ""
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

for i in range(len(data)):
    if data.loc[i, "month"] == month and data.loc[i, "day"] == date:
        with open(letter_path) as f:
            letter = f.read()
            new_letter = letter.replace("[NAME]", data.loc[i, "name"])
            connection.sendmail(from_addr=my_email,
                                to_addrs=data.loc[i, "email"],
                                msg=f"Subject: Happy Birthday\n\n{new_letter}")
            connection.close()





