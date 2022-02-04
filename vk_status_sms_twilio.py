import time
import os
import requests

from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
to = os.getenv('to')
from_ = os.getenv('from_')
vk_token = os.getenv('vk_token')


def get_status(user_id):
    params = {
        'user_id': user_id,
        'v': '5.131',
        'access_token': vk_token,
        'fields': 'online',
    }
    status = requests.post("https://api.vk.com/method/users.get", data=params).json()['response'][0]['online']
    return status  # Верните статус пользователя в ВК


def sms_sender(sms_text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to,
        from_=from_,
        body=sms_text,
    )
    return message.sid  # Верните sid отправленного сообщения из Twilio


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(30)
