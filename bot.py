# import pytelegrambotapi
import telebot
import PIL
import tempfile
import os
import youtube_dl
import yaml
import moviepy


# telebot==3.6.6
bot = telebot.TeleBot('930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s')


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from telebot import types

from moviepy.editor import *



markup = types.ReplyKeyboardMarkup(True)


telo = ''
vkanal = ''
pkanal = 100
skanal = ''
# skanal = 'https://t.me/sgk_proba'
pv = 0
HSK1 = ''
info = ''
info_video = ''
mm = 0
itembtnNews = types.KeyboardButton('News')
itembtnADS = types.KeyboardButton('ADS')
itembtnBla = types.KeyboardButton('Sight')
itembtnDa = types.KeyboardButton('Hands')
itembtnKomb = types.KeyboardButton('Comb')
itembtndHum = types.KeyboardButton('Humor')
itembtnSend = types.KeyboardButton('Send')
itembtnRead = types.KeyboardButton('Help')

markup.row(itembtnNews, itembtnADS, itembtnDa, itembtnRead)
markup.row(itembtndHum, itembtnBla, itembtnKomb, itembtnSend)

HS = "Здравствуйте." \
     "\n" \
     "\n" \
     "Этот бот предназначен для помощи при создании сообщений в вашем канале. Для того, " \
     "чтобы начать пользоваться:" \
     "\n" \
     " - Введите имя канала, куда вы будете отправлять сообщения в формате " \
     "https://t.me/SGK_espace " \
     "\n" \
     " - Добавьте бота в Администраторы." \
     "\n \n" \
     "Теперь Вы можете прикреплять к своим сообщениям хэштеги, автоматически добавлять" \
     " ссылку на источник, скачивать видео с youtube, добавлять к изображению водяной знак." \
     "\n" \
     "<a href='https://telegra.ph/file/8ed76b876a0b67a01ef66.mp4'> " \
     "Посмотреть короткое видео по работе бота.</a>" \
     "\n \n" \
     "Простота бота накладывает ограничения - вы всегда работаете только с последним ВИДИМЫМ в боте сообщением." \
     " Настроить расположение водяного знака нельзя. Любая отправленная ссылка (кроме на ютуб) формирует “Читать далее”." \
     " Ссылка на ютуб скачивает видео. Отправленная картинка возвращается с водяным знаком. " \
     "\n" \
     "Данный проект не является коммерческим, поэтому у него нет специального чата поддержки. " \
     "Если у вас возникнет необходимость обсудить работу бота зарегистрируйтесь на моем канале или " \
     "<a href='https://t.me/joinchat/EHLktEzzYJXpERD7UgaHFQ'>задайте вопрос сразу в чате.</a> " \
     "\n" \
     "<a href='https://t.me/SGK_espace'>Подписаться на мой канал</a>"     \
     "\n" \
     "v1.02" \

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
    '<b>       Действия:</b>' \
    '\n' \
    '<b>Comb</b>    Объединить картинку или видео с сообщением' \
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
    '<a href="https://t.me/SGK_espace"> Подписаться на канал</a>'

