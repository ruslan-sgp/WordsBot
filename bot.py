import telebot
from telebot.types import Message
from os import getenv
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup
from random import randint, sample
import dict_general
import dict_econ
import dict_pdb
from UserSessions import (
    load_session,
    save_sessions,
    selected_dict,
    words_dict,
)

load_dotenv()
bot_token = getenv("TOKEN")
print("Using token ...", bot_token[-5:])


dict_list = {
    "English General": ("/dict_eng", dict_general.words_dict),
    "English Economics": ("/dict_enec", dict_econ.words_dict),
    "Python Databases": ("/dict_pdb", dict_pdb.words_dict),
}


def dict_info():
    info_list = []
    for name in dict_list:
        command, dict = dict_list[name]
        sel_icon = "✅" if selected_dict() == command else "☑️"
        info_list.append(f"{sel_icon} {command} - {name} ({len(dict)} слов)")
    return "\n".join(info_list)


def load_dict(command):
    print("Загрузка словаря", command)
    name, dict = next(
        ((k, d) for k, (cmd, d) in dict_list.items() if cmd == command), None
    )
    load_session()["words_dict"] = dict
    print(f"Загружен словарь {dict[next(iter(dict))]} ...")
    return name


bot = telebot.TeleBot(bot_token)


def send_word(message: Message):
    session = load_session()
    if not session.get("words_dict"):
        sd = selected_dict()
        load_dict(sd)
    dict = words_dict()
    random4 = sample(list(dict.keys()), 4)
    # random4 = []
    # word_codes = words_dict.keys()
    # while len(random4) < 4:
    #     index = randint(0, len(word_codes) - 1)
    #     new_pair = words_dict[inde]
    #     if new_pair[0] not in random4:
    #         random4.append(new_pair)

    # pair = random4[randint(0, 3)]

    # english_word = pair[0]
    # russian_word = pair[1]

    code = random4[randint(0, 3)]
    words_data = dict[code]
    english_word = words_data["eng"]
    russian_word = words_data["ru"]
    usage_example = words_data["ex"]

    keyboard = ReplyKeyboardMarkup(row_width=2)
    button1 = telebot.types.KeyboardButton(dict[random4[0]]["ru"])
    button2 = telebot.types.KeyboardButton(dict[random4[1]]["ru"])
    button3 = telebot.types.KeyboardButton(dict[random4[2]]["ru"])
    button4 = telebot.types.KeyboardButton(dict[random4[3]]["ru"])
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Выбери перевод слова:\n\n**{english_word.upper()}**\n\nПример использования:\n\n{usage_example}",
        reply_markup=keyboard,
        parse_mode="Markdown",
    )

    load_session()["correct_word"] = russian_word
    save_sessions()


@bot.message_handler(commands=["start"])
def handle_start(message: Message):
    print(
        f"Получена команда /start от пользователя {message.from_user.id} {message.from_user.username} {message.from_user.first_name} {message.from_user.last_name}"
    )

    session = load_session(message.from_user.id)
    load_dict(session["selected_dict"])

    username = (
        message.from_user.full_name
        if message.from_user.full_name
        else message.from_user.username
    )
    text = f"""Привет {username}! 👋 

Я бот для изучения слов. Вот доступные словари:

{dict_info()}

Начнём тренировку? ⬇️
"""
    bot.send_message(message.chat.id, text)

    send_word(message)


@bot.message_handler()
def handle_message(message: Message):
    print(
        f"Получено сообщение от пользователя {message.from_user.id} {message.from_user.username} {message.from_user.first_name} {message.from_user.last_name}"
    )
    print(message.text)
    session = load_session(message.from_user.id)

    if message.text and message.text.startswith("/"):
        handle_command(message)
    else:
        word = message.text
        correct_word = session["correct_word"]
        if word == correct_word:
            text = "Верно! Переходим к следующему слову"
            bot.send_message(message.chat.id, text)
            send_word(message)
        else:
            text = f"Неправильно! Попробуйте еще раз"
            bot.send_message(message.chat.id, text)


def handle_command(message: Message):
    command = message.text
    if command.startswith("/dict_"):
        name = load_dict(command)
        load_session(message.from_user.id)["selected_dict"] = command
        bot.send_message(message.chat.id, "Загружен словарь " + name)
        send_word(message)
        save_sessions()


def print_info(message):
    info = f"""Вы написали: {message.text}
Пользователь: {message.from_user.username}
Чат: {message.chat.id}
"""
    print(info)
    bot.send_message(message.chat.id, info, parse_mode="Markdown")


bot.infinity_polling()

save_sessions()
