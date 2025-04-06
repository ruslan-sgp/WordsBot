# @PyBotWords_Bot


import telebot
from telebot.types import Message
from os import getenv
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup
from random import randint


load_dotenv()
bot_token = getenv("TOKEN")
print("Using token ...", bot_token[-5:])


bot = telebot.TeleBot(bot_token)

words_dict = {
    'apple': 'яблоко',
    'book': 'книга',
    'cat': 'кот',
    'dog': 'собака',
    'egg': 'яйцо',
    'fish': 'рыба',
    'house': 'дом',
    'tree': 'дерево',
    'sun': 'солнце',
    'moon': 'луна',
    'car': 'машина',
    'pen': 'ручка',
    'chair': 'стул',
    'water': 'вода',
    'milk': 'молоко',
    'bird': 'птица',
    'table': 'стол',
    'ball': 'мяч',
    'hand': 'рука',
    'window': 'окно'
}

word_pairs = [x for x in words_dict.items()]

def send_word(message):

    random4 = []
    while len(random4) < 4:
        new_pair = word_pairs[randint(0, len(word_pairs) - 1)]
        if new_pair[0] not in random4:
            random4.append(new_pair)

    pair = random4[randint(0, 3)]

    english_word = pair[0]
    
    keyboard = ReplyKeyboardMarkup(row_width=2)
    button1 = telebot.types.KeyboardButton(random4[0][1])
    button2 = telebot.types.KeyboardButton(random4[1][1])
    button3 = telebot.types.KeyboardButton(random4[2][1])
    button4 = telebot.types.KeyboardButton(random4[3][1])
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Выбери перевод слова \n{english_word}",
        reply_markup=keyboard
    )

@bot.message_handler(commands=["start"])
def handle_start(message: Message):
    print("Получена команда /start")
    username = message.from_user.full_name if message.from_user.full_name else message.from_user.username
    text = f"""Привет {username}! 👋 

Я бот для изучения английских слов, версия 0.6.0.

Давай попрактикуемся в английском языке. Можешь отвечать в удобном для себя темпе.

Ну что, начнём? ⬇️
"""
    bot.send_message(message.chat.id, text)

    send_word(message)


@bot.message_handler()
def handle_message(message: Message):
    ...


def print_info(message):
    info = f"""Вы написали: `{message.text}`
Пользователь: `{message.from_user.username}`
Чат: `{message.chat.id}`
"""
    print(info)
    bot.send_message(message.chat.id, info, parse_mode="Markdown")


bot.infinity_polling()


