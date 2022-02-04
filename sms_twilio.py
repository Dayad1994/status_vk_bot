from twilio.rest import Client

import os
from dotenv import load_dotenv
load_dotenv()


account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
to = os.getenv('to')
from_ = os.getenv('from_')
vk_token = os.getenv('access_token')

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=to,
    from_=from_,
    body="Hello mot!")

print(message.sid)
