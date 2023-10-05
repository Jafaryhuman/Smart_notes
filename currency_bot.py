import telebot
import requests

TOKEN = ''#свой токен
api_key = 'aadb12a34d5d4ea3898f7222030381b2'

bot = telebot.TeleBot(TOKEN)

def usd_to_uzs(chat_id):
    url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        currency_rate = data['rates']['UZS']
        currency_rate1 = data['rates']['RUB']
        rub_to_uzs = currency_rate/currency_rate1
        message = (f'1 dollar = {round(currency_rate, 2)} sums\n1 ruble = {round(rub_to_uzs, 2)} sums')

        bot.send_message(chat_id, message)
    else:
        bot.send_message(chat_id, 'Sorry, no data available. Try again later')

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    usd_to_uzs(chat_id)

bot.polling()
