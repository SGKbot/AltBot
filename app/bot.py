# -*- coding: utf-8 -*-
from telethon.events import StopPropagation
from telethon.sync import events, utils

from telethon.tl.custom.message import Message
from telethon.client.messages import MessageMethods

from telethon.tl import types
from telethon.tl.types import (
    KeyboardButtonRow,
    KeyboardButtonCallback,
)

from telethon.tl.functions.messages import ExportChatInviteRequest

from telethon import TelegramClient, events, Button
from datetime import date, datetime
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

import re
import tempfile
import youtube_dl

import bl_as_modul
import user_info
import cfg
import sl_tm

from user_info import create_connection

bot = bl_as_modul.client

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from moviepy.editor import *

import sched_send_delete
from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler()
#  scheduler.add_job(sched_send_delete.exampl_send, "interval", seconds=5)
scheduler.add_job(sched_send_delete.exampl_send, "cron", minute='0,5,10,15,20,25,30,35,40,45,50,55')
scheduler.start()

pv = 0
info = ''
info_video = ''


@bot.on(events.NewMessage(pattern='/start'))
async def start_message(message):
    await bot.send_message(message.chat_id, bl_as_modul.HS, parse_mode='html', link_preview=False, buttons=bl_as_modul.Main_menu_btn)
    await bot.send_message(message.chat_id, cfg.Pr, parse_mode='html', link_preview=False)
    raise StopPropagation



@bot.on(events.CallbackQuery(data=b"snd_s"))  # выбор метода отправки сообщения отложить
async def sel_send(event):
    await user_info.snd_feature_choice(event, 'sch')  # ставим признак выбора
    await user_info.run_dt(event)  # запуск выбора времени даты




@bot.on(events.CallbackQuery(data=b"snd_sd"))  # выбор метода отправки сообщения отложить и удалить
async def sel_send(event):
    await user_info.snd_feature_choice(event, 'schdel')  # ставим признак выбора
    await event.edit("отложить и удалить")

    await user_info.run_dt(event)  # отложить, del  придумать


@bot.on(events.CallbackQuery(data=b"snd_i"))  # выбор метода отправки сообщения Immediately
async def sel_send(event):
    await user_info.snd_feature_choice(event, 'imm')  # ставим признак выбора
    await user_info.snd_chl_i(event)
    await user_info.snd_clear_info_cnl(event)  # чистим строку информации о канале


@bot.on(events.CallbackQuery(data=b"snd_id"))  # выбор метода отправки сообщения мнговенно и удалить
async def sel_send(event):
    await user_info.snd_feature_choice(event, 'delimm')  # ставим признак выбора

    await event.edit("мнговенно и удалить")

    await user_info.run_dt(event)



@bot.on(events.CallbackQuery(pattern=re.compile(b"time")))
async def sel_time(event):
    await sl_tm.sl_time(event)


@bot.on(events.CallbackQuery(pattern=DetailedTelegramCalendar.func(telethon=True)))
async def calendar_handler(event):
    result, key, step = DetailedTelegramCalendar(telethon=True, min_date=date.today()).process(event.data.decode("utf-8"))

    if not result and key:
        await event.edit(f"Select {LSTEP[step]}", buttons=key)
    elif result:
        # await event.edit(f"You selected {result}")
        await sl_tm.dmy(result, event)
        await event.edit(' Введите время', buttons=sl_tm.tempAM_but)


@bot.on(events.NewMessage(forwards='true'))
async def send_text(message):
    new_link = (await bot(ExportChatInviteRequest(message.message.forward.chat_id))).link
    chat_from_forward = message.message.forward.chat.title
    title_from_forward = message.message.forward.chat_id

    conn = await user_info.create_connection()
    while (True):
        try:
            user = await user_info.find_user(conn, message.chat_id, title_from_forward, 3)
        except NameError:
            await user_info.add_user(conn, message.chat_id, title_from_forward, chat_from_forward, 100, '', '',
                                     new_link, 0, 1, 0, '', '', 0)
        except Exception:
            await user_info.add_user(conn, message.chat_id, title_from_forward, chat_from_forward, 100, '', '',
                                     new_link, 0, 0, 0, '', '', 0)
            await bot.send_message(message.chat_id, 'Данные о вашем канале успешно добавлены', parse_mode='html',
                                   link_preview=False)

    await user_info.close_connection(conn)


