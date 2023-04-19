# import smtplib
#
# my_email = "tiptil@gmail.com"
# my_password = "enzzutzitpwzdqto"
# dest_email = "mic_tgv@yahoo.co.uk"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=dest_email,
#                         msg="Subject:Python Test with not close()\n\nHello, this is an email from Python.")


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

DOB = dt.datetime(day=28, month=6, year=1977)
print(DOB)

print(now.year)
