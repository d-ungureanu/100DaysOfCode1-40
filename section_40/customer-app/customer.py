import config
import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/ebb01654d5ee1ae99f728ad2b4f66044/flightDeals/users"
SHEETY_AUTH_HEADER = {
    "Authorization": config.SHEETY_TOKEN
}


def get_details():
    print("Welcome to Daniel's Flight Club.")
    print("We find the best deals and email them to you.")
    print("What is your first name?")
    first_name = input().title()
    print("What is your last name?")
    last_name = input().title()
    while True:
        print("What is your email?")
        email_1 = input().lower()
        print("Type your email again.")
        email_2 = input().lower()
        if email_1 == email_2:
            print("You're in the club!")
            break
        elif email_2 == "exit" or email_2 == "quit":
            exit()
        else:
            print("Emails don't match!!!")
    return {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email_1
        }
    }


data = {'user': {'firstName': 'Dan', 'lastName': 'Tan', 'email': 'dan@man.co'}}


def upload_user_details(data: dict):
    response = requests.post(
        url=f"{SHEETY_USERS_ENDPOINT}",
        json=data,
        headers=SHEETY_AUTH_HEADER
    )
    print("Upload response code: ", response.status_code)


def get_sheet_data():
    response = requests.get(url="https://api.sheety.co/ebb01654d5ee1ae99f728ad2b4f66044/flightDeals/users",
                            headers=SHEETY_AUTH_HEADER)
    print(response.json())


user_data = get_details()
# data = get_sheet_data()
upload_user_details(user_data)
