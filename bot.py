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
    global vkanal
    if message.text.lower() == 'новости':
        #  bot.send_message(message.chat.id, 'Привет, мой создатель, давно пургу не копипастил')
        telo = telo +'<a href="https://t.me/sgk_proba">#Новости</a>'
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        telo = ''
    elif message.text.lower() == 'дача':
        #  bot.send_message(message.chat.id, 'Прощай, создатель')
        telo = telo +'<a href="https://t.me/sgk_proba">#Дача</a>'
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.text.lower() == 'отправить':
        telo = vkanal
        bot.send_message('@SGK_proba', telo, parse_mode='html', disable_web_page_preview=True)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        # bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)

        telo = ''
    elif message.text.lower() == 'прогресс':
        telo = telo +'<a href="https://t.me/sgk_proba">#Прогресс</a>'
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        telo = ''
    elif message.entities:
             for item in message entities:
                if item.type == "url":
                     telo = telo + '\n' + '<a href="' + message.text + '">#Читать далее...</a>'
                     bot.delete_message(message.chat.id, message.message_id - 1)
                     bot.delete_message(message.chat.id, message.message_id)
                     bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
                     telo = ''
                     do_something()
    elif message.text.lower() == 'объединить':
        # bot.send_message(message.chat.id, message.message_id)
        telo = telo +'<a href="https://t.me/sgk_proba">Этого пункта скорее всего не будет</a>'
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        telo = ''
    elif message.text.lower() == 'мнение':
        # bot.send_message(message.chat.id, 'кому оно интересно')
        telo = telo +'<a href="https://t.me/sgk_proba">#Мнение</a>'
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        telo = ''
    elif message.text.lower() == 'юмор':
        #  bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
        telo = telo +'<a href="https://t.me/sgk_proba">#Юмор</a>'
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        telo = ''
    telo = message.text + '\n'

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
