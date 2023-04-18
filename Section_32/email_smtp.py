import smtplib

my_email = "tiptil@gmail.com"
my_password = "enzzutzitpwzdqto"
dest_email = "mic_tgv@yahoo.co.uk"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs=dest_email, msg="Hello, this is an email from Python.")
connection.close()