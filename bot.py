import telebot
from telebot.types import Message
from os import getenv
from dotenv import load_dotenv


load_dotenv()
bot_token = getenv("TOKEN")
print("Using token ...", bot_token[-5:])


bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=["start"])
def handle_start(message: Message):
    print("Получена команда /start")
    username = message.from_user.full_name if message.from_user.full_name else message.from_user.username
    text = f"""Здравствуйте {username}
Я помогу вам изучать иностранные слова
Версия бота: 0.0.3
"""
    bot.send_message(message.chat.id, text)


@bot.message_handler()
def handle_message(message: Message):
    info = f"""Вы написали: `{message.text}`
Пользователь: `{message.from_user.username}`
Чат: `{message.chat.id}`
"""
    print(info)
    bot.send_message(message.chat.id, info, parse_mode="Markdown")


bot.infinity_polling()
