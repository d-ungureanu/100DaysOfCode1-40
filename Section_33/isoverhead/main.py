import requests
import config
from datetime import datetime
import smtplib
import time




def is_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_diff = abs(iss_latitude - int(config.MY_LAT))
    lng_diff = abs(iss_longitude - int(config.MY_LONG))

    return lat_diff <= 5 and lng_diff <= 5

def is_night():
    parameters = {
        "lat": config.MY_LAT,
        "lng": config.MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = int(datetime.now().hour)

    return True if sunrise <= time_now < sunset else False

while True:
    if is_near() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as email_connection:
            email_connection.starttls()
            email_connection.login(user=config.sender_email, password=config.sender_pass)
            email_connection.sendmail(from_addr=config.sender_email,
                                      to_addrs=config.dest_email,
                                      msg=f"Subject: Look up\n\nISS is visible tonight from your location")
        print("Email sent successfully.")
    time.sleep(60)