@bot.message_handler(commands=['start'])
def start_message(message):
    global telo
    global vkanal
    global pkanal
    bot.send_message(message.chat.id, HS, parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
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
    global IdPhotoSign
    global info
    global info_video
    global mm
    global message_video_File_id
    global URL_for_Inline
    global file_info_video
    global message_keyb_IV
    global message_keyb_WM

    if message.text.lower() == 'news':                                            # Новости

        if pkanal == 10:
            telo = vkanal + '\n' + '<a href="' + skanal + '">#Новости</a>'
        else:
            telo = telo + '\n' + '<a href="' + skanal + '">#Новости</a>'

        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)

        vkanal = telo
        telo = ''
        pkanal = 10

    elif message.text.lower() == 'help':                                            # Помощь

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

    elif message.text.lower() == 'send':                                                             #  Отправка в канал
        #  Водяной знак        pkanal = 5
        #  Работа со ссылками  pkanal = 6
        #  Картинка с каментом pkanal = 11
        #  instant view        pkanal = 22
        bot.delete_message(message.chat.id, message.message_id)
        if pkanal == 5 or pkanal == 6 or pkanal == 100:
            bot.send_message(message.chat.id, 'Фото, видео и пустые сообщения не отправляются в канал', parse_mode='html', disable_web_page_preview=True)
        else:
            chat_id = "@" + skanal[13:]
            if message.from_user.id in [adm_obj.user.id for adm_obj in bot.get_chat_administrators(chat_id)]:        #  Важно, можно ли отправлять в канал
                if pkanal == 11:  #  Картинка с каментом
                    bot.send_photo(chat_id, info.photo[-1].file_id, caption=telo,  parse_mode='html')

                else:
                     if pkanal == 10:
                         telo = vkanal
                         bot.send_message(chat_id, telo, parse_mode='html', disable_web_page_preview=True)
                     elif pkanal == 22:
                         telo = vkanal
                         bot.send_message(chat_id, telo, parse_mode='html', disable_web_page_preview=False)
                     else:
                         telo = telo

                     # bot.send_message(chat_id, telo, parse_mode='html', disable_web_page_preview=True)
                     # bot.delete_message(message.chat.id, message.message_id)

                telo = ''
                vkanal = ''
                pkanal = 100
            else:
                bot.send_message(message.chat.id, 'Вы не являетесь Администратором канала', parse_mode='html', disable_web_page_preview=True)


    elif message.text.lower() == 'ads':                                             #  Реклама
        if pkanal == 10:
            telo = vkanal + '\n' + '<a href="' + skanal + '">#Реклама</a>'
        else:
            telo = telo + '\n' + '<a href="' + skanal + '">#Реклама</a>'
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, telo,parse_mode='html', disable_web_page_preview=True)
        vkanal = telo
        telo = ''
        pkanal = 10

    elif message.entities:                                                               # Работа со ссылками pkanal = 6
             for item in message.entities:
                if item.type == "url" and message.text.find(' ') == -1:

                    if 'youtube.com' in message.text or 'youtu.be' in message.text:                  #  Загружаем с Ютуб

                        f = tempfile.NamedTemporaryFile(delete=False)
                        video_path_out = f'{f.name}.mkv'
                        video_path = f.name
                        video_path_out_mp4 = f'{f.name}.mp4'

                        # bot.send_message(message.chat.id, video_path, parse_mode='html', disable_web_page_preview=True)

                        ydl_opts = {'outtmpl': video_path, 'max_filesize': 60000000, 'filename': video_path_out}

                        link_of_the_video = message.text

                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            video_path = ydl.download([link_of_the_video])

                        # bot.delete_message(message.chat.id, message.message_id)
                        # video_path = f.name
                        # bot.send_message(message.chat.id, youtube_dl.YoutubeDL.filename, parse_mode='html', disable_web_page_preview=True)


                        if os.path.exists(video_path):  # файл есть   if os.path.exists('/tmp/f.mp4'):
                            # video_save = open(video_path, 'rb')

                            video = VideoFileClip(video_path_out)  # пробую из vkv --> mp4
                            result = CompositeVideoClip([video])
                            result.write_videofile(video_path_out_mp4)

                            with open(video_path_out_mp4, 'rb') as fi:
                                info_video = bot.send_video(message.chat.id, fi)


                            os.remove(f.name)
                            #  os.remove(video_path)
                            os.remove(video_path_out)
                            os.remove(video_path_out_mp4)

                            pkanal = 6
                            mm = 2

                            file_info_video = bot.get_file(info_video.video.file_id)

                            # bot.send_message(message.chat.id, message)
                            # message_video_File_id = message.video
                        else:       # файла нет
                            bot.send_message(message.chat.id, 'Слишком большой файл', parse_mode='html', disable_web_page_preview=True)
                            telo = ''
                            vkanal = ''
                            pkanal = 100

                        #bot.send_message(message.chat.id, info)

                        # message_video_File_id = info.video.file_id
                        # mm = 2


                    elif '/t.me/' in message.text or message.text.find('@') == 0:              #  устанавливаем канал пользователя
                        #  bot.send_message(message.chat.id, message.text, parse_mode='html', disable_web_page_preview=True)
                        if not message.text.find('@') == -1:   # Нашел @    Тут что-то ни хрена не работает// а С ХЕРА БУДЕТ РАБОТАТЬ ЕСЛИ ПОПАЛ СЮДА ПО УСЛОВИЮ /t.me
                            skanal ='https://t.me/' + message.text[1:]
                        else:
                            skanal = message.text

                        telo = ''
                        vkanal = ''
                        pkanal = 100
                        bot.delete_message(message.chat.id, message.message_id)
                        bot.send_message(message.chat.id, 'Вы установили свой канал как ' + skanal, parse_mode='html', disable_web_page_preview=True)
                        pv = 2

                    else:                                                                    # Читать далее
                        if pkanal == 10:
                            telo = vkanal

                                                                                          # режим instant view 111111

                        chat_id = message.chat.id
                        message_id_Telo = message.message_id


                        keybIV = types.InlineKeyboardMarkup()  # наша клавиатура
                        key_yes_iv = types.InlineKeyboardButton(text='Да', callback_data='iv_yes')  # кнопка «Да»
                        keybIV.add(key_yes_iv)  # добавляем кнопку в клавиатуру
                        key_no_iv = types.InlineKeyboardButton(text='Нет', callback_data='iv_no')
                        keybIV.add(key_no_iv)
                        question = 'Нужен режим instant view?'
                        message_keyb_IV = bot.send_message(message.from_user.id, text=question, reply_markup=keybIV)

                        URL_for_Inline = message.text
                        # message_Id_for_delet = message.message_id

                        @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("iv"))
                        def callback_worker_iv(call):

                            global file_info
                            global URL_for_Inline
                            global telo
                            global chat_id
                            global message_id_Telo  # 1111111
                            global vkanal
                            global pkanal
                            global message_keyb_IV

                            # bot.send_message(message.chat.id, URL_for_Inline, parse_mode='html', disable_web_page_preview=False)

                            if call.data == "iv_yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
                                telo ='<a href="' + URL_for_Inline + '">.</a>' + telo  # исправить 11111

                                # inline_message_id
                                bot.delete_message(message.chat.id, message_keyb_IV.message_id)
                                # bot.delete_message(message.chat.id, message.message_id + 1)
                                # markup = types.ReplyKeyboardRemove(selective=False)   убрать нахер строку и маркуп в следующей
                                bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=False)
                                vkanal = telo + '\n'
                                telo = ''   #   А с этим надо что-то делать!!!!
                                pkanal = 22

                            elif call.data == "iv_no":
                                telo = telo + '\n' + '<a href="' + URL_for_Inline + '">Читать далее...</a>'

                                bot.delete_message(message.chat.id, message_keyb_IV.message_id)
                                # bot.delete_message(message.chat.id, message.message_id + 1)

                                bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
                                vkanal = telo + '\n'
                                telo = ''    #  А с этим надо что-то делать!!!!
                                pkanal = 10

                                # bot.send_message(message.from_user.id, reply_markup=markup)

                            # bot.editMessageReplyMarkup()
                            # return False


             if not message.text.find(' ') == -1:            # В сообщении присутствует ссылка, но это сообщение в канал

                 telo = message.text + '\n'  # Просто текст

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


    elif message.text.lower() == 'comb':                                              # Объединение картинки и сообщения

         bot.delete_message(message.chat.id, message.message_id) # удаляю слово Комб

         if pkanal == 10:
             telo = vkanal

         if mm == 1:     # mm == 1  photo
             bot.send_photo(info.chat.id, info.photo[-1].file_id, caption=telo,  parse_mode='html')
         elif mm == 2:    # mm == 2  video .file_id
             bot.send_video(message.chat.id, file_info_video.file_id, caption=telo, parse_mode='html')
             pkanal = 11

         vkanal = telo
         # telo = ''
         pkanal = 11

    elif message.text.lower() == 'sight':                                                                       # Мнение
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

    elif not message.text == '':
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



