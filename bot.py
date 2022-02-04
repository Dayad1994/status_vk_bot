import telegram
import os

from dotenv import load_dotenv
load_dotenv()


TELEGRAM_TOKEN = os.getenv('bot_token')  # добавить токен
CHAT_ID = '576415473'  # добавить chat_id


def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    return bot.send_message(chat_id=CHAT_ID, text=message)


message = 'Привет, я ботик, у меня баги'
send_message(message)