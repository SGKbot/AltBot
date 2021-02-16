#!/usr/bin/python3
# -*- coding: utf-8 -*-
import telethon
from telethon.events import StopPropagation
from telethon.sync import TelegramClient, events, utils
from telethon.tl.custom import Button
from telethon.client.chats import ChatMethods

from telethon.tl import types
from telethon.tl.types import (
    UpdateShortMessage,
    ReplyKeyboardMarkup,
    ReplyInlineMarkup,
    KeyboardButtonRow,
    KeyboardButtonCallback,
)

from telethon.tl import functions
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.client.messages import MessageMethods

import PIL
import tempfile
import os
import youtube_dl
import yaml
import moviepy

import bl_as_modul
import user_info
import cfg
import aiosqlite
# import sqlite3

from user_info import create_connection
from user_info import close_connection

bot = bl_as_modul.client

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from moviepy.editor import *

pv = 0
info = ''
info_video = ''

markup1 = types.ReplyInlineMarkup(
    rows=[
        KeyboardButtonRow(
            buttons=[
                KeyboardButtonCallback(text="Tk", data="tk"),
                KeyboardButtonCallback(text="Gs", data=b"/gs"),
                KeyboardButtonCallback(text="Bal", data=b"/bal"),
            ]
        ),
        KeyboardButtonRow(
            buttons=[
                KeyboardButtonCallback(text="Task", data=b"/task"),
                KeyboardButtonCallback(text="Games", data=b"/games"),
                KeyboardButtonCallback(text="Balance", data=b"/balance"),
            ]
        )
    ]
)


@bot.on(events.NewMessage(pattern='/start'))
async def start_message(message):
    await bot.send_message(message.chat_id, bl_as_modul.HS, parse_mode='html', link_preview=False, buttons=[
        [
            Button.text('News'),
            Button.text('Think'),
            Button.text('ADS'),
            Button.text('Hands'),
            Button.text('Help')
        ],
        [
            Button.text('Humor', resize=True, single_use=True),
            Button.text('Stolen'),
            Button.text('Sight'),
            Button.text('Comb'),
            Button.text('Send')
        ]
    ])

    await bot.send_message(message.chat_id, cfg.Pr, parse_mode='html', link_preview=False)
    # , buttons=markup1)

    # await event.delete()
    # No other event handler will have a chance to handle this event
    raise StopPropagation


@bot.on(events.NewMessage(forwards='true'))
async def send_text(message):
    new_link = (await bot(ExportChatInviteRequest(message.message.forward.chat_id))).link

    forward_message_text = message.message.text
    chat_from_forward = message.message.forward.chat.title
    # аналол?
    # new_link = bot.export_chat_invite_link(message.forward_from_chat.id)
    # await bot.send_message(message.chat.id, new_link)

    title_from_forward = message.message.forward.chat_id

    # bot.send_message(message.chat.id, message.forward_from_chat.id, parse_mode='html', disable_web_page_preview=True)
    # user = []

    conn = await user_info.create_connection()
    while (True):
        try:
            user = await user_info.find_user(conn, message.chat_id, title_from_forward, 3)
        except NameError:
            await user_info.add_user(conn, message.chat_id, title_from_forward, chat_from_forward, 100, '', '',
                                     new_link, 0, 1, 0, '')
        except Exception:
            await user_info.add_user(conn, message.chat_id, title_from_forward, chat_from_forward, 100, '', '',
                                     new_link, 0, 0, 0, '')
            await bot.send_message(message.chat_id, 'Данные о вашем канале успешно добавлены', parse_mode='html',
                                   link_preview=False)

    await user_info.close_connection(conn)


# @dp.message_handler(content_types=['document'])
# def start_message(document):
#    bot.send_message(document.chat.id, document)


# фото делаем
@bot.on(events.NewMessage(func=lambda e: e.is_private and getattr(e, 'photo')))
async def photo_detect(event):  # Водяной знак p=5
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    photo = event
    channel = sender.id  # 275965108
    entity = await bot.get_entity(channel)
    # await bot.send_message(entity=entity, file=photo, message=name)
    photo_id = photo.message.photo.id

    f = tempfile.NamedTemporaryFile(delete=False)
    Input_file = photo
    f.write(await event.download_media(bytes))
    f.close()

    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, channel, '', 1)
    await user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8], photo_id, f.name)
    await user_info.close_connection(conn)

    await bot.send_message(channel, 'Водяной знак нужен и картинка Вам принадлежит?', buttons=[
        KeyboardButtonCallback(text="Да", data=b"wmp_y"),
        KeyboardButtonCallback(text="Нет", data=b"wmp_n"),
    ])


