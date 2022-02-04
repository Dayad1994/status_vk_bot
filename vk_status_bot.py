import os
import requests
import telegram
import time

from dotenv import load_dotenv
load_dotenv()

vk_token = os.getenv('vk_token')
bot_token = os.getenv('bot_token')
chat_id = '576415473'


def get_status(user_id):
    params = {
        'user_id': user_id,
        'v': '5.131',
        'access_token': vk_token,
        'fields': 'online',
    }
    status = requests.post("https://api.vk.com/method/users.get", data=params).json()['response'][0]['online']
    return status  # Верните статус пользователя в ВК


def send_message(message):
    bot = telegram.Bot(token=bot_token)
    return bot.send_message(chat_id=chat_id, text=message)


while True:
    if get_status(user_id=80711619) == 1:
        send_message('online')
    else:
        send_message('offline')
        break
    time.sleep(20)
