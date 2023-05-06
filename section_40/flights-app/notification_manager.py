import config
from data_manager import DataManager
import smtplib


class NotificationManager:

    def __init__(self):
        self.sender_email = config.sender_email
        self.sender_pass = config.sender_pass
        self.dest_email = ""
        self.smtp_server = config.SMTP_SERV
        self.data_manager = DataManager()
        self.users_list = []

    def send_emails(self, message):
        with smtplib.SMTP(self.smtp_server) as email_connection:
            self.users_list = self.data_manager.get_users_list()
            email_connection.starttls()
            email_connection.login(user=self.sender_email, password=self.sender_pass)
            for user in self.users_list:

                email_connection.sendmail(from_addr=self.sender_email,
                                          to_addrs=user["email"],
                                          msg=message)
        print("Email sent successfully.")

    # def send_sms(self, message):
    #     message = self.client.messages.create(
    #         body=message,
    #         from_=TWILIO_VIRTUAL_NUMBER,
    #         to=TWILIO_VERIFIED_NUMBER,
    #     )
    #     # Prints if successfully sent.
    #     print(message.sid)