@bot.on(events.NewMessage(func=lambda e: e.is_private and getattr(e, 'photo')))  # фото делаем
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
    await user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8], photo_id, f.name, u[11], u[12])
    await user_info.close_connection(conn)
    await bot.send_message(channel, 'Водяной знак нужен и картинка Вам принадлежит?', buttons=[
        KeyboardButtonCallback(text="Да", data=b"wmp_y"),
        KeyboardButtonCallback(text="Нет", data=b"wmp_n"),
    ])

@bot.on(events.CallbackQuery(pattern=re.compile(b"iv_")))  # инстан вью
async def ins_v(event):
    sender = await event.get_sender()
    channel = sender.id
    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, channel, '', 1)
    if event.data == b"iv_yes":
        telo = '<a href="' + u[4] + '">.</a>' + u[5]  # исправить 11111
        await bot.send_message(channel, '<b>' + u[2] + '</b>' + '\n\n' + telo, parse_mode='html', link_preview=True)
        vkanal = telo + '\n'
        await user_info.update_user(conn, u[0], u[1], u[2], 22, vkanal, '', u[6], u[7], u[8], u[9], '', u[11], u[12])
        await user_info.close_connection(conn)
    elif event.data == b"iv_no":
        telo = u[5] + '\n' + '<a href="' + u[4] + '">Читать далее...</a>'
        await bot.send_message(channel, '<b>' + u[2] + '</b>' + '\n\n' + telo, parse_mode='html', link_preview=False)
        u = await user_info.find_user(conn, channel, '', 1)
        await user_info.update_user(conn, u[0], u[1], u[2], 10, telo, '', u[6], u[7], u[8], u[9], '', u[11], u[12])
        await user_info.close_connection(conn)


@bot.on(events.CallbackQuery(pattern=re.compile(b"wv_")))  # видео
async def treatment_video(event):
    sender = await event.get_sender()
    channel = sender.id
    if event.data == b'wv_y':
        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, channel, '', 1)
        await user_info.update_user(conn, u[0], u[1], u[2], 7, u[4], u[5], u[6], 2, u[8], u[9], u[10], u[11], u[12])
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
        final.write_videofile(video_path, fps=24, codec='mpeg4')
        with open(video_path, 'rb') as fi:
            info_video = await bot.send_file(u[0], fi, supports_streaming=True, force_document=True)
        os.remove(u[10])
        # os.remove(video_path)
        fip = info_video.id
        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, u[0], '', 1)
        await user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 2, u[8], fip, video_path, u[11], u[12])
        await user_info.close_connection(conn)
    if event.data == b'wv_n':
        r = 1


@bot.on(events.CallbackQuery(pattern=re.compile(b"wrkch")))
async def photo_ex(event):
    callbtn = event.data
    sender = await event.get_sender()
    # name = utils.get_display_name(sender)
    channel = sender.id
    id_message = event.message_id

    if callbtn == b"wrkchsel_c":  # выбрать канал

        # await call.message.delete()
        await bot.delete_messages(channel, id_message)
        conn = await user_info.create_connection()
        etud = await user_info.find_user(conn, channel, '', 2)
        chaname = await user_info.Name_ch_(etud)
        await user_info.close_connection(conn)
        hlp_v = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[0], data=b"wrkchc1"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[1], data=b"wrkchc2"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[2], data=b"wrkchc3"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[3], data=b"wrkchc4"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[4], data=b"wrkchc5"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[5], data=b"wrkchc6"), ]),

            ]
        )
        await bot.send_message(channel, 'канал?', buttons=hlp_v)  # 444444

    if callbtn == b"wrkchc1":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 0, 1)
    if callbtn == b"wrkchc2":  # выбираем 2 канал
        await user_info.sel_chan(channel, id_message, 1, 1)
    if callbtn == b"wrkchc3":  # выбираем 3 канал
        await user_info.sel_chan(channel, id_message, 2, 1)
    if callbtn == b"wrkchc4":  # выбираем 4 канал
        await user_info.sel_chan(channel, id_message, 3, 1)
    if callbtn == b"wrkchc5":  # выбираем 5 канал
        await user_info.sel_chan(channel, id_message, 4, 1)
    if callbtn == b"wrkchc6":  # выбираем 6 канал
        await user_info.sel_chan(channel, id_message, 5, 1)

    # if callbtn == b"add_c": #  добавить канал
    #     await bot.delete_messages(channel, id_message)
    #     conn = await user_info.create_connection()
    #     etud = await user_info.find_user(conn, channel, '', 2)
    #     chaname = await user_info.Name_ch_(etud)
    #     await user_info.close_connection(conn)

    if callbtn == b"wrkchdel_c":  # удалить канал
        await bot.delete_messages(channel, id_message)
        conn = await user_info.create_connection()
        etud = await user_info.find_user(conn, channel, '', 2)
        chaname = await user_info.Name_ch_(etud)
        await user_info.close_connection(conn)
        hlp_del = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[0], data=b"wrkchd1"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[1], data=b"wrkchd2"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[2], data=b"wrkchd3"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[3], data=b"wrkchd4"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[4], data=b"wrkchd5"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=chaname[5], data=b"wrkchd6"), ]),

            ]
        )
        await bot.send_message(channel, 'канал?', buttons=hlp_del)  # 444444

    if callbtn == b"wrkchd1":  # выбираем 1 канал
        await user_info.sel_chan(channel, id_message, 0, 2)
    if callbtn == b"wrkchd2":  # выбираем 2 канал
        await user_info.sel_chan(channel, id_message, 1, 2)
    if callbtn == b"wrkchd3":  # выбираем 3 канал
        await user_info.sel_chan(channel, id_message, 2, 2)
    if callbtn == b"wrkchd4":  # выбираем 4 канал
        await user_info.sel_chan(channel, id_message, 3, 2)
    if callbtn == b"wrkchd5":  # выбираем 5 канал
        await user_info.sel_chan(channel, id_message, 4, 2)
    if callbtn == b"wrkchd6":  # выбираем 6 канал
        await user_info.sel_chan(channel, id_message, 5, 2)
    if callbtn == b"wrkchotval":  # выйти из меню работы с каналами
        await bot.delete_messages(channel, id_message)

