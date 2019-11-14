import telebot
import PIL
import tempfile
import os
import youtube_dl
import yaml

#  config_file = open("config.yaml","r")
#  config = yaml.load(config_file)
#  value = config.get("key")


bot = telebot.TeleBot('930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s')


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from telebot import types

markup = types.ReplyKeyboardMarkup(True)


telo = ''
vkanal = ''
pkanal = 100
skanal = ''
# skanal = 'https://t.me/sgk_proba'
pv = 0
HSK1 = ''

itembtnNews = types.KeyboardButton('News')
itembtnADS = types.KeyboardButton('ADS')
itembtnBla = types.KeyboardButton('Sight')
itembtnDa = types.KeyboardButton('Hands')
itembtnKomb = types.KeyboardButton('Comb')
itembtndHum = types.KeyboardButton('Humor')
itembtnSend = types.KeyboardButton('Send')
itembtnRead = types.KeyboardButton('Help')

markup.row(itembtnNews, itembtnADS, itembtnDa, itembtnKomb)
markup.row(itembtndHum, itembtnBla, itembtnRead, itembtnSend)

HS = 'Здравствуйте. ' \
    '\n' \
    '\n' \
    ' - Введите имя канала, куда вы будете отправлять сообщения в формате https://t.me/SGK_espace ' \
    '\n' \
    ' - Добавьте бота в Администраторы.' \
    '\n \n' \
    'Ограничения: Простота накладывает ограничения - вы всегда работаете только с последним ВИДИМЫМ В боте сообщением.' \
    ' Настроить расположение водяного знака нельзя. Любая отправленная ссылка (кроме на ютуб) формирует “Читать далее”.' \
    ' Ссылка на ютуб скачивает видео. Отправленная картинка возвращается с водяным знаком. ' \
    'v1.0' \
    '\n' \
    '<a href="https://t.me/SGK_espace">Подписаться на мой канал</a>'

HSK = '\n \n' \
    '<b>       Клавиши:</b>' \
    '\n' \
    '<b>Теги:</b>' \
    '\n' \
    '<b>News</b>      Новости' \
    '\n' \
    '<b>ADS</b>         Реклама' \
    '\n' \
    '<b>Sight</b>       Мнение автора' \
    '\n' \
    '<b>Hands</b>     Дача, своими руками' \
    '\n' \
    '<b>Humor</b>    Юмор' \
    '\n \n' \
    '<b>Действия:</b>' \
    '\n' \
    '<b>Comb</b>    Объединить два последних сообщения' \
    '\n' \
    '<b>Send</b>      Отправить подготовленное сообщение в ваш канал' \
    '\n' \
    '<b>Help</b>       Помощь по боту' \
    '\n \n' \
    '<b>       Действия без клавиш:</b>' \
    '\n' \
    'Отправить боту текст в двойных русских буквах -  <b>бб</b>выделить жирным шрифтом<b>бб</b> .' \
    '\n' \
    '<b>Отправить боту картинку</b> возвращается картинка с указанием на ваш канал.' \
    '\n' \
    '<b>Отправка боту ссылки</b>' \
    '\n' \
    '<b>на ютуб</b> возвращает видеофайл' \
    '\n' \
    '<b>на ваш канал</b> в последующем добавляет в тег гиперссылку на канал,  пишет на картинке, отправленной боту вашу ссылку.' \
    '\n' \
    'Формат https://t.me/SGK_espace' \
    '\n' \
    '<b>любая другая</b> ссылка добавляется к тексту гиперссылкой со словами “Читать далее…"' \
    '\n' \
    'Все вопросы и предложения по работе бота только в чате моего канала.' \
    '\n' \
    '<a href="https://t.me/SGK_espace">Подписаться на мой канал</a>'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, HS,parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
    telo = ''
    vkanal = ''
    pkanal = 100

