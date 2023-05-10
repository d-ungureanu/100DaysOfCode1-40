import smtplib

from twilio.rest import Client
import config


TWILIO_SID = config.TWILIO_SID
TWILIO_AUTH_TOKEN = config.TWILIO_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = config.TWILIO_VIRTUAL_NUMBER
TWILIO_VERIFIED_NUMBER = config.TWILIO_VERIFIED_NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)


    def send_emails(self, emails_list, message):
        with smtplib.SMTP(config.SMTP_SERV) as email_connection:
            email_connection.starttls()
            email_connection.login(user=config.sender_email, password=config.sender_pass)
            for email in emails_list:
                email_connection.sendmail(from_addr=config.sender_email,
                                          to_addrs=email,
                                          msg=f"Subject:NEW LOW PRICE ALERT!\n\n{message}".encode('utf-8'))
        print("Email sent successfully.")