import telebot;                                                            
bot = telebot.TeleBot('930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s'); 
from telebot import types                                                  

markup = types.ReplyKeyboardMarkup(True, True)

itembtnNews = types.KeyboardButton('Новости')
itembtnDa = types.KeyboardButton('Дача')
itembtnСomb = types.KeyboardButton('Объединить')
itembtndAmour = types.KeyboardButton('Я тебя люблю') #  Юмор
itembtnSend = types.KeyboardButton('Send')
itembtnRead = types.KeyboardButton('Читать далее...')
itembtnIt = types.KeyboardButton('#IT')
itembtnBla = types.KeyboardButton('#Мои рассуждения')


markup.row(itembtnNews, itembtnIt, itembtnDa, itembtnСomb)
markup.row(itembtndAmour, itembtnBla, itembtnRead, itembtnSend)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Новости':
        bot.send_message(message.chat.id, 'Привет, мой создатель, давно пургу не копипастил')
    elif message.text.lower() == 'Дача':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'Send':
        bot.send_sticker(message.chat.id, '#Проба(https://t.me/sgk_proba)')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
