import os
import requests
import telegram
import time


vk_token = "30e770f3e68d44887769e5a60756a9c7aa45ad957275a6fb10fec086944c4cbcffdae81a9d6a45b787d00"
bot_token = "5243422478:AAGc4_4OTKOleqdwAYRRnDHovbK0zVtImso"
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
