# import telebot
import PIL
import tempfile
import os
import youtube_dl
import yaml
import moviepy

import bl_as_modul
import user_info
import cfg
import sqlite3

from user_info import create_connection
from user_info import close_connection
# from user_info import acq


# bot = telebot.TeleBot('930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s')
# bot = telebot.TeleBot(cfg.token)
bot = bl_as_modul.bot_telebot()

# https://t.me/joinchat/AAAAAFMTI3MQ_G-1GNNL3w

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from telebot import types

from moviepy.editor import *

markup = types.ReplyKeyboardMarkup(True)

pv = 0
info = ''
info_video = ''


itembtnNews = types.KeyboardButton('News')
itembtnADS = types.KeyboardButton('ADS')
itembtnBla = types.KeyboardButton('Sight')
itembtnDa = types.KeyboardButton('Hands')
itembtnKomb = types.KeyboardButton('Comb')
itembtndHum = types.KeyboardButton('Humor')
itembtnSend = types.KeyboardButton('Send')
itembtnRead = types.KeyboardButton('Help')
itembtnStolen = types.KeyboardButton('Stolen')  # Украдено
itembtnThink = types.KeyboardButton('Think')    # Подумай

markup.row(itembtnNews, itembtnThink, itembtnADS, itembtnDa, itembtnRead)
markup.row(itembtndHum, itembtnStolen,itembtnBla, itembtnKomb, itembtnSend)


@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, bl_as_modul.HS, parse_mode='html', disable_web_page_preview=True, reply_markup=markup)

    user_info.acquaintance(message)



@bot.message_handler(func=lambda message: message.forward_from_chat, content_types=['text'])
def send_text(message):
    forward_message_text = message.text
    chat_from_forward = message.forward_from_chat.id

    new_link = bot.export_chat_invite_link(message.forward_from_chat.id)
    bot.send_message(message.chat.id, new_link)

    # qqq = bot.export_Chat_Invite_Link(chat_from_forward)
    # bot.send_message(message.chat.id, qqq, parse_mode='html', disable_web_page_preview=True)

    title_from_forward = message.forward_from_chat.title

    bot.send_message(message.chat.id, message.forward_from_chat.id, parse_mode='html', disable_web_page_preview=True)
    conn = user_info.create_connection()
    user = user_info.find_user(conn, message.chat.id)
    bot.send_message(message.chat.id, message.chat.id, parse_mode='html', disable_web_page_preview=True)

    if not user:
        user_info.acquaintance(message)
        user_info.close_connection(conn)

        keybmc = types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes_mc = types.InlineKeyboardButton(text='Да', callback_data='mc_yes')  # кнопка «Да»
        keybmc.add(key_yes_mc)  # добавляем кнопку в клавиатуру
        key_no_mc = types.InlineKeyboardButton(text='Нет', callback_data='mc_no')
        keybmc.add(key_no_mc)
        question = 'Вы переслали ваше сообщение из вашего канала?'
        message_keyb_mc = bot.send_message(message.from_user.id, text=question, reply_markup=keybmc)

        @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("mc"))
        def callback_worker_mc(call):

            conn = user_info.create_connection()

            if call.data == "mc_yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
                user_info.add_user(conn, message.chat.id, chat_from_forward, title_from_forward, 100, '', '', new_link, 0)
                user_info.close_connection(conn)
                bot.send_message(message.chat.id, 'Данные о вашем канале успешно добавлены', parse_mode='html',
                                 disable_web_page_preview=True)


            elif call.data == "mc_no":
                bot.send_message(message.chat.id, forward_message_text, parse_mode='html',
                                 disable_web_page_preview=True)

    else:
        # Подумать, что сделать с пересланным сообщением (почистить от кого, убрать ссылки)
        bot.send_message(message.chat.id, forward_message_text, parse_mode='html',
                         disable_web_page_preview=True)


@bot.message_handler(content_types=['document'])
def start_message(document):
    bot.send_message(document.chat.id, document)


