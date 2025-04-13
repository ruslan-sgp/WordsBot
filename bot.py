# @PyBotWords_Bot


import telebot
from telebot.types import Message
from os import getenv
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup
from random import randint, sample


load_dotenv()
bot_token = getenv("TOKEN")
print("Using token ...", bot_token[-5:])


bot = telebot.TeleBot(bot_token)

words_dict = {
    "apple": "яблоко",
    "book": "книга",
    "cat": "кот",
    "dog": "собака",
    "egg": "яйцо",
    "fish": "рыба",
    "house": "дом",
    "tree": "дерево",
    "sun": "солнце",
    "moon": "луна",
    "car": "машина",
    "pen": "ручка",
    "chair": "стул",
    "water": "вода",
    "milk": "молоко",
    "bird": "птица",
    "table": "стол",
    "ball": "мяч",
    "hand": "рука",
    "window": "окно",
}

words_dict = {
    "EC00001": {
        "eng": "Picture",
        "ru": "Представить",
        "ex": "Picture a bustling marketplace.",
    },
    "EC00002": {
        "eng": "Bustling",
        "ru": "Оживлённый",
        "ex": "A bustling marketplace is full of activity.",
    },
    "EC00003": {
        "eng": "Marketplace",
        "ru": "Рынок",
        "ex": "Traders and buyers meet at the marketplace.",
    },
    "EC00004": {
        "eng": "Traders",
        "ru": "Торговцы",
        "ex": "Traders shout out prices to attract buyers.",
    },
    "EC00005": {
        "eng": "Shouting",
        "ru": "Кричать",
        "ex": "Traders are shouting to sell their goods.",
    },
    "EC00006": {
        "eng": "Prices",
        "ru": "Цены",
        "ex": "Buyers check prices before making a deal.",
    },
    "EC00007": {
        "eng": "Buyers",
        "ru": "Покупатели",
        "ex": "Buyers haggle for the best deals.",
    },
    "EC00008": {
        "eng": "Haggling",
        "ru": "Торговаться",
        "ex": "Buyers are haggling over the price of sneakers.",
    },
    "EC00009": {"eng": "Deals", "ru": "Сделки", "ex": "Good deals save money."},
    "EC00010": {
        "eng": "Imagine",
        "ru": "Вообразить",
        "ex": "Imagine the economy as a global marketplace.",
    },
    "EC00011": {
        "eng": "Expanding",
        "ru": "Расширяться",
        "ex": "The marketplace is expanding to include the world.",
    },
    "EC00012": {
        "eng": "Encompass",
        "ru": "Охватывать",
        "ex": "The economy encompasses all trades and businesses.",
    },
    "EC00013": {
        "eng": "Entire",
        "ru": "Весь",
        "ex": "The entire world is part of the global economy.",
    },
    "EC00014": {
        "eng": "World",
        "ru": "Мир",
        "ex": "The world economy connects everyone.",
    },
    "EC00015": {
        "eng": "Economy",
        "ru": "Экономика",
        "ex": "The economy is the system of trade and money.",
    },
    "EC00016": {
        "eng": "Simplest",
        "ru": "Простейший",
        "ex": "The simplest form of economics is buying and selling.",
    },
    "EC00017": {
        "eng": "Form",
        "ru": "Форма",
        "ex": "Economics takes the form of supply and demand.",
    },
    "EC00018": {
        "eng": "Ever-changing",
        "ru": "Постоянно меняющийся",
        "ex": "The ever-changing economy affects jobs and prices.",
    },
    "EC00019": {
        "eng": "Dynamic",
        "ru": "Динамичный",
        "ex": "A dynamic system adapts to changes.",
    },
    "EC00020": {
        "eng": "System",
        "ru": "Система",
        "ex": "The economic system helps allocate resources.",
    },
    "EC00021": {
        "eng": "Saving",
        "ru": "Экономия",
        "ex": "Saving money is important for your future.",
    },
    "EC00022": {
        "eng": "Allowance",
        "ru": "Карманные деньги",
        "ex": "Your allowance helps you learn about saving.",
    },
    "EC00023": {
        "eng": "Spending",
        "ru": "Трата",
        "ex": "Spending too much can lead to debt.",
    },
    "EC00024": {
        "eng": "Mall",
        "ru": "Торговый центр",
        "ex": "People spend money at the mall.",
    },
    "EC00025": {
        "eng": "Planning",
        "ru": "Планирование",
        "ex": "Planning helps you make smart financial decisions.",
    },
    "EC00026": {
        "eng": "Invest",
        "ru": "Инвестировать",
        "ex": "You can invest in stocks for the future.",
    },
    "EC00027": {
        "eng": "Stocks",
        "ru": "Акции",
        "ex": "Stocks are a way to grow your money.",
    },
    "EC00028": {
        "eng": "Future",
        "ru": "Будущее",
        "ex": "Investing is about planning for the future.",
    },
    "EC00029": {
        "eng": "Fundamental",
        "ru": "Фундаментальный",
        "ex": "Fundamental concepts help you understand economics.",
    },
    "EC00030": {
        "eng": "Concepts",
        "ru": "Концепции",
        "ex": "Economic concepts like supply and demand are key.",
    },
    "EC00031": {
        "eng": "Economics",
        "ru": "Экономика",
        "ex": "Economics studies how people use resources.",
    },
    "EC00032": {
        "eng": "Decipher",
        "ru": "Расшифровывать",
        "ex": "You need to decipher financial news to stay informed.",
    },
    "EC00033": {
        "eng": "Financial",
        "ru": "Финансовый",
        "ex": "Financial decisions affect your life.",
    },
    "EC00034": {
        "eng": "News",
        "ru": "Новости",
        "ex": "Financial news explains market trends.",
    },
    "EC00035": {
        "eng": "Informed",
        "ru": "Осведомлённый",
        "ex": "Being informed helps you make better choices.",
    },
    "EC00036": {
        "eng": "Decisions",
        "ru": "Решения",
        "ex": "Smart decisions shape your financial future.",
    },
    "EC00037": {
        "eng": "Shape",
        "ru": "Формировать",
        "ex": "Your choices shape your future.",
    },
    "EC00038": {
        "eng": "Participant",
        "ru": "Участник",
        "ex": "Everyone is a participant in the economy.",
    },
    "EC00039": {
        "eng": "Journey",
        "ru": "Путешествие",
        "ex": "Learning economics is a journey.",
    },
    "EC00040": {
        "eng": "Understanding",
        "ru": "Понимание",
        "ex": "Understanding economics helps you make sense of the world.",
    },
    "EC00041": {
        "eng": "Resources",
        "ru": "Ресурсы",
        "ex": "Resources are things we use to produce goods.",
    },
    "EC00042": {
        "eng": "Companies",
        "ru": "Компании",
        "ex": "Companies decide what to produce.",
    },
    "EC00043": {
        "eng": "Governments",
        "ru": "Правительства",
        "ex": "Governments regulate the economy.",
    },
    "EC00044": {
        "eng": "Value",
        "ru": "Ценность",
        "ex": "Money has value because we use it to buy things.",
    },
    "EC00045": {
        "eng": "Supply",
        "ru": "Предложение",
        "ex": "High supply lowers prices.",
    },
    "EC00046": {"eng": "Demand", "ru": "Спрос", "ex": "High demand raises prices."},
    "EC00047": {"eng": "Market", "ru": "Рынок", "ex": "The market determines prices."},
    "EC00048": {
        "eng": "Determines",
        "ru": "Определяет",
        "ex": "Supply and demand determine prices.",
    },
    "EC00049": {
        "eng": "Phone",
        "ru": "Телефон",
        "ex": "A new phone might be expensive if demand is high.",
    },
    "EC00050": {
        "eng": "Available",
        "ru": "Доступный",
        "ex": "If few phones are available, prices rise.",
    },
    "EC00051": {
        "eng": "Increase",
        "ru": "Увеличивать",
        "ex": "Prices increase when demand is high.",
    },
    "EC00052": {
        "eng": "Fluctuate",
        "ru": "Колебаться",
        "ex": "Prices fluctuate based on supply and demand.",
    },
    "EC00053": {
        "eng": "Boom",
        "ru": "Подъём",
        "ex": "A boom means the economy is doing well.",
    },
    "EC00054": {
        "eng": "Bust",
        "ru": "Спад",
        "ex": "A bust means the economy is struggling.",
    },
    "EC00055": {
        "eng": "Affect",
        "ru": "Влиять",
        "ex": "Economic changes affect jobs and wages.",
    },
    "EC00056": {
        "eng": "Jobs",
        "ru": "Работа",
        "ex": "More jobs mean a stronger economy.",
    },
    "EC00057": {
        "eng": "Cost",
        "ru": "Стоимость",
        "ex": "The cost of sneakers depends on demand.",
    },
    "EC00058": {
        "eng": "Sneakers",
        "ru": "Кроссовки",
        "ex": "Sneakers are an example of a product affected by supply and demand.",
    },
    "EC00059": {
        "eng": "Money",
        "ru": "Деньги",
        "ex": "Money is used to buy goods and services.",
    },
    "EC00060": {
        "eng": "Medium",
        "ru": "Средство",
        "ex": "Money is a medium of exchange.",
    },
    "EC00061": {
        "eng": "Exchange",
        "ru": "Обмен",
        "ex": "Barter is an old form of exchange.",
    },
    "EC00062": {
        "eng": "Barter",
        "ru": "Бартер",
        "ex": "People used to barter goods instead of using money.",
    },
    "EC00063": {
        "eng": "Swap",
        "ru": "Обмен",
        "ex": "You can swap one item for another.",
    },
    "EC00064": {
        "eng": "Goods",
        "ru": "Товары",
        "ex": "Goods are things we buy, like food or clothes.",
    },
    "EC00065": {
        "eng": "Services",
        "ru": "Услуги",
        "ex": "Services include things like haircuts or repairs.",
    },
    "EC00066": {"eng": "Banks", "ru": "Банки", "ex": "Banks keep your money safe."},
    "EC00067": {
        "eng": "Safeguard",
        "ru": "Защищать",
        "ex": "Banks safeguard your savings.",
    },
    "EC00068": {
        "eng": "Deposit",
        "ru": "Депозит",
        "ex": "You deposit money into a bank account.",
    },
    "EC00069": {
        "eng": "Lend",
        "ru": "Давать в долг",
        "ex": "Banks lend money to businesses.",
    },
    "EC00070": {
        "eng": "Businesses",
        "ru": "Бизнес",
        "ex": "Businesses borrow money to grow.",
    },
    "EC00071": {
        "eng": "Individuals",
        "ru": "Частные лица",
        "ex": "Individuals save money in banks.",
    },
    "EC00072": {
        "eng": "Charge",
        "ru": "Взимать",
        "ex": "Banks charge interest on loans.",
    },
    "EC00073": {
        "eng": "Interest",
        "ru": "Процент",
        "ex": "Interest is the cost of borrowing money.",
    },
    "EC00074": {
        "eng": "Loans",
        "ru": "Кредиты",
        "ex": "Loans help people buy houses or cars.",
    },
    "EC00075": {
        "eng": "Profit",
        "ru": "Прибыль",
        "ex": "Banks make a profit by charging interest.",
    },
    "EC00076": {
        "eng": "Regulating",
        "ru": "Регулирование",
        "ex": "Banks regulate the amount of money in the economy.",
    },
    "EC00077": {
        "eng": "Circulating",
        "ru": "Обращение",
        "ex": "Too much money circulating causes inflation.",
    },
    "EC00078": {
        "eng": "Inflation",
        "ru": "Инфляция",
        "ex": "Inflation makes prices rise.",
    },
    "EC00079": {
        "eng": "Trade",
        "ru": "Торговля",
        "ex": "Trade happens when countries buy and sell goods.",
    },
    "EC00080": {"eng": "Buy", "ru": "Покупать", "ex": "You buy goods at the store."},
    "EC00081": {
        "eng": "Sell",
        "ru": "Продавать",
        "ex": "Companies sell products to consumers.",
    },
    "EC00082": {
        "eng": "Exchange Rates",
        "ru": "Обменные курсы",
        "ex": "Exchange rates show how much one currency is worth.",
    },
    "EC00083": {
        "eng": "Currency",
        "ru": "Валюта",
        "ex": "Different countries have different currencies.",
    },
    "EC00084": {
        "eng": "Worth",
        "ru": "Стоимость",
        "ex": "How much is this currency worth?",
    },
    "EC00085": {
        "eng": "Travel",
        "ru": "Путешествие",
        "ex": "Travel abroad requires exchanging currency.",
    },
    "EC00086": {
        "eng": "Abroad",
        "ru": "За границей",
        "ex": "You need money to travel abroad.",
    },
    "EC00087": {
        "eng": "Purchasing Power",
        "ru": "Покупательная способность",
        "ex": "Inflation decreases your purchasing power.",
    },
    "EC00088": {
        "eng": "Decrease",
        "ru": "Уменьшение",
        "ex": "Prices can decrease during a bust.",
    },
    "EC00089": {
        "eng": "Central Bank",
        "ru": "Центральный банк",
        "ex": "The central bank controls the money supply.",
    },
    "EC00090": {
        "eng": "Savings Account",
        "ru": "Сберегательный счёт",
        "ex": "A savings account helps you save money.",
    },
    "EC00091": {
        "eng": "Borrowing",
        "ru": "Заимствование",
        "ex": "Borrowing money costs interest.",
    },
    "EC00092": {
        "eng": "Impact",
        "ru": "Влияние",
        "ex": "Economic policies impact daily life.",
    },
    "EC00093": {
        "eng": "Economic Climate",
        "ru": "Экономический климат",
        "ex": "The economic climate affects spending and saving.",
    },
    "EC00094": {
        "eng": "Recessions",
        "ru": "Рецессии",
        "ex": "Recessions are periods of economic decline.",
    },
    "EC00095": {
        "eng": "Budget",
        "ru": "Бюджет",
        "ex": "A budget helps you plan your spending.",
    },
    "EC00096": {
        "eng": "Wisely",
        "ru": "Мудро",
        "ex": "Invest wisely to secure your financial future.",
    },
}

