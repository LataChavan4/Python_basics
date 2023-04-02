import smtplib
import datetime as dt
import random

with open("quotes.txt", "r") as f:
    quote = f.readlines()
    today_quote = random.choice(quote)
    print(quote)
now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "emailid from which you want to send mail"
password = "app_password"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

if day_of_week == 6:
    connection.sendmail(from_addr=my_email, to_addrs="emailid to which you want to send an email",
                        msg=f"subject:Happy Sunday\n\n{today_quote}\n regards\n Lata")

connection.close()
