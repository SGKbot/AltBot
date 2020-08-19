#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
itembtnThink = types.KeyboardButton('Think')  # Подумай
itembtnHum = types.KeyboardButton('Humor')
itembtnSend = types.KeyboardButton('Send')
itembtnRead = types.KeyboardButton('Help')
itembtnStolen = types.KeyboardButton('Stolen')  # Украдено
# itembtnCha = types.KeyboardButton('Chan')    # Канал
# itembtnZerro = types.KeyboardButton('Zerro')    # Пусто


markup.row(itembtnNews, itembtnThink, itembtnADS, itembtnDa, itembtnRead)
markup.row(itembtnHum, itembtnStolen, itembtnBla, itembtnKomb, itembtnSend)


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

    title_from_forward = message.forward_from_chat.title

    bot.send_message(message.chat.id, message.forward_from_chat.id, parse_mode='html', disable_web_page_preview=True)
    conn = user_info.create_connection()
    user = user_info.find_user(conn, message.chat.id, title_from_forward, 3)
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
                kp = user_info.find_user(conn, message.chat.id, '', 1)
                if not kp:
                    user_info.add_user(conn, message.chat.id, chat_from_forward, title_from_forward, 100, '', '', new_link, 0, 1, 0, '')
                else:
                    user_info.add_user(conn, message.chat.id, chat_from_forward, title_from_forward, 100, '', '', new_link, 0, 0, 0, '')

                user_info.close_connection(conn)
                bot.send_message(message.chat.id, 'Данные о вашем канале успешно добавлены', parse_mode='html', disable_web_page_preview=True)


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
    global message_keyb_cm
    global message_keyb_IV
    global message_keyb_WM
    global message_keyb_mf
    global message_keyb3

    if message.text.lower() == 'help':  # Помощь
        user_info.help_bl_as(message)

        help_main = inl_keyb6('Выбрать канал', 'Добавить канал', 'Удалить канал', 'Выйти из меню', '', '', 'hm')
        bot.send_message(message.from_user.id, text='Выберите необходимое действие', reply_markup=help_main)

    elif message.text.lower() == 'hands':  # Своми руками
        user_info.add_hashtag(message, 'hands')

    elif message.text.lower() == 'think':  # Подумай
        user_info.add_hashtag(message, 'think')

    elif message.text.lower() == 'stolen':  # Украдено
        user_info.add_hashtag(message, 'stolen')

    elif message.text.lower() == 'ads':  # Реклама
        user_info.add_hashtag(message, 'ads')

    elif message.text.lower() == 'sight':  # Мнение
        user_info.add_hashtag(message, 'sight')

    elif message.text.lower() == 'humor':  # Юмор
        user_info.add_hashtag(message, 'humor')

    elif message.text.lower() == 'news':  # Новости
        user_info.add_hashtag(message, 'news')



    elif message.text.lower() == 'send':  # Отправка в канал
        #  НЕ ОТПРАВЛЯЕТ ПОСЛЕ КОМБ ПОЧЕМУ ТО
        #  видео с каментом    pkanal = 11 mm=2
        #  Водяной знак        pkanal = 5     u[3]
        #  Работа со ссылками  pkanal = 6
        #  Картинка с каментом pkanal = 11 mm=1
        #  instant view        pkanal = 22
        #  просто сообщение    pkanal = 9
        bot.delete_message(message.chat.id, message.message_id)

        conn = user_info.create_connection()
        u = user_info.find_user(conn, message.chat.id, '', 1)

        if u[3] == 5 or u[3] == 6 or u[3] == 100:
            bot.send_message(message.chat.id, 'Пустые сообщения не отправляются в канал', parse_mode='html',
                             disable_web_page_preview=True)
        else:

            chat_id = u[1]
            # bot.send_message(message.chat.id, skanal, parse_mode='html', disable_web_page_preview=True)
            # bot.send_message(message.chat.id, chat_id, parse_mode='html', disable_web_page_preview=True)

            if message.from_user.id in [adm_obj.user.id for adm_obj in
                                        bot.get_chat_administrators(chat_id)]:  # Важно, можно ли отправлять в канал
                if u[3] == 11:  # Картинка или видео с каментом
                    if u[7] == 2:
                        bot.send_video(u[1], file_info_video.file_id, caption=u[5], parse_mode='html')  # 123
                    else:
                        bot.send_photo(u[1], u[10], caption=u[5], parse_mode='html')

                else:
                    if u[3] == 10 or u[3] == 9:

                        bot.send_message(chat_id, u[4], parse_mode='html', disable_web_page_preview=True)
                    elif u[3] == 22:

                        bot.send_message(chat_id, u[4], parse_mode='html', disable_web_page_preview=False)

                user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], u[9], '')


            else:
                bot.send_message(message.chat.id, 'Вы не являетесь Администратором канала', parse_mode='html',  disable_web_page_preview=True)

        user_info.close_connection(conn)


    elif message.entities:  # Работа со ссылками pkanal = 6
        for item in message.entities:
            if item.type == "url" and message.text.find(' ') == -1:

                if 'youtube.com' in message.text or 'youtu.be' in message.text or 'ok.ru' in message.text:  # Загружаем с Ютуб

                    link_of_the_video = message.text
                    bot.delete_message(message.chat.id, message.message_id)

                    # bot.send_chat_action(message.chat.id, action='upload_video')
                    # gif = bot.send_document(message.chat.id, 'CgADAgAD6wUAAuOb8Ugra3Kv7t4n_hYE')
                    # bot.send_chat_action(message.chat.id, action='upload_video')

                    f = tempfile.NamedTemporaryFile(delete=False)
                    video_path_out = f'{f.name}.mkv'  # .mkv
                    video_path = f.name
                    video_path_out_mp4 = f'{f.name}.mp4'

                    ydl_opts = {'outtmpl': video_path,
                                'merge_output_format': 'mkv',
                                'noplaylist': 'true',
                                'ignoreerrors': 'true',
                                'quiet': True,
                                'max_filesize': 1200000000,
                                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                                'filename': video_path_out}

                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        video_path = ydl.download([link_of_the_video])

                    bot.send_message(message.chat.id, 'Закончили Ютуб ', parse_mode='html',
                                     disable_web_page_preview=True)

                    # info_video = bot.send_video(message.chat.id, video_path)

                    if not os.path.exists(video_path_out) == 0:  # файл есть   if os.path.exists('/tmp/f.mp4'):

                        video = VideoFileClip(video_path_out)  # mkv --> mp4
                        result = CompositeVideoClip([video])
                        result.write_videofile(video_path_out_mp4)

                        with open(video_path_out_mp4, 'rb') as fi:
                           info_video = bot.send_video(message.chat.id, fi)

                        # info_video = bot.send_video(message.chat.id, video_path_out_mp4)

                        os.remove(f.name)
                        os.remove(video_path_out)
                        os.remove(video_path_out_mp4)

                        conn = user_info.create_connection()
                        u = user_info.find_user(conn, message.chat.id, '', 1)
                        user_info.update_user(conn, u[0], u[1], u[2], 6, u[4], u[5], u[6], 2, u[8], u[9], '')
                        user_info.close_connection(conn)

                        # file_info_video = bot.get_file(info_video.video.file_id)

                    else:  # файла нет
                        # bot.delete_message(message.chat.id, gif.message_id)
                        bot.send_message(message.chat.id, 'Слишком большой файл для загрузки,' + "<a href='https://t.me/joinchat/EHLktEzzYJXpERD7UgaHFQ'> пишите мне в чат </a>" + 'какие варианты интересны', parse_mode='html', disable_web_page_preview=True)
                        # предложить  сделать ссылку  на ролик

                        conn = user_info.create_connection()
                        u = user_info.find_user(conn, message.chat.id, '', 1)
                        user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], u[9], '')
                        user_info.close_connection(conn)


                else:  # Читать далее

                    conn = user_info.create_connection()
                    u = user_info.find_user(conn, message.chat.id, '', 1)
                    if u[3] == 10:
                        # telo = vkanal
                        user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], u[4], u[6], 0, u[8], U[9], '')
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
                            telo = '<a href="' + URL_for_Inline + '">.</a>' + telo  # исправить 11111

                            bot.delete_message(message.chat.id, message_keyb_IV.message_id)
                            bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=False)

                            vkanal = telo + '\n'

                            conn = user_info.create_connection()
                            u = user_info.find_user(conn, message.chat.id, '', 1)
                            user_info.update_user(conn, u[0], u[1], u[2], 22, vkanal, '', u[6], u[7], u[8], U[9], '')
                            user_info.close_connection(conn)

                        elif call.data == "iv_no":

                            telo = telo + '\n' + '<a href="' + URL_for_Inline + '">Читать далее...</a>'

                            bot.delete_message(message.chat.id, message_keyb_IV.message_id)

                            bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)

                            conn = user_info.create_connection()
                            u = user_info.find_user(conn, message.chat.id, '', 1)
                            user_info.update_user(conn, u[0], u[1], u[2], 10, vkanal, '', u[6], u[7], u[8], U[9], '')
                            user_info.close_connection(conn)

        if not message.text.find(' ') == -1:  # В сообщении присутствует ссылка, но это сообщение в канал

            telo = message.text + '\n'  # Просто текст

            #  Обрабатываем выделение жирным, нет проверки на ошибку
            #  надо переписать это на str.find(), вместо index()
            #  и разобраться с парностью
            if round(telo.count('ьь') / 2) - telo.count('ьь') / 2 == 0.5 or telo.count('ьь') == 1:
                bot.send_message(message.chat.id, 'Вы неправильно оформили выделение жирным шрифтом', parse_mode='html', disable_web_page_preview=True)
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
            u = user_info.find_user(conn, message.chat.id, '', 1)
            user_info.update_user(conn, u[0], u[1], u[2], 9, u[4], telo, u[6], u[7], u[8], u[9], '')
            user_info.close_connection(conn)


    elif message.text.lower() == 'comb':  # Объединение картинки и сообщения

        conn = user_info.create_connection()
        u = user_info.find_user(conn, message.chat.id, '', 1)

        bot.delete_message(message.chat.id, message.message_id)  # удаляю слово Комб

        if u[7] > 0:

            if message.message_id - 1:
                bot.delete_message(message.chat.id, message.message_id - 1)  # удаляю сообщение для комб

            if u[3] == 10 or u[3] == 9:
                telo = u[4]

            if u[7] == 1:  # mm == 1  photo

                bot.send_photo(u[0], u[10], caption=u[5], parse_mode='html')

            elif u[7] == 2:  # mm == 2  video .file_id   # 123

                bot.send_video(u[0], u[10], caption=u[5], parse_mode='html')

            user_info.update_user(conn, u[0], u[1], u[2], 11, telo, telo, u[6], u[7], u[8], u[9], u[10])

        else:
            bot.send_message(message.chat.id, 'Нет медиафайла!', parse_mode='html', disable_web_page_preview=True,
                             reply_markup=markup)

        user_info.close_connection(conn)


    elif not message.text == '':  # Просто текст
        user_info.just_text(message)