word_codes = list(words_dict.keys())

user_sessions = {}


def send_word(message: Message):
    random4 = sample(word_codes, 4)
    # while len(random4) < 4:
    #     index = randint(0, len(word_codes) - 1)
    #     new_pair = words_dict[inde]
    #     if new_pair[0] not in random4:
    #         random4.append(new_pair)

    # pair = random4[randint(0, 3)]

    # english_word = pair[0]
    # russian_word = pair[1]

    code = random4[randint(0, 3)]
    words_data = words_dict[code]
    english_word = words_data["eng"]
    russian_word = words_data["ru"]
    usage_example = words_data["ex"]

    keyboard = ReplyKeyboardMarkup(row_width=2)
    button1 = telebot.types.KeyboardButton(words_dict[random4[0]]["ru"])
    button2 = telebot.types.KeyboardButton(words_dict[random4[1]]["ru"])
    button3 = telebot.types.KeyboardButton(words_dict[random4[2]]["ru"])
    button4 = telebot.types.KeyboardButton(words_dict[random4[3]]["ru"])
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Выбери перевод слова \n\n**{english_word.upper()}**\n\nПример использования:\n\n{usage_example}",
        reply_markup=keyboard,
    )

    user_sessions[message.from_user.id] = russian_word


@bot.message_handler(commands=["start"])
def handle_start(message: Message):
    print(
        f"Получена команда /start от пользователя {message.from_user.id} {message.from_user.username} {message.from_user.first_name} {message.from_user.last_name}"
    )
    username = (
        message.from_user.full_name
        if message.from_user.full_name
        else message.from_user.username
    )
    text = f"""Привет {username}! 👋 

Я бот для изучения английских слов, версия 0.6.0.

Давай попрактикуемся в английском языке. Можешь отвечать в удобном для себя темпе.

Ну что, начнём? ⬇️
"""
    bot.send_message(message.chat.id, text)

    send_word(message)


@bot.message_handler()
def handle_message(message: Message):
    print(
        f"Получено сообщение от пользователя {message.from_user.id} {message.from_user.username} {message.from_user.first_name} {message.from_user.last_name}"
    )
    print(message.text)
    word = message.text
    correct_word = user_sessions[message.from_user.id]
    if word == correct_word:
        text = "Верно! Переходим к следующему слову"
        bot.send_message(message.chat.id, text)
        send_word(message)
    else:
        text = f"Неправильно! Попробуйте еще раз"
        bot.send_message(message.chat.id, text)


def print_info(message):
    info = f"""Вы написали: `{message.text}`
Пользователь: `{message.from_user.username}`
Чат: `{message.chat.id}`
"""
    print(info)
    bot.send_message(message.chat.id, info, parse_mode="Markdown")


bot.infinity_polling()