@bot.on(events.CallbackQuery(pattern=re.compile(b"wmp_")))  # видео
async def treatment_video(event):
    sender = await event.get_sender()
    channel = sender.id
    if event.data == b'wmp_y':
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
        await user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8], fip, photo_path, u[11], u[12])
        await user_info.close_connection(conn)
    if event.data == b'wmp_n':
        # решить, что делать
        r = 1

@bot.on(events.NewMessage(func=lambda e: e.is_private and getattr(e, 'video')))  # видео делаем
async def video_detect(event):
    sender = await event.get_sender()
    channel = sender.id
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(await event.download_media(bytes))
    f.close()

    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, channel, '', 1)
    await user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 2, u[8], u[9], f.name, u[11], u[12])
    await user_info.close_connection(conn)

    await bot.send_message(channel, 'Бегущая строка нужна и видео Вам принадлежит?', buttons=[
        KeyboardButtonCallback(text="Да", data=b"wv_y"),
        KeyboardButtonCallback(text="Нет", data=b"wv_n"),
    ])


@bot.on(events.CallbackQuery(pattern=re.compile(b"hsht_")))  # hashteg
async def hashteg_w(event):
    if event.data == b'hsht_n':
        await user_info.add_hashtag(event, 'news')
    elif event.data == b'hsht_h':
        await user_info.add_hashtag(event, 'hands')
    elif event.data == b'hsht_t':
        await user_info.add_hashtag(event, 'think')
    elif event.data == b'hsht_s':
        await user_info.add_hashtag(event, 'stolen')
    elif event.data == b'hsht_a':
        await user_info.add_hashtag(event, 'ads')
    elif event.data == b'hsht_s':
        await user_info.add_hashtag(event, 'sight')
    elif event.data == b'hsht_hum':
        await user_info.add_hashtag(event, 'humor')


@bot.on(events.CallbackQuery(pattern=re.compile(b"tools_")))  # tools
async def tools_w(event):
    sender = await event.get_sender()
    channel = sender.id
    await bot.delete_messages(channel, event.original_update.msg_id)
    if event.data == b'tools_ch':

        await bot.send_message(channel, 'Выберите необходимое действие', buttons=bl_as_modul.hlp_but)
    elif event.data == b'tools_but':
        pkanal = 2000  # признак что кнопка
        conn = await create_connection()
        u = await user_info.find_user(conn, channel, '', 1)  # а если всего один
        pkanal=pkanal+u[3]
        await user_info.update_user(conn, u[0], u[1], u[2], pkanal, '', u[5], u[6], u[7], u[8], u[9], u[10], u[11], u[12])
        await user_info.close_connection(conn)

        await bot.send_message(channel, 'отправте до 3_х кнопок в виде' +
                               '\n' + 'ТЕКСТ КНОПКИ Url' +
                               '\n' + 'ТЕКСТ КНОПКИ Url' +
                               '\n' + 'ТЕКСТ КНОПКИ Url')


    elif event.data == b'tools_cmb':
        await user_info.combo_f(event)


