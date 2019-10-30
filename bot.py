import telebot
import PIL
import tempfile
import os

bot = telebot.TeleBot('930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s')

log = open("output.log","a")
log.write("test")
log.close()

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from telebot import types

markup = types.ReplyKeyboardMarkup(True)


telo = ''
vkanal = ''
pkanal = 100

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
    global pkanal

    if message.text.lower() == 'новости':
        if pkanal == 1 or pkanal == 10:
            pkanal = 10
            telo = vkanal + '\n' + '<a href="https://t.me/sgk_proba">#Новости</a>'
        else:
            telo = telo + '\n' + '<a href="https://t.me/sgk_proba">#Новости</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.text.lower() == 'дача':
        if pkanal == 1 or pkanal == 10:
            pkanal = 10
            telo = vkanal + '\n' + '<a href="https://t.me/sgk_proba">#Дача</a>'
        else:
            telo = telo + '\n' + '<a href="https://t.me/sgk_proba">#Дача</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.text.lower() == 'отправить':
        telo = vkanal
        bot.send_message('@SGK_proba', telo, parse_mode='html', disable_web_page_preview=True)
        bot.delete_message(message.chat.id, message.message_id)
        telo = ''
    elif message.text.lower() == 'прогресс':
        if pkanal == 1 or pkanal == 10:
            pkanal = 10
            telo = vkanal + '\n' + '<a href="https://t.me/sgk_proba">#Прогресс</a>'
        else:
            telo = telo + '\n' + '<a href="https://t.me/sgk_proba">#Прогресс</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.entities:
             for item in message.entities:
                if item.type == "url":
                    if telo == '':
                       telo = vkanal + '<a href="' + message.text + '">Читать далее...</a>'
                    else:
                       telo = telo + '<a href="' + message.text + '">Читать далее...</a>'
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
                vkanal = telo + '\n'
                telo = ''
                pkanal = 1
    elif message.text.lower() == 'объединить':
        telo = telo +'<a href="https://t.me/sgk_proba">Этого пункта скорее всего не будет</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.text.lower() == 'мнение':
        if pkanal == 1 or pkanal == 10:
            pkanal = 10
            telo = vkanal + '\n' + '<a href="https://t.me/sgk_proba">#Мнение</a>'
        else:
            telo = telo + '\n' + '<a href="https://t.me/sgk_proba">#Мнение</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.text.lower() == 'юмор':
        #  bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
        if pkanal == 1 or pkanal == 10:
            pkanal = 10
            telo = vkanal + '\n' + '<a href="https://t.me/sgk_proba">#Юмор</a>'
        else:
            telo = telo + '\n' + '<a href="https://t.me/sgk_proba">#Юмор</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    telo = message.text + '\n'
    # vkanal = telo



@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    f = tempfile.NamedTemporaryFile(delete=False)

    file_info = bot.get_file(message.photo[-1].file_id)

    f.write(bot.download_file(file_info.file_path))
    f.close()

    photo = Image.open(f.name)

    drawing = ImageDraw.Draw(photo)

    black = (240, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 16)
    pos = (40, 290)
    text = 'Телеграм @SGK_espace'

    drawing.text(pos, text, fill=black, font=font)
    photo_path = f'{f.name}.jpeg'
    photo.save(photo_path, 'JPEG', dpi=[800,600], quality=100)

    with open(photo_path, 'rb') as fi:
        bot.send_photo(message.chat.id, fi)

    os.remove(f.name)
    os.remove(photo_path)



bot.polling()
