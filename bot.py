import telebot
import PIL
import tempfile
import os
import youtube_dl

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

itembtnNews = types.KeyboardButton('News')
itembtnIt = types.KeyboardButton('IT News')
itembtnBla = types.KeyboardButton('Sight')
itembtnDa = types.KeyboardButton('Hands')
itembtnKomb = types.KeyboardButton('Comb')
itembtndHum = types.KeyboardButton('Humor')
itembtnSend = types.KeyboardButton('Send')
itembtnRead = types.KeyboardButton('Help')

markup.row(itembtnNews, itembtnIt, itembtnDa, itembtnKomb)
markup.row(itembtndHum, itembtnBla, itembtnRead, itembtnSend)

HS='Здравствуйте. ' \
   ' Оговорюсь сразу - бот создавался исключительно для помощи в продвижении моего канала.' \
   ' Простота накладывает ограничения - вы всегда работаете только с последним отправленным боту сообщением.' \
   ' Настроить расположение водяного знака нельзя. Любая отправленная ссылка (кроме на ютуб) формирует “Читать далее”.' \
   ' Ссылка на ютуб скачивает видео. Отправленная картинка возвращается с водяным знаком. ' \
   '\n' \
   '<a href="https://t.me/SGK_espace">Подписаться на мой канал</a>'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, HS,parse_mode='html', disable_web_page_preview=True)

@bot.message_handler(content_types=['text'])
def send_text(message):
    global telo
    global vkanal
    global pkanal

    if message.text.lower() == 'news':
        if pkanal == 1 or pkanal == 10:
            pkanal = 10
            telo = vkanal + '\n' + '<a href="https://t.me/SGK_espace">#Новости</a>'
        else:
            telo = telo + '\n' + '<a href="https://t.me/SGK_espace">#Новости</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.text.lower() == 'hands':
        if pkanal == 1 or pkanal == 10:
            pkanal = 10
            telo = vkanal + '\n' + '<a href="https://t.me/sgk_proba">#Hands</a>'
        else:
            telo = telo + '\n' + '<a href="https://t.me/sgk_proba">#Hands</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.text.lower() == 'send':
        telo = vkanal
        bot.send_message('@SGK_proba', telo, parse_mode='html', disable_web_page_preview=True)
        bot.delete_message(message.chat.id, message.message_id)
        telo = ''
    elif message.text.lower() == 'it news':
        if pkanal == 1 or pkanal == 10:
            pkanal = 10
            telo = vkanal + '\n' + '<a href="https://t.me/sgk_proba">#NewsIT</a>'
        else:
            telo = telo + '\n' + '<a href="https://t.me/sgk_proba">#NewsIT</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''

    elif message.entities:
             for item in message.entities:
                if item.type == "url":
                    if 'youtube.com' in message.text: #  Загружаем с Ютуб

                        ydl_opts = {'outtmpl': '/tmp/f.mp3', 'preferredcodec': 'mp3'}
                        link_of_the_video = message.text

                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([link_of_the_video])

                        bot.delete_message(message.chat.id, message.message_id)
                        video = open('/tmp/f.mp3', 'rb')
                        bot.send_video(message.chat.id, video)
                        #  bot.send_video(chat_id, "FILEID")
                        os.remove('/tmp/f.mp3')


                    else:  # Читать далее
                      if telo == '':
                         telo = vkanal + '<a href="' + message.text + '">Читать далее...</a>'
                      else:
                         telo = telo + '<a href="' + message.text + '">Читать далее...</a>'

                      bot.delete_message(message.chat.id, message.message_id)
                      bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
                      vkanal = telo + '\n'
                      telo = ''
                      pkanal = 1

    elif message.text.lower() == 'comb':
        telo = telo +'<a href="https://t.me/sgk_proba">Этого пункта скорее всего не будет</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.text.lower() == 'sight':
        if pkanal == 1 or pkanal == 10:
            pkanal = 10
            telo = vkanal + '\n' + '<a href="https://t.me/sgk_proba">#Мнение</a>'
        else:
            telo = telo + '\n' + '<a href="https://t.me/sgk_proba">#Мнение</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
    elif message.text.lower() == 'humor':
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
    width, height = photo.size

    drawing = ImageDraw.Draw(photo)

    black = (240, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", width//20)
    pos = (width//3, height - height//10)
    text = 'Телеграм @SGK_espace'

    drawing.text(pos, text, fill=black, font=font)
    pos = (1 + width // 3, 1 + height - height // 10)
    drawing.text(pos, text, fill=black, font=font)
    pos = (2 + width // 3, 2 + height - height // 10)
    drawing.text(pos, text, fill=black, font=font)

    photo_path = f'{f.name}.jpeg'
    photo.save(photo_path, 'JPEG')

    with open(photo_path, 'rb') as fi:
        bot.send_photo(message.chat.id, fi)

    os.remove(f.name)
    os.remove(photo_path)



bot.polling()