@bot.message_handler(content_types=['text'])
def send_text(message):

    global IdPhotoSign
    global info
    global info_video
    global message_video_File_id
    global URL_for_Inline
    global file_info_video
    global message_keyb_IV
    global message_keyb_WM


    if message.text.lower() == 'help':                                            # Помощь
        user_info.help_bl_as(message)

    elif message.text.lower() == 'hands':                               #  Своми руками
        user_info.add_hashtag(message, 'hands')

    elif message.text.lower() == 'think':                               #  Подумай
        user_info.add_hashtag(message, 'think')

    elif message.text.lower() == 'stolen':                               #  Украдено
        user_info.add_hashtag(message, 'stolen')

    elif message.text.lower() == 'ads':                                   # Реклама
        user_info.add_hashtag(message, 'ads')

    elif message.text.lower() == 'sight':                                  # Мнение
        user_info.add_hashtag(message, 'sight')

    elif message.text.lower() == 'humor':                                  # Юмор
        user_info.add_hashtag(message, 'humor')

    elif message.text.lower() == 'news':                       # Новости
        user_info.add_hashtag(message, 'news')



    elif message.text.lower() == 'send':                                                             #  Отправка в канал
        #  НЕ ОТПРАВЛЯЕТ ПОСЛЕ КОМБ ПОЧЕМУ ТО
        #  видео с каментом    pkanal = 11 mm=2
        #  Водяной знак        pkanal = 5     u[3]
        #  Работа со ссылками  pkanal = 6
        #  Картинка с каментом pkanal = 11 mm=1
        #  instant view        pkanal = 22
        #  просто сообщение    pkanal = 9
        bot.delete_message(message.chat.id, message.message_id)

        conn = user_info.create_connection()
        u = user_info.find_user(conn, message.chat.id)


        if u[3] == 5 or u[3] == 6 or u[3] == 100:
            bot.send_message(message.chat.id, 'Пустые сообщения не отправляются в канал', parse_mode='html', disable_web_page_preview=True)
        else:
 
            chat_id = u[1]
            # bot.send_message(message.chat.id, skanal, parse_mode='html', disable_web_page_preview=True)
            # bot.send_message(message.chat.id, chat_id, parse_mode='html', disable_web_page_preview=True)

            if message.from_user.id in [adm_obj.user.id for adm_obj in bot.get_chat_administrators(chat_id)]:        #  Важно, можно ли отправлять в канал
                if u[3] == 11:  #  Картинка или видео с каментом
                    if u[7] == 2:
                        bot.send_video(chat_id, file_info_video.file_id, caption=u[5], parse_mode='html')  # 123
                    else:
                        bot.send_photo(chat_id, info.photo[-1].file_id, caption=u[5],  parse_mode='html')

                else:
                     if u[3] == 10 or u[3] == 9:

                         bot.send_message(chat_id, u[4], parse_mode='html', disable_web_page_preview=True)
                     elif u[3] == 22:

                         bot.send_message(chat_id, u[4], parse_mode='html', disable_web_page_preview=False)


                user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0)


            else:
                bot.send_message(message.chat.id, 'Вы не являетесь Администратором канала', parse_mode='html', disable_web_page_preview=True)

        user_info.close_connection(conn)


    elif message.entities:                                             # Работа со ссылками pkanal = 6
             for item in message.entities:
                if item.type == "url" and message.text.find(' ') == -1:

                    if 'youtube.com' in message.text or 'youtu.be' in message.text or 'ok.ru' in message.text:                  #  Загружаем с Ютуб

                        link_of_the_video = message.text
                        bot.delete_message(message.chat.id, message.message_id)

                        # bot.send_chat_action(message.chat.id, action='upload_video')
                        # gif = bot.send_document(message.chat.id, 'CgADAgAD6wUAAuOb8Ugra3Kv7t4n_hYE')
                        # bot.send_chat_action(message.chat.id, action='upload_video')

                        f = tempfile.NamedTemporaryFile(delete=False)
                        video_path_out = f'{f.name}.mkv'   # .mkv
                        video_path = f.name
                        video_path_out_mp4 = f'{f.name}.mp4'

                        ydl_opts = {'outtmpl': video_path,
                                    'merge_output_format': 'mkv',
                                    'noplaylist': 'true',
                                    'ignoreerrors': 'true',
                                    'quiet': True,
                                    'max_filesize': 5120000000,
                                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                                    'filename': video_path_out}


                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            video_path = ydl.download([link_of_the_video])

                        bot.send_message(message.chat.id, 'Закончили Ютуб ', parse_mode='html', disable_web_page_preview=True)

                        if not os.path.exists(video_path_out) == 0:  # файл есть   if os.path.exists('/tmp/f.mp4'):

                            video = VideoFileClip(video_path_out)  # mkv --> mp4

                            result = CompositeVideoClip([video])

                            result.write_videofile(video_path_out_mp4)

                            # bot.delete_message(message.chat.id, gif.message_id)
                            with open(video_path_out_mp4, 'rb') as fi:
                                 info_video = bot.send_video(message.chat.id, fi)


                            os.remove(f.name)
                            os.remove(video_path_out)
                            os.remove(video_path_out_mp4)

                            conn = user_info.create_connection()
                            u = user_info.find_user(conn, message.chat.id)
                            user_info.update_user(conn, u[0], u[1], u[2], 6, u[4], u[5], u[6], 2)
                            user_info.close_connection(conn)

                            file_info_video = bot.get_file(info_video.video.file_id)

                        else:       # файла нет
                            # bot.delete_message(message.chat.id, gif.message_id)
                            bot.send_message(message.chat.id, 'Слишком большой файл для загрузки,' +  "<a href='https://t.me/joinchat/EHLktEzzYJXpERD7UgaHFQ'> пишите мне в чат </a>" + 'какие варианты интересны', parse_mode='html', disable_web_page_preview=True)
                            # предложить  сделать ссылку  на ролик

                            conn = user_info.create_connection()
                            u = user_info.find_user(conn, message.chat.id)
                            user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0)
                            user_info.close_connection(conn)


                    else:                                           # Читать далее


                        conn = user_info.create_connection()
                        u = user_info.find_user(conn, message.chat.id)
                        if u[3]  == 10:
                            # telo = vkanal
                            user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], u[4], u[6], 0)
                            user_info.close_connection(conn)


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


                        @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("iv"))
                        def callback_worker_iv(call):

                            global file_info
                            global URL_for_Inline
                            global chat_id
                            global message_id_Telo  # 1111111
                            global message_keyb_IV

                            # bot.send_message(message.chat.id, URL_for_Inline, parse_mode='html', disable_web_page_preview=False)

                            if call.data == "iv_yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
                                 telo ='<a href="' + URL_for_Inline + '">.</a>' + telo  # исправить 11111

                                 bot.delete_message(message.chat.id, message_keyb_IV.message_id)
                                 bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=False)

                                 vkanal = telo + '\n'

                                 conn = user_info.create_connection()
                                 u = user_info.find_user(conn, message.chat.id)
                                 user_info.update_user(conn, u[0], u[1], u[2], 22, vkanal, '', u[6], u[7])
                                 user_info.close_connection(conn)

                            elif call.data == "iv_no":

                                 telo = telo + '\n' + '<a href="' + URL_for_Inline + '">Читать далее...</a>'

                                 bot.delete_message(message.chat.id, message_keyb_IV.message_id)

                                 bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)

                                 conn = user_info.create_connection()
                                 u = user_info.find_user(conn, message.chat.id)
                                 user_info.update_user(conn, u[0], u[1], u[2], 10, vkanal, '', u[6], u[7])
                                 user_info.close_connection(conn)

             if not message.text.find(' ') == -1:            # В сообщении присутствует ссылка, но это сообщение в канал

                 telo = message.text + '\n'  # Просто текст

                 #  Обрабатываем выделение жирным, нет проверки на ошибку
                 #  надо переписать это на str.find(), вместо index()
                 #  и разобраться с парностью
                 if round(telo.count('ьь')/2) - telo.count('ьь')/2 == 0.5 or telo.count('ьь') == 1:
                     bot.send_message(message.chat.id, 'Вы неправильно оформили выделение жирным шрифтом',
                                      parse_mode='html', disable_web_page_preview=True)
                 else:
                     while (True):
                         try:
                             index = telo.index('ьь')
                             telo = telo[:index] + '<b>' + telo[index + 2:]

                             index = telo.index('ьь', index)
                             telo = telo[:index] + '</b>' + telo[index + 2:]
                         except ValueError:
                             break

                 conn = user_info.create_connection()
                 u = user_info.find_user(conn, message.chat.id)
                 user_info.update_user(conn, u[0], u[1], u[2], 9, u[4], telo, u[6], u[7])
                 user_info.close_connection(conn)


    elif message.text.lower() == 'comb':                                              # Объединение картинки и сообщения

         conn = user_info.create_connection()
         u = user_info.find_user(conn, message.chat.id)

         bot.delete_message(message.chat.id, message.message_id)  # удаляю слово Комб

         if u[7] > 0:

             if message.message_id - 1:
                 bot.delete_message(message.chat.id, message.message_id - 1)  # удаляю сообщение для комб

             if u[3] == 10 or u[3] == 9:
                 telo = u[4]

             if u[7] == 1:  # mm == 1  photo

                 bot.send_photo(info.chat.id, info.photo[-1].file_id, caption=telo, parse_mode='html')

             elif u[7] == 2:  # mm == 2  video .file_id   # 123

                 bot.send_video(message.chat.id, file_info_video.file_id, caption=telo, parse_mode='html')

             user_info.update_user(conn, u[0], u[1], u[2], 11, telo, telo, u[6], u[7])

         else:
             bot.send_message(message.chat.id, 'Нет медиафайла!', parse_mode='html', disable_web_page_preview=True,
                              reply_markup=markup)

         user_info.close_connection(conn)



    elif not message.text == '':  # Просто текст
        user_info.just_text(message)