@bot.on(events.NewMessage(func=lambda e: e.is_private and getattr(e, 'text')))
async def text_detect(event):
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    channel = sender.id
    text_e = event.message.text
    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, channel, '', 1)
    await user_info.close_connection(conn)

    if text_e == 'hashtag':
        await bot.send_message(channel, 'Выберите hashtag', buttons=bl_as_modul.hsht_but)
    elif text_e == 'Tools':
        m = await bot.send_message(channel, 'Tools', buttons=bl_as_modul.tools_but)
        await bot.delete_messages(channel, m.id - 1)   # 11111111111
    elif text_e == 'Help':  # Помощь
        await bot.send_message(channel, bl_as_modul.HSK, parse_mode='html', link_preview=False)
        try:
            conn = await create_connection()
            u = await user_info.find_user(conn, channel, '', 1)  # а если всего один
            await user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], u[7], u[8], u[9], u[10], u[11], u[12])
            await user_info.close_connection(conn)
        except Exception:
            await bot.send_message(channel, 'У вас нет рабочего канала, выберете его', parse_mode='html',
                                   link_preview=False)
    elif text_e == 'Send':  # Отправка в канал
        #  НЕ ОТПРАВЛЯЕТ ПОСЛЕ КОМБ ПОЧЕМУ ТО
        #  видео с каментом    pkanal = 11 mm=2
        #  Водяной знак        pkanal = 5     u[3]
        #  Работа со ссылками  pkanal = 6
        #  Картинка с каментом pkanal = 11 mm=1
        #  instant view        pkanal = 22
        #  просто сообщение    pkanal = 9
        # bot.delete_message(message.chat.id, message.message_id)
        #  await bot.delete_messages(channel, id_message)

        conn = await user_info.create_connection()
        u = await user_info.find_user(conn, channel, '', 1)
        await user_info.close_connection(conn)
        if u[3] == 5 or u[3] == 6 or u[3] == 100:
            await bot.send_message(channel, 'Пустые сообщения не отправляются в канал', parse_mode='html',
                                   link_preview=False)

        else:  # Выбираем стиль отправки

            snd_but = types.ReplyInlineMarkup(
                rows=[
                    KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Schedule", data=b"snd_s")]),
                    KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Schedule & Delete", data=b"snd_sd"), ]),
                    KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Immediately", data=b"snd_i"), ]),
                    KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Immediately & Delete", data=b"snd_id"), ]),
                ]
            )

            await bot.send_message(channel, 'Выберите необходимое действие', buttons=snd_but)


    elif text_e.find('://') > 0: # Работа со ссылками pkanal = 6  6666666

        if text_e.find(' ') == -1:
            if ('youtube.com' in text_e or 'youtu.be' in text_e or 'ok.ru' in text_e) and (u[3]//100 != 20):  # Загружаем с Ютуб
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

                if not os.path.exists(video_path_out) == 0:  # файл есть   if os.path.exists('/tmp/f.mp4'):
                    video = VideoFileClip(video_path_out)  # mkv --> mp4
                    result = CompositeVideoClip([video])
                    result.write_videofile(video_path_out_mp4, fps=24, codec='mpeg4')

                    with open(video_path_out_mp4, 'rb') as fi:

                        info_video = await bot.send_file(channel, fi)

                    # info_video = bot.send_video(message.chat.id, video_path_out_mp4)

                    os.remove(f.name)
                    os.remove(video_path_out)
                    os.remove(video_path_out_mp4)

                    conn = await user_info.create_connection()
                    u = await user_info.find_user(conn, channel, '', 1)
                    await user_info.update_user(conn, u[0], u[1], u[2], 6, u[4], u[5], u[6], 2, u[8], info_video.id,
                                                video_path, u[11], u[12])
                    await user_info.close_connection(conn)

                    # file_info_video = bot.get_file(info_video.video.file_id)

                else:  # файла нет
                    # bot.delete_message(message.chat.id, gif.message_id)
                    await bot.send_message(channel, 'Слишком большой файл для загрузки,' + "<a href='https://t.me/joinchat/EHLktEzzYJXpERD7UgaHFQ'> пишите мне в чат </a>" + 'какие варианты интересны', parse_mode='html')
                    # предложить  сделать ссылку  на ролик

                    conn = await user_info.create_connection()
                    u = await user_info.find_user(conn, channel, '', 1)
                    await user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], u[9], '', u[11], u[12])
                    await user_info.close_connection(conn)

            else:  # Читать далее

                conn = await user_info.create_connection()
                u = await user_info.find_user(conn, channel, '', 1)

                if u[3] == 10:
                    # telo = vkanal
                    await user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], u[4], u[6], u[7], u[8], u[9], u[10],
                                                u[11], u[12])
                    await user_info.close_connection(conn)
                else:
                    await user_info.update_user(conn, u[0], u[1], u[2], u[3], text_e, u[5], u[6], u[7], u[8], u[9],
                                                u[10], u[11], u[12])
                    await user_info.close_connection(conn)

                await bot.send_message(channel, 'Нужен режим instant view?', buttons=[
                    KeyboardButtonCallback(text="Да", data=b"iv_yes"),
                    KeyboardButtonCallback(text="Нет", data=b"iv_no"),
                                                                                      ])
                conn = await user_info.create_connection()
                u = await user_info.find_user(conn, channel, '', 1)
                await user_info.update_user(conn, u[0], u[1], u[2], u[3], text_e, u[5], u[6], u[7], u[8], u[9], u[10],
                                            u[11], u[12])
                await user_info.close_connection(conn)

        else:  # В сообщении присутствует ссылка, но это сообщение в канал

            telo = text_e  #  + '\n'  # Просто текст

            #  Обрабатываем выделение жирным,
            #  надо переписать это на str.find(), вместо index()

            if round(telo.count('ьь') / 2) - telo.count('ьь') / 2 == 0.5 or telo.count('ьь') == 1:
                bot.send_message(channel, 'Вы неправильно оформили выделение жирным шрифтом',
                                 parse_mode='html', disable_web_page_preview=True)
            else:
                while (True):
                    try:
                        index = telo.index('ьь')
                        telo = telo[:index] + '<b>' + telo[index + 2:]
                        index = telo.index('ьь', index)
                        telo = telo[:index] + '</b>' + telo[index + 2:]
                        conn = await user_info.create_connection()  # убрать в каждый раздел!!!!!
                        u = await user_info.find_user(conn, channel, '', 1)
                        await user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], telo, u[6], u[7], u[8], u[9],
                                                    u[10], u[11], u[12])
                        await user_info.close_connection(conn)

                    except ValueError:
                        break

            if round(telo.count('===') / 2) - telo.count('===') / 2 == 0.5 or telo.count('===') == 1:
                bot.send_message(channel, 'Вы неправильно оформили кнопку',
                                 parse_mode='html', disable_web_page_preview=True)
            else:
                if telo.find('===') > 0:
                    while (True):
                        try:
                            x1 = telo[:(telo.index('==='))]
                            x2 = telo[(telo.rindex('===') + 3):]  # ссылка
                            x3 = telo[(telo.index('===')+3): (telo.rindex('==='))]  # кнопка
                            msg = await bot.send_message(channel, x1, parse_mode='html', link_preview=False,
                                                         buttons=[
                                                             [Button.inline(''), Button.inline('')],
                                                             [Button.url(x3, x2.strip())]
                                                                 ])

                            conn = await user_info.create_connection()
                            u = await user_info.find_user(conn, channel, '', 1)
                            await user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], x1, u[6], u[7], u[8], u[9],
                                                        u[10], x3 + ' ' + x2, u[12])
                            await user_info.close_connection(conn)

                            break
                        except ValueError:
                            break

            if u[3]//100 == 20:  # кнопка из меню

                x2, x3, x4, x5, x6, x7 = await user_info.processing_button_data(telo)

                if not u[5]:  # для отладки
                    otl = '<>'
                else:
                    otl = u[5]

                msg = await bot.send_message(channel, otl, parse_mode='html', link_preview=False,
                                             buttons=[
                                                 [Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                                                 [Button.url(x3, x2.strip())]
                                             ])
                conn = await user_info.create_connection()
                u = await user_info.find_user(conn, channel, '', 1)
                await user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10],
                                            telo, u[12])
                await user_info.close_connection(conn)


    else:  # Просто текст
        await user_info.just_text(event)


@bot.on(events.NewMessage(pattern='/inlb'))
async def start_message(message):
    await bot.send_message(message.chat_id, 'Добавляем кнопки в сообщение', parse_mode='html', link_preview=False)

    raise StopPropagation


if __name__ == '__main__':
    bot.run_until_disconnected()