@bot.message_handler(content_types=['photo'])  # Водяной знак p=5
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

    name_keyb = inl_keyb6('Да', 'Нет', '', '', '', '', 'wmp')
    bot.send_message(message.from_user.id, text='Водяной знак нужен и картинка Вам принадлежит?', reply_markup=name_keyb)


@bot.message_handler(content_types=['video'])  # Водяной знак видео p=7 ??????
def handle_docs_video(message):
    # global file_info_video
    # global info_video

    # file_info_video = bot.get_file(message.video.file_id)
    # l = file_info_video.file_path
    l = message.video.file_id

    name_keyb = inl_keyb6('Да', 'Нет', '', '', '', '', 'wv')
    bot.send_message(message.from_user.id, text='Водяной знак нужен и видео Вам принадлежит?', reply_markup=name_keyb)

    conn = user_info.create_connection()
    u = user_info.find_user(conn, message.chat.id, '', 1)
    user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], 0, l)
    user_info.close_connection(conn)


@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('wv'))
def callback_worker_5(call):
    # global file_info_video
    # global info_video

    conn = user_info.create_connection()
    u = user_info.find_user(conn, call.message.chat.id, '', 1)
    file_info_video = u[10]
    user_info.close_connection(conn)

    f = tempfile.NamedTemporaryFile(delete=False)
    # f.write(bot.download_file(file_info_video))
    f.write(bot.get_file(file_info_video))
    f.close()
    vp = f.name

    if call.data == "wv1":
        my_clip = VideoFileClip(vp, audio=True)  # Видео файл с включенным аудио
        clip_duration = my_clip.duration  # длительность ролика

        w, h = my_clip.size  # размер клипа
        # Клип с текстом и прозрачным фоном

        conn = user_info.create_connection()
        u = user_info.find_user(conn, call.message.chat.id, '', 1)
        text = u[2]
        user_info.update_user(conn, u[0], u[1], u[2], 7, u[4], u[5], u[6], 2, u[8], u[9], '')
        user_info.close_connection(conn)

        txt = TextClip(text, color='red', fontsize=w // 20)
        txt_col = txt.on_color(size=(my_clip.w + txt.w, txt.h), color=(0, 0, 0), pos=(120, 'center'), col_opacity=0)

        # Этот пример демонстрирует эффект движущегося текста, где позиция является функцией времени (t, в секундах).
        # Конечно, вы можете исправить положение текста вручную. Помните, что вы можете использовать строки,
        # как 'top', 'left', чтобы указать позицию

        txt_mov = txt_col.set_pos(
            lambda t: (max(w / 50, int(w - w * (t + 2) / clip_duration)), max(5 * h / 6, int(h * t / clip_duration))))
        # Записать файл на диск
        final = CompositeVideoClip([my_clip, txt_mov])
        final.duration = my_clip.duration

        video_path = f'{f.name}.mp4'

        final.write_videofile(video_path, fps=24, codec='libx264')

        with open(video_path, 'rb') as fi:
            info_video = bot.send_video(call.message.chat.id, fi)

        os.remove(f.name)
        # file_info_video = bot.get_file(info_video.video.file_id)


def inl_keyb6(txt1, txt2, txt3, txt4, txt5, txt6, cbd):

    name_keyb = types.InlineKeyboardMarkup()  # наша клавиатура

    key_1 = types.InlineKeyboardButton(text=txt1, callback_data=cbd+'1')
    name_keyb.add(key_1)  # добавляем кнопку в клавиатуру

    key_2 = types.InlineKeyboardButton(text=txt2, callback_data=cbd+'2')
    name_keyb.add(key_2)

    if not txt3 == '':
        key_3 = types.InlineKeyboardButton(text=txt3, callback_data=cbd+'3')
        name_keyb.add(key_3)

    if not txt4 == '':
        key_4 = types.InlineKeyboardButton(text=txt4, callback_data=cbd+'4')
        name_keyb.add(key_4)

    if not txt5 == '':
        key_5 = types.InlineKeyboardButton(text=txt5, callback_data=cbd+'5')
        name_keyb.add(key_5)

    if not txt6 == '':
        key_6 = types.InlineKeyboardButton(text=txt3, callback_data=cbd+'6')
        name_keyb.add(key_6)

    return name_keyb


@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('hm'))
def callback_worker_3(call):

    bot.delete_message(call.message.chat.id, call.message.message_id)

    conn = user_info.create_connection()
    etud = user_info.find_user(conn, call.message.chat.id, '', 2)
    chaname = user_info.Name_ch_(etud)
    user_info.close_connection(conn)

    if call.data == "hm1":  # Выбрать канал

        help_v = inl_keyb6(chaname[0], chaname[1], chaname[2], chaname[3], chaname[4], chaname[5], 'hvc')
        bot.send_message(call.message.chat.id, text='канал?', reply_markup=help_v)

    if call.data == "hm2": # Добавить канал
        bot.send_message(call.message.chat.id, text='добавить канал')


    if call.data == "hm3":  # Удалить канал

        help_d = inl_keyb6(chaname[0], chaname[1], chaname[2], chaname[3], chaname[4], chaname[5], 'hdc')
        bot.send_message(call.message.chat.id, text='канал?', reply_markup=help_d)