@bot.message_handler(content_types=['photo'])                                                        #  Водяной знак p=5
def handle_docs_photo(message):

    global info
    global pkanal
    global chat_id
    global message_id_Photo
    global message_Photo_File_id
    global mm
    global telo
    global vkanal
    global file_info
    global message_keyb_WM

    mm = 1
    chat_id = message.chat.id
    message_id_Photo = message.message_id
    message_Photo_File_id = message.photo[-1].file_id

    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='wm_yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='wm_no')
    keyboard.add(key_no)
    question = 'Водяной знак нужен и картинка Вам принадлежит? '
    message_keyb_WM  = bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


    @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("wm"))
    def callback_worker_wm(call):

        global telo
        global info
        global pkanal
        global chat_id
        global message_id_Photo
        global message_Photo_File_id
        global vkanal
        global file_info
        global mm
        global message_keyb_WM



        if call.data == "wm_yes":  # call.data это callback_data, которую мы указали при объявлении кнопки

            f = tempfile.NamedTemporaryFile(delete=False)

            file_info = bot.get_file(message_Photo_File_id)
            f.write(bot.download_file(file_info.file_path))
            f.close()


            bot.delete_message(chat_id, message_id_Photo)
            bot.delete_message(chat_id, message_keyb_WM.message_id)

            photo = Image.open(f.name)
            width, height = photo.size
            drawing = ImageDraw.Draw(photo)
            black = (240, 8, 12)
            font = ImageFont.truetype("/FreeMono.ttf", width // 20)
            pos = (width // 4, height - height // 10)
            text = skanal
            drawing.text(pos, text, fill=black, font=font)
            pos = (1 + width // 4, 1 + height - height // 10)
            drawing.text(pos, text, fill=black, font=font)
            pos = (2 + width // 4, 2 + height - height // 10)
            drawing.text(pos, text, fill=black, font=font)
            photo_path = f'{f.name}.jpeg'
            photo.save(photo_path, 'JPEG')
            with open(photo_path, 'rb') as fi:
                info = bot.send_photo(message.chat.id, fi)
            os.remove(f.name)
            os.remove(photo_path)
            pkanal = 5
            mm = 1


        elif call.data == "wm_no":

            f = tempfile.NamedTemporaryFile(delete=False)
            file_info = bot.get_file(message_Photo_File_id)
            f.write(bot.download_file(file_info.file_path))
            f.close()

            bot.delete_message(chat_id, message_id_Photo)
            bot.delete_message(chat_id, message_keyb_WM.message_id)

            photo = Image.open(f.name)
            photo_path = f'{f.name}.jpeg'
            photo.save(photo_path, 'JPEG')
            with open(photo_path, 'rb') as fi:
                info = bot.send_photo(message.chat.id, fi)
            os.remove(f.name)
            os.remove(photo_path)
            pkanal = 5
            mm = 1

        # bot.editMessageReplyMarkup()
        # return False

@bot.message_handler(content_types=['video'])                                     #  Водяной знак видео p=7
def handle_docs_video(message):

    global telo
    global vkanal
    global pkanal
    global mm
    global file_info_video
    global info_video
    global skanal

    f = tempfile.NamedTemporaryFile(delete=False)
    file_info_video = bot.get_file(message.video.file_id)
    f.write(bot.download_file(file_info_video.file_path))
    f.close()
    vp = f.name
    mm = 2


    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='wv_yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='wv_no')
    keyboard.add(key_no)
    question = 'Водяной знак нужен и видео Вам принадлежит? '
    message_keyb_WM  = bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


    @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("wv"))
    def callback_worker_wm(call):

        global telo
        global vkanal
        global pkanal
        global mm
        global file_info_video
        global info_video
        global skanal

        if call.data == "wv_yes":

            #  bot.delete_message(message.chat.id, message.message_id)

            my_clip = VideoFileClip(vp, audio=True)  # Видео файл с включенным аудио
            clip_duration = my_clip.duration  # длительность ролика

            w, h = my_clip.size  # размер клипа
            # Клип с текстом и прозрачным фоном
            #  font='FreeMono.ttf'
            text = 'Это не мое видео'
            if len(skanal) > 0 :
                text = skanal

            txt = TextClip(text, color='red', fontsize=w//20)
            # txt.h - 10
            txt_col = txt.on_color(size=(my_clip.w + txt.w, txt.h ), color=(0, 0, 0), pos=(120, 'center'), col_opacity=0)

            # Этот пример демонстрирует эффект движущегося текста, где позиция является функцией времени (t, в секундах).
            # Конечно, вы можете исправить положение текста вручную. Помните, что вы можете использовать строки,
            # как 'top', 'left', чтобы указать позицию

            #  txt_mov = txt_col.set_pos(lambda t: (max(w / 35, int(w - 0.5 * w * t)), max(5 * h / 6, int(20 * t))))
            txt_mov = txt_col.set_pos(lambda t: (max(w / 50, int(w - w * (t+2)/clip_duration)), max(5 * h / 6, int(h*t/clip_duration))))
            # Записать файл на диск
            final = CompositeVideoClip([my_clip, txt_mov])
            final.duration = my_clip.duration

            video_path = f'{f.name}.mp4'

            final.write_videofile(video_path, fps=24, codec='libx264')


            with open(video_path, 'rb') as fi:
                info_video = bot.send_video(message.chat.id, fi)

            os.remove(f.name)
            # os.remove(video_path)
            file_info_video = bot.get_file(info_video.video.file_id)

            # bot.send_message(message.chat.id,info_video ,parse_mode='html', disable_web_page_preview=True)
            # bot.send_message(message.chat.id,file_info_video ,parse_mode='html', disable_web_page_preview=True)



bot.polling()
