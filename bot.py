import telebot
from telebot.types import Message
from os import getenv
from dotenv import load_dotenv


load_dotenv()
bot_token = getenv("TOKEN")
print("Using token ...", bot_token[-5:])


bot = telebot.TeleBot(bot_token)


@bot.message_handler()
def handle_message(message: Message):
    info = f"""Вы написали: `{message.text}`
Пользователь: `{message.from_user.username}`
Чат: `{message.chat.id}`"""
    print(info)
    bot.send_message(message.chat.id, info, parse_mode="Markdown")


bot.infinity_polling()