@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('hvc'))
def callback_worker_4(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    s = int(call.data[3])-1

    conn = user_info.create_connection()
    etud = user_info.find_user(conn, call.message.chat.id, '', 2)
    vis = etud[s]
    n = user_info.find_user(conn, call.message.chat.id, '', 1)
    user_info.update_user(conn, n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7], 0, n[9], '')
    cursor = conn.cursor()
    del_user = (vis[0], vis[2])
    cursor.execute('DELETE FROM projects WHERE bot_chat_id = ? and channel_name = ?', del_user)
    conn.commit()
    visi = (vis[0], vis[1], vis[2], vis[3], vis[4], vis[5], vis[6], vis[7], 1, vis[9], '')
    cursor.execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', visi)
    conn.commit()
    user_info.close_connection(conn)

@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("wmp"))
def callback_worker_wm(call):  # водяной знак фото
    if call.data == "wmp1":
        f = tempfile.NamedTemporaryFile(delete=False)

        file_info = bot.get_file(message_Photo_File_id)
        f.write(bot.download_file(file_info.file_path))
        f.close()

        bot.delete_message(chat_id, message_id_Photo)
        # bot.delete_message(chat_id, message_keyb_WM.message_id)

        photo = Image.open(f.name)
        width, height = photo.size
        drawing = ImageDraw.Draw(photo)
        black = (240, 8, 12)
        font = ImageFont.truetype(cfg.user_font, width // 20)
        pos = (width // 2, height - height // 10)

        conn = user_info.create_connection()
        u = user_info.find_user(conn, chat_id, '', 1)
        text = u[2]
        user_info.close_connection(conn)

        drawing.text(pos, text, fill=black, font=font)
        pos = (1 + width // 2, 1 + height - height // 10)
        drawing.text(pos, text, fill=black, font=font)
        pos = (2 + width // 2, 2 + height - height // 10)
        drawing.text(pos, text, fill=black, font=font)
        photo_path = f'{f.name}.jpeg'
        photo.save(photo_path, 'JPEG')
        # bot.send_chat_action(message.chat.id, action='upload_photo')

        with open(photo_path, 'rb') as fi:
            info = bot.send_photo(chat_id, fi)
        os.remove(f.name)
        os.remove(photo_path)

        fip = info.photo[-1].file_id

        conn = user_info.create_connection()
        u = user_info.find_user(conn, chat_id, '', 1)
        user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8], u[9], fip)
        user_info.close_connection(conn)

    if call.data == "wmp2":
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

        fip = info.photo[-1].file_id

        conn = user_info.create_connection()
        u = user_info.find_user(conn, message.chat.id, '', 1)
        user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8], u[9], fip)
        user_info.close_connection(conn)








bot.polling()