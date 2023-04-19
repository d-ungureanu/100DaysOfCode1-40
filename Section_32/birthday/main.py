import os
import random
import smtplib
import pandas as pd
import datetime as dt

sender_email = "tiptil@gmail.com"
sender_pass = ""
dest_email = ""

today = dt.datetime.now()
today_month = today.month
today_day = today.day
name_to_email = ""

df = pd.read_csv("birthdays.csv")
birthday_dict = {}
for _, row in df.iterrows():
    birthday_dict[(row["month"], row["day"])] = row.to_dict()

if (today_month, today_day) in birthday_dict:
    name_to_email = birthday_dict[(today_month, today_day)]["name"]
    dest_email = birthday_dict[(today_month, today_day)]["email"]
    templates_list = os.listdir("./letter_templates")
    chosen_template = random.choice(templates_list)
    with open(f"./letter_templates/{chosen_template}", "r") as template_to_use:
        template_text = template_to_use.read()
    template_text = template_text.replace("[NAME]", name_to_email)
    with smtplib.SMTP("smtp.gmail.com") as email_connection:
        email_connection.starttls()
        email_connection.login(user=sender_email, password=sender_pass)
        email_connection.sendmail(from_addr=sender_email,
                                  to_addrs=dest_email,
                                  msg=f"Subject: Happy Birthday!\n\n{template_text}")
    print("Email sent successfully.")
