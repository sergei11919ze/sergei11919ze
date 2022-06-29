import telebot
import requests
from telebot import types


URL = 'https://cdn.cur.su/api/cbr.json'

response = requests.get(URL)

res = response.json()


bot = telebot.TeleBot('5523966143:AAFIlOX_x-RxyJkMajZjnJ9MxXDrd382vJ4') #вставить токен

@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=2)
    item = types.KeyboardButton('JPY')
    item2 = types.KeyboardButton('EUR')
    item3 = types.KeyboardButton('USD')
    item4 = types.KeyboardButton('CNY')

    markup_reply.add(item, item2, item3, item4)
    bot.send_message(message.chat.id, 'Вся информация взята с официального сайта ЦБ.\nВыбирете валюту', reply_markup=markup_reply)

@bot.message_handler()
def get_user_text(message):

    for y in res['rates']:
        if message.text == y:
            mess = 1/res['rates'][y]
            mess = str(mess*res['rates']['RUB']) + ' RUB' 
            bot.send_message(message.chat.id, mess, parse_mode='html')
    


bot.polling(none_stop=True)  #постоянная работа