@bot.on(events.CallbackQuery)
async def photo_ex(event):
    callbtn = event.data
    sender = await event.get_sender()
    # name = utils.get_display_name(sender)
    channel = sender.id
    id_message = event.message_id
    if callbtn == b"iv_yes":  # инстан вью

        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, channel, '', 1)

        telo = '<a href="' + u[4] + '">.</a>' + u[5]  # исправить 11111

        # bot.delete_message(message.chat.id, message_keyb_IV.message_id)
        await bot.send_message(channel,'<b>' + u[2] + '</b>' + '\n\n' + telo, parse_mode='html', link_preview=True)

        vkanal = telo + '\n'

        await user_info.update_user(conn, u[0], u[1], u[2], 22, vkanal, '', u[6], u[7], u[8], U[9], '')
        await user_info.close_connection(conn)

    elif callbtn == b"iv_no":

        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, channel, '', 1)

        telo = u[5] + '\n' + '<a href="' + u[4] + '">Читать далее...</a>'

        # bot.delete_message(message.chat.id, message_keyb_IV.message_id)

        await bot.send_message(channel,'<b>' + u[2] + '</b>' + '\n\n' + telo, parse_mode='html', link_preview=False)

        u = await user_info.find_user(conn, message.chat.id, '', 1)
        await user_info.update_user(conn, u[0], u[1], u[2], 10, vkanal, '', u[6], u[7], u[8], U[9], '')
        await user_info.close_connection(conn)

    if callbtn == b"sel_c":  # выбрать канал

        # await call.message.delete()
        await bot.delete_messages(channel, id_message)
        conn = await user_info.create_connection()
        etud = await user_info.find_user(conn, channel, '', 2)
        chaname = await user_info.Name_ch_(etud)
        await user_info.close_connection(conn)

        # help_v = await inl_keyb6(chaname[0], chaname[1], chaname[2], chaname[3], chaname[4], chaname[5], 'hvc')

        hlp_v = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[0], data=b"c1"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[1], data=b"c2"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[2], data=b"c3"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[3], data=b"c4"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[4], data=b"c5"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[5], data=b"c6"), ]),

            ]
        )
        await bot.send_message(channel, 'канал?', buttons=hlp_v)  # 444444

    if callbtn == b"c1":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 0, 1)

    if callbtn == b"c2":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 1, 1)

    if callbtn == b"c3":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 2, 1)

    if callbtn == b"c4":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 3, 1)

    if callbtn == b"c5":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 4, 1)

    if callbtn == b"c6":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 5, 1)

    # if callbtn == b"add_c": #  добавить канал
    #     await bot.delete_messages(channel, id_message)
    #     conn = await user_info.create_connection()
    #     etud = await user_info.find_user(conn, channel, '', 2)
    #     chaname = await user_info.Name_ch_(etud)
    #     await user_info.close_connection(conn)

    if callbtn == b"del_c":  # удалить канал
        await bot.delete_messages(channel, id_message)
        conn = await user_info.create_connection()
        etud = await user_info.find_user(conn, channel, '', 2)
        chaname = await user_info.Name_ch_(etud)
        await user_info.close_connection(conn)
        hlp_del = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[0], data=b"d1"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[1], data=b"d2"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[2], data=b"d3"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[3], data=b"d4"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[4], data=b"d5"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[5], data=b"d6"), ]),

            ]
        )
        await bot.send_message(channel, 'канал?', buttons=hlp_del)  # 444444

    if callbtn == b"d1":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 0, 2)

    if callbtn == b"d2":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 1, 2)

    if callbtn == b"d3":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 2, 2)

    if callbtn == b"d4":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 3, 2)

    if callbtn == b"d5":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 4, 2)

    if callbtn == b"d6":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 5, 2)

    if callbtn == b"otval":  # выйти из меню работы с каналами
        await bot.delete_messages(channel, id_message)

    if callbtn == b'wmp_y':
        # Водяной знак p=5
        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, channel, '', 1)
        await user_info.close_connection(conn)

        # bot.delete_message(chat_id, message_id_Photo)
        # bot.delete_message(chat_id, message_keyb_WM.message_id)

        photo = Image.open(u[10])
        width, height = photo.size
        drawing = ImageDraw.Draw(photo)
        black = (240, 8, 12)
        font = ImageFont.truetype(cfg.user_font, width // 20)
        pos = (width // 2, height - height // 10)
        text = u[2]
        drawing.text(pos, text, fill=black, font=font)
        pos = (1 + width // 2, 1 + height - height // 10)
        drawing.text(pos, text, fill=black, font=font)
        pos = (2 + width // 2, 2 + height - height // 10)
        drawing.text(pos, text, fill=black, font=font)
        photo_path = f'{u[10]}.jpeg'
        photo.save(photo_path, 'JPEG')
        # bot.send_chat_action(message.chat.id, action='upload_photo')

        with open(photo_path, 'rb') as fi:
            info = await bot.send_file(u[0], fi)

        os.remove(u[10])
        # os.remove(photo_path)

        fip = info.photo.id

        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, u[0], '', 1)
        await user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8], fip, photo_path)
        await user_info.close_connection(conn)

    if callbtn == b'wmp_n':
        # решить, что делать
        r = 1

    if callbtn == b'wv_y':  # Видео
        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, channel, '', 1)
        user_info.update_user(conn, u[0], u[1], u[2], 7, u[4], u[5], u[6], 2, u[8], u[9], '')
        await user_info.close_connection(conn)

        text = u[2]
        my_clip = VideoFileClip(u[10], audio=True)  # Видео файл с включенным аудио
        clip_duration = my_clip.duration  # длительность ролика

        w, h = my_clip.size  # размер клипа
        # Клип с текстом и прозрачным фоном

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

        video_path = f'{u[10]}.mp4'

        # final.write_videofile(video_path, fps=24, codec='libx264')
        final.write_videofile(video_path, fps=24, codec='mpeg4')

        with open(video_path, 'rb') as fi:
            info_video = await bot.send_file(u[0], fi, supports_streaming=True, force_document=True)

        os.remove(u[10])
        os.remove(video_path)

        fip = info_video.video.id

        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, u[0], '', 1)
        await user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8], fip, '')
        await user_info.close_connection(conn)

    if callbtn == b'wv_n':
        r = 1