@bot.message_handler(content_types=['photo'])                                                        #  Водяной знак p=5
def handle_docs_photo(message):

    global info
    global chat_id
    global message_id_Photo
    global message_Photo_File_id
    global file_info
    global message_keyb_WM


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


        global info
        global message_id_Photo
        global message_Photo_File_id
        global file_info
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

            conn = user_info.create_connection()
            u = user_info.find_user(conn, message.chat.id)
            text = u[2]
            user_info.close_connection(conn)

            drawing.text(pos, text, fill=black, font=font)
            pos = (1 + width // 4, 1 + height - height // 10)
            drawing.text(pos, text, fill=black, font=font)
            pos = (2 + width // 4, 2 + height - height // 10)
            drawing.text(pos, text, fill=black, font=font)
            photo_path = f'{f.name}.jpeg'
            photo.save(photo_path, 'JPEG')
            bot.send_chat_action(message.chat.id, action='upload_photo')

            with open(photo_path, 'rb') as fi:
                info = bot.send_photo(message.chat.id, fi)
            os.remove(f.name)
            os.remove(photo_path)

            conn = user_info.create_connection()
            u = user_info.find_user(conn, message.chat.id)
            user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1)
            user_info.close_connection(conn)


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

            conn = user_info.create_connection()
            u = user_info.find_user(conn, message.chat.id)
            user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1)
            user_info.close_connection(conn)


