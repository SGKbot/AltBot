import telebot

bot = telebot.TeleBot('930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s')
from telebot import types
#  disable_web_page_preview
markup = types.ReplyKeyboardMarkup(True)


telo = ''

itembtnNews = types.KeyboardButton('Новости')
itembtnIt = types.KeyboardButton('Прогресс')
itembtnBla = types.KeyboardButton('Мнение')
itembtnDa = types.KeyboardButton('Дача')
itembtnKomb = types.KeyboardButton('Объединить')
itembtndHum = types.KeyboardButton('Юмор')
itembtnSend = types.KeyboardButton('Отправить')
itembtnRead = types.KeyboardButton('Далее...')

markup.row(itembtnNews, itembtnIt, itembtnDa, itembtnKomb)
markup.row(itembtndHum, itembtnBla, itembtnRead, itembtnSend)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup)

@bot.message_handler(content_types=['text'])

def send_text(message):
    global telo
    if message.text.lower() == 'новости':
        bot.send_message(message.chat.id, 'Привет, мой создатель, давно пургу не копипастил')
    elif message.text.lower() == 'дача':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'отправить':
        bot.send_message(message.chat.id, '#Проба(https://t.me/sgk_proba)')
    elif message.text.lower() == 'прогресс':
        bot.delete_message(message.chat.id, message.message_id - 1)
        telo = telo + message.text
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo)
    elif message.text.lower() == 'далее...':
        bot.delete_message(message.chat.id, message.message_id - 2)
    elif message.text.lower() == 'объединить':
        bot.send_message(message.chat.id, message.message_id)
    elif message.text.lower() == 'мнение':
        bot.send_message(message.chat.id, 'кому оно интересно')
    elif message.text.lower() == 'юмор':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text:
        telo = message.text + '\n'

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