@bot.message_handler(content_types=['text'])
def send_text(message):

    global telo
    global vkanal
    global pkanal
    global skanal
    global HSK
    global HSK1
    global pv


    if message.text.lower() == 'news':                                            # Новости

        if pkanal == 10:
            telo = vkanal + '\n' + '<a href="' + skanal + '">#Новости</a>'
        else:
            telo = telo + '\n' + '<a href="' + skanal + '">#Новости</a>'

        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)

        vkanal = telo
        telo = ''
        pkanal = 10

    elif message.text.lower() == 'help':                        # Помощь

        if skanal == '' and pv == 0:
            HSK1 = '<b>Не забудьте сделать бота администратором вашего канала и отправить боту ссылку на канал</b>'
            pv = 1
        elif pv == 2:
            HSK1 = '<b>Ваш канал </b>' + skanal
            pv = 3

        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id,HSK1+HSK, parse_mode='html', disable_web_page_preview=True)
        telo = ''
        vkanal = ''
        pkanal = 100

    elif message.text.lower() == 'hands':                               #  Своми руками

        if pkanal == 10:
            telo = vkanal + '\n' + '<a href="' + skanal + '">#Hands</a>'
        else:
            telo = telo + '\n' + '<a href="' + skanal + '">#Hands</a>'

        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
        pkanal = 10

    elif message.text.lower() == 'send':                        #  Отправка в канал
        #  Водяной знак       pkanal = 5
        #  Работа со ссылками pkanal = 6
        if pkanal == 5 or pkanal == 6 or pkanal == 100:
            bot.send_message(message.chat.id, 'Фото, видео и пустые сообщения не отправляются в канал',                             parse_mode='html', disable_web_page_preview=True)
        else:
            chat_id = "@" + skanal[13:]
            if message.from_user.id in [adm_obj.user.id for adm_obj in bot.get_chat_administrators(chat_id)]:
                if pkanal==10:
                   telo = vkanal
                else:
                   telo = telo

                bot.send_message(chat_id, telo, parse_mode='html', disable_web_page_preview=True)
                bot.delete_message(message.chat.id, message.message_id)
                telo = ''
                vkanal = ''
                pkanal = 100
            else:
                bot.send_message(message.chat.id, 'Вы не являетесь Администратором канала', parse_mode='html', disable_web_page_preview=True)


    elif message.text.lower() == 'ads':                     #  Реклама
        if pkanal == 10:
            telo = vkanal + '\n' + '<a href="' + skanal + '">#Реклама</a>'
        else:
            telo = telo + '\n' + '<a href="' + skanal + '">#Реклама</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
        pkanal = 10

    elif message.entities:                                      # Работа со ссылками pkanal = 6
             for item in message.entities:
                if item.type == "url":
                    if 'youtube.com' in message.text or 'youtu.be' in message.text:           #  Загружаем с Ютуб
                        ydl_opts = {'outtmpl': '/tmp/f.mp3', 'preferredcodec': 'mp3', 'max_filesize': 60000000}
                        link_of_the_video = message.text
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([link_of_the_video])
                        bot.delete_message(message.chat.id, message.message_id)

                        if os.path.exists('/tmp/f.mp3'):  # файл есть
                            video = open('/tmp/f.mp3', 'rb')
                            bot.send_video(message.chat.id, video)
                            os.remove('/tmp/f.mp3')
                            pkanal = 6
                        else:       # файла нет
                            bot.send_message(message.chat.id, 'Слишком большой файл', parse_mode='html', disable_web_page_preview=True)
                            telo = ''
                            vkanal = ''
                            pkanal = 100


                    elif 't.me' in message.text:              #  устанавливаем канал пользователя
                        skanal = message.text
                        telo = ''
                        vkanal = ''
                        pkanal = 100
                        bot.delete_message(message.chat.id, message.message_id)
                        bot.send_message(message.chat.id, 'Вы установили свой канал как ' + skanal, parse_mode='html', disable_web_page_preview=True)
                        pv = 2
                        #  chat_id = '@SGK_proba'
                        #  adm_list = [(adm_obj.user.id, adm_obj.user.username) for adm_obj in
                        #            bot.get_chat_administrators(chat_id)]
                        #  bot.send_message(message.chat.id, f'Администраторы {adm_list}\n', parse_mode='html',
                        #                 disable_web_page_preview=True)

                    else:                                        # Читать далее
                      if pkanal == 9:
                        telo = telo + '<a href="' + message.text + '">Читать далее...</a>'
                        # telo = vkanal + '<a href="' + message.text + '">Читать далее...</a>'
                      else:
                        telo = telo + '<a href="' + message.text + '">Читать далее...</a>'

                      bot.delete_message(message.chat.id, message.message_id)
                      bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)

                      vkanal = telo + '\n'
                      telo = ''
                      pkanal = 10


    elif message.text.lower() == 'comb':
        telo = telo +'<a href="https://t.me/sgk_proba">Этого пункта скорее всего не будет</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
        pkanal = 11

    elif message.text.lower() == 'sight':                  # Мнение
        if pkanal == 10:
            telo = vkanal + '\n' + '<a href="' + skanal + '">#Мнение</a>'
        else:
            telo = telo + '\n' + '<a href="' + skanal + '">#Мнение</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
        pkanal = 10

    elif message.text.lower() == 'humor':                    # Юмор
        if pkanal == 10:
            telo = vkanal + '\n' + '<a href="' + skanal + '">#Юмор</a>'
        else:
            telo = telo + '\n' + '<a href="' + skanal + '">#Юмор</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
        pkanal = 10

    else:
        telo = message.text + '\n'        # Просто текст

                                                       #  Обрабатываем выделение жирным, нет проверки на ошибку
                                                       #  надо переписать это на str.find(), вместо index()
                                                       #  и разобраться с парностью
        while (True):
            try:
                index = telo.index('бб')
                telo = telo[:index] + '<b>' + telo[index + 2:]
                index = telo.index('бб', index)
                telo = telo[:index] + '</b>' + telo[index + 2:]
            except ValueError:
                break

        pkanal = 9
        # bot.send_message(message.chat.id,message ,parse_mode='html', disable_web_page_preview=True)
        # vkanal = telo



@bot.message_handler(content_types=['photo'])           #  Водяной знак p=5
def handle_docs_photo(message):
    f = tempfile.NamedTemporaryFile(delete=False)
    file_info = bot.get_file(message.photo[-1].file_id)
    f.write(bot.download_file(file_info.file_path))
    f.close()
    photo = Image.open(f.name)
    width, height = photo.size
    drawing = ImageDraw.Draw(photo)
    black = (240, 8, 12)
    font = ImageFont.truetype("/FreeMono.ttf", width // 20)
    #  font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", width//20)
    pos = (width//4, height - height//10)
    text = skanal
    drawing.text(pos, text, fill=black, font=font)
    pos = (1 + width // 4, 1 + height - height // 10)
    drawing.text(pos, text, fill=black, font=font)
    pos = (2 + width // 4, 2 + height - height // 10)
    drawing.text(pos, text, fill=black, font=font)
    photo_path = f'{f.name}.jpeg'
    photo.save(photo_path, 'JPEG')
    with open(photo_path, 'rb') as fi:
        bot.send_photo(message.chat.id, fi)
    os.remove(f.name)
    os.remove(photo_path)
    pkanal = 5



bot.polling()
