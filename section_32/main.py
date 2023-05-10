import datetime as dt
import smtplib
import random

today = dt.datetime.now()
day_of_week = today.strftime("%A")

my_email = "tiptil@gmail.com"
my_password = ""
dest_email = "mic_tgv@yahoo.co.uk"
trigger = "Tuesday"

if day_of_week == trigger:
    with open("quotes.txt", "r") as quotes_file:
        lines = quotes_file.readlines()
        lines = [x.strip() for x in lines]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=dest_email,
                            msg=f"Subject:Quote of the day.\n\n{random.choice(lines)}")
