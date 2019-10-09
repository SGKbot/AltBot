import telebot
bot = telebot.TeleBot('930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s')
from telebot import types                                                  

markup = types.ReplyKeyboardMarkup(True)

itembtnNews = types.KeyboardButton('Новости')
itembtnIt = types.KeyboardButton('Прогресс')
itembtnBla = types.KeyboardButton('Мнение')
itembtnDa = types.KeyboardButton('Дача')
itembtnComb = types.KeyboardButton('Объединить')
itembtndHum = types.KeyboardButton('Юмор')
itembtnSend = types.KeyboardButton('Отправить')
itembtnRead = types.KeyboardButton('Далее...')

markup.row(itembtnNews, itembtnIt, itembtnDa, itembtnComb)
markup.row(itembtndHum, itembtnBla, itembtnRead, itembtnSend)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup)
    print(message_id)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Новости':
        bot.send_message(message.chat.id, 'Привет, мой создатель, давно пургу не копипастил')
    elif message.text.lower() == 'Дача':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'Отправить':
        bot.send_message(message.chat.id, '#Проба(https://t.me/sgk_proba)')
    elif message.text.lower() == 'Прогресс':
        bot.send_message(message.chat.id, '#Проба(https://t.me/sgk_proba)')
    elif message.text.lower() == 'Далее...':
        bot.send_message(message.chat.id, '#Проба(https://t.me/sgk_proba)')
    elif message.text.lower() == 'Объединить':
        bot.send_message(message.chat.id, '#Проба(https://t.me/sgk_proba)')
    elif message.text.lower() == 'Мнение':
        bot.send_message(message.chat.id, '#Проба(https://t.me/sgk_proba)')
    elif message.text.lower() == 'Юмор':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
