import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_message(to='+918269301199', mssg_body='Hello! Yohohhoh'):
    account_sid = os.environ['Twilio_Account_sid']
    auth_token = os.environ['Twilio_auth_tokent']
    client = Client(account_sid, auth_token)
    sender= os.environ['twilio_phone_num']

    message = client.messages \
                    .create(
                        body=mssg_body,
                        from_= sender,
                        to=to
                    )

    print(message.status)


# send_message('+918269301199', 'Hello! I think it will rain today, So get your umberalla')