@bot.message_handler(content_types=['video'])                       #  Водяной знак видео p=7 ??????
def handle_docs_video(message):


    global file_info_video
    global info_video


    f = tempfile.NamedTemporaryFile(delete=False)
    file_info_video = bot.get_file(message.video.file_id)
    f.write(bot.download_file(file_info_video.file_path))
    f.close()
    vp = f.name

    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='wv_yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='wv_no')
    keyboard.add(key_no)
    question = 'Водяной знак нужен и видео Вам принадлежит? '
    message_keyb_WM  = bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


    @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("wv"))
    def callback_worker_wm(call):

        global file_info_video
        global info_video

        if call.data == "wv_yes":
            # bot.answer_callback_query(callback_query_id=call.id, text='Дело делаем')
            bot.send_chat_action(message.chat.id, action='upload_video')
            # bot.send_document(message.chat.id, 'CgADAgAD6wUAAuOb8Ugra3Kv7t4n_hYE')

            my_clip = VideoFileClip(vp, audio=True)  # Видео файл с включенным аудио
            clip_duration = my_clip.duration  # длительность ролика

            w, h = my_clip.size  # размер клипа
            # Клип с текстом и прозрачным фоном

            conn = user_info.create_connection()
            u = user_info.find_user(conn, message.chat.id)
            text = u[2]
            user_info.update_user(conn, u[0], u[1], u[2], 7, u[4], u[5], u[6], 2)
            user_info.close_connection(conn)

            txt = TextClip(text, color='red', fontsize=w//20)
            txt_col = txt.on_color(size=(my_clip.w + txt.w, txt.h ), color=(0, 0, 0), pos=(120, 'center'), col_opacity=0)

            # Этот пример демонстрирует эффект движущегося текста, где позиция является функцией времени (t, в секундах).
            # Конечно, вы можете исправить положение текста вручную. Помните, что вы можете использовать строки,
            # как 'top', 'left', чтобы указать позицию

            txt_mov = txt_col.set_pos(lambda t: (max(w / 50, int(w - w * (t+2)/clip_duration)), max(5 * h / 6, int(h*t/clip_duration))))
            # Записать файл на диск
            final = CompositeVideoClip([my_clip, txt_mov])
            final.duration = my_clip.duration

            video_path = f'{f.name}.mp4'

            # bot.send_chat_action(message.chat.id, action='record_video')
            # bot.send_video(message.chat.id, '82428c1ff4a97038984f32ab98bda266')   гифку ну никак


            final.write_videofile(video_path, fps=24, codec='libx264')

            bot.delete_message(message.chat.id, message.message_id)  #  удаляем ненужное сообщение

            with open(video_path, 'rb') as fi:
                info_video = bot.send_video(message.chat.id, fi)

            os.remove(f.name)
            file_info_video = bot.get_file(info_video.video.file_id)



bot.polling()