# видео делаем
@bot.on(events.NewMessage(func=lambda e: e.is_private and getattr(e, 'video')))
async def video_detect(event):
    sender = await event.get_sender()
    channel = sender.id

    f = tempfile.NamedTemporaryFile(delete=False)

    f.write(await event.download_media(bytes))
    f.close()

    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, channel, '', 1)
    await user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8], u[9], f.name)
    await user_info.close_connection(conn)

    await bot.send_message(channel, 'Бегущая строка нужна и видео Вам принадлежит?', buttons=[
        KeyboardButtonCallback(text="Да", data=b"wv_y"),
        KeyboardButtonCallback(text="Нет", data=b"wv_n"),
    ])


# events.NewMessage(forwards='false')
@bot.on(events.NewMessage(func=lambda e: e.is_private and getattr(e, 'text')))
async def text_detect(event):
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    channel = sender.id
    id_message = event.message.id
    # entity = await bot.get_entity(channel)
    text_e = event.message.text
    id_user = event.message.to_id.user_id

    if text_e == 'News':
        await user_info.add_hashtag(event, 'news')

    elif text_e == 'Hands':  # Своми руками
        await user_info.add_hashtag(event, 'hands')

    elif text_e == 'Think':  # Подумай
        await user_info.add_hashtag(event, 'think')

    elif text_e == 'Stolen':  # Украдено
        await user_info.add_hashtag(event, 'stolen')

    elif text_e == 'ADS':  # Реклама
        await user_info.add_hashtag(event, 'ads')

    elif text_e == 'Sight':  # Мнение
        await user_info.add_hashtag(event, 'sight')

    elif text_e == 'Humor':  # Юмор
        await user_info.add_hashtag(event, 'humor')

    elif text_e == 'Comb':

        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, channel, '', 1)

        await bot.delete_messages(channel, id_message)  # удаляю слово Комб

        if u[7] > 0:

            # if message.message_id - 1:
            # await bot.delete_message(channel, id_message - 1)  # удаляю сообщение для комб

            if u[3] == 10 or u[3] == 9:
                telo = u[4]

            if u[7] == 1:  # mm == 1  photo

                photo = Image.open(u[10])
                photo_path = f'{u[10]}.jpeg'
                photo.save(photo_path, 'JPEG')
                with open(photo_path, 'rb') as fi:
                    info = await bot.send_file(u[0], fi, caption='<b>' + u[2] + '</b>' + '\n\n' + u[5],
                                               parse_mode='html')


            elif u[7] == 2:  # mm == 2  video .file_id   # 123

                await bot.send_video(u[0], u[10], caption=u[5], parse_mode='html')

            await user_info.update_user(conn, u[0], u[1], u[2], 11, telo, u[5], u[6], u[7], u[8], u[9], u[10])

        else:
            await bot.send_message(message.chat.id, 'Нет медиафайла!', parse_mode='html', disable_web_page_preview=True,
                                   reply_markup=markup)

        await user_info.close_connection(conn)


    elif text_e == 'Help':  # Помощь
        # await user_info.help_bl_as(event)

        await bot.send_message(channel, bl_as_modul.HSK, parse_mode='html', link_preview=False)

        # while (True):

        try:
            conn = await create_connection()
            u = await user_info.find_user(conn, channel, '', 1)  # а если всего один
            await user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], u[9], u[10])
            await user_info.close_connection(conn)
        except Exception:
            await bot.send_message(channel, 'У вас нет рабочего канала, выберете его', parse_mode='html',
                                   link_preview=False)

        #  тут
        hlp_but = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Выбрать канал", data=b"sel_c"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Удалить канал", data=b"del_c"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Выйти из меню", data=b"otval"), ]),
            ]
        )
        # KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Добавить канал", data=b"add_c"), ]),

        await bot.send_message(channel, 'Выберите необходимое действие', buttons=hlp_but)

    elif text_e == 'Send':  # Отправка в канал
        #  НЕ ОТПРАВЛЯЕТ ПОСЛЕ КОМБ ПОЧЕМУ ТО
        #  видео с каментом    pkanal = 11 mm=2
        #  Водяной знак        pkanal = 5     u[3]
        #  Работа со ссылками  pkanal = 6
        #  Картинка с каментом pkanal = 11 mm=1
        #  instant view        pkanal = 22
        #  просто сообщение    pkanal = 9
        # bot.delete_message(message.chat.id, message.message_id)
        await bot.delete_messages(channel, id_message)

        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, channel, '', 1)

        if u[3] == 5 or u[3] == 6 or u[3] == 100:
            await bot.send_message(channel, 'Пустые сообщения не отправляются в канал', parse_mode='html',
                                   link_preview=False)
        else:

            # bot.send_message(message.chat.id, skanal, parse_mode='html', disable_web_page_preview=True)
            # bot.send_message(message.chat.id, chat_id, parse_mode='html', disable_web_page_preview=True)

            # if message.from_user.id in [adm_obj.user.id for adm_obj in bot.get_chat_administrators(chat_id)]:  # Важно, можно ли отправлять в канал
            # permissions = await bot.ChatMethods.get_permissions(u[1], id_user)
            # if permissions.is_admin:
            # do something

            if u[0] > 0:
                if u[3] == 9 or u[3] == 10:
                    await bot.send_message(u[1] * (-1), u[4], parse_mode='html', link_preview=False)

                    # bot.send_message(chat_id, u[4], parse_mode='html', disable_web_page_preview=True)
                elif u[3] == 11:  # Картинка или видео с каментом
                    if u[7] == 2:
                        await bot.send_video(u[1] * (-1), file_info_video.file_id, caption=u[5],
                                             parse_mode='html')  # 123
                    else:
                        await bot.send_file(u[1], u[10], caption=u[5], parse_mode='html')
                elif u[3] == 22:
                    bot.send_message(chat_id, u[4], parse_mode='html', disable_web_page_preview=False)
                else:
                    await bot.send_message(u[1] * (-1), u[4], parse_mode='html', link_preview=False)

                await user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], u[9], '')


            else:
                await bot.send_message(u[0], 'Вы не являетесь Администратором канала', parse_mode='html',
                                       link_preview=False)

        await user_info.close_connection(conn)


    # elif message.entities:  # Работа со ссылками pkanal = 6  6666666
    elif text_e.find('://') > 0:

        if text_e.find(' ') == -1:

            if 'youtube.com' in text_e or 'youtu.be' in text_e or 'ok.ru' in text_e:  # Загружаем с Ютуб

                link_of_the_video = text_e
                # await message.delete()

                f = tempfile.NamedTemporaryFile(delete=False)
                video_path_out = f'{f.name}.mkv'  # .mkv
                video_path = f.name
                video_path_out_mp4 = f'{f.name}.mp4'

                ydl_opts = {'outtmpl': video_path,
                            'merge_output_format': 'mkv',
                            'noplaylist': 'true',
                            'ignoreerrors': 'true',
                            'quiet': True,
                            'max_filesize': 120000000,
                            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                            'filename': video_path_out}

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    video_path = ydl.download([link_of_the_video])

                # message.reply('Закончили Ютуб ', parse_mode='html',disable_web_page_preview=True)

                # info_video = bot.send_video(message.chat.id, video_path)

                if not os.path.exists(video_path_out) == 0:  # файл есть   if os.path.exists('/tmp/f.mp4'):

                    video = VideoFileClip(video_path_out)  # mkv --> mp4
                    result = CompositeVideoClip([video])
                    result.write_videofile(video_path_out_mp4, fps=24, codec='mpeg4')

                    with open(video_path_out_mp4, 'rb') as fi:
                        # info_video = bot.send_video(message.chat.id, fi)
                        # info_video = await message.answer_video(video=fi)

                        info_video = await bot.send_file(channel, fi)

                    # info_video = bot.send_video(message.chat.id, video_path_out_mp4)

                    os.remove(f.name)
                    os.remove(video_path_out)
                    os.remove(video_path_out_mp4)

                    conn = await user_info.create_connection()
                    u = await user_info.find_user(conn, channel, '', 1)
                    await user_info.update_user(conn, u[0], u[1], u[2], 6, u[4], u[5], u[6], 2, u[8], u[9], '')
                    await user_info.close_connection(conn)

                    # file_info_video = bot.get_file(info_video.video.file_id)

                else:  # файла нет
                    # bot.delete_message(message.chat.id, gif.message_id)
                    message.reply(
                        'Слишком большой файл для загрузки,' + "<a href='https://t.me/joinchat/EHLktEzzYJXpERD7UgaHFQ'> пишите мне в чат </a>" + 'какие варианты интересны',
                        parse_mode='html', disable_web_page_preview=True)
                    # предложить  сделать ссылку  на ролик

                    conn = await user_info.create_connection()
                    u = await user_info.find_user(conn, message.chat.id, '', 1)
                    await user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], u[9], '')
                    await user_info.close_connection(conn)


            else:  # Читать далее

                conn = await user_info.create_connection()
                u = await user_info.find_user(conn, channel, '', 1)
                if u[3] == 10:
                    # telo = vkanal
                    await user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], u[4], u[6], 0, u[8], u[9], '')
                    await user_info.close_connection(conn)
                else:
                    await user_info.update_user(conn, u[0], u[1], u[2], u[3], text_e, u[5], u[6], 0, u[8], u[9], '')
                    await user_info.close_connection(conn)


                    # режим instant view 111111  555555

                chat_id = channel
                # message_id_Telo = message.message.id

                await bot.send_message(channel, 'Нужен режим instant view?', buttons=[
                    KeyboardButtonCallback(text="Да", data=b"iv_yes"),
                    KeyboardButtonCallback(text="Нет", data=b"iv_no"),
                ])

                conn = await user_info.create_connection()
                u = await user_info.find_user(conn, channel, '', 1)
                await user_info.update_user(conn, u[0], u[1], u[2], u[3], text_e, u[5], u[6], u[7], u[8], U[9], u[10])
                await user_info.close_connection(conn)



        else:  # В сообщении присутствует ссылка, но это сообщение в канал

            telo = text_e + '\n'  # Просто текст

            #  Обрабатываем выделение жирным, нет проверки на ошибку
            #  надо переписать это на str.find(), вместо index()
            #  и разобраться с парностью
            if round(telo.count('ьь') / 2) - telo.count('ьь') / 2 == 0.5 or telo.count('ьь') == 1:
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

            conn = await user_info.create_connection()
            u = await user_info.find_user(conn, message.chat.id, '', 1)
            await user_info.update_user(conn, u[0], u[1], u[2], 9, u[4], telo, u[6], u[7], u[8], u[9], '')
            await user_info.close_connection(conn)

    else:  # Просто текст
        await user_info.just_text(event)


if __name__ == '__main__':
    bot.run_until_disconnected()
