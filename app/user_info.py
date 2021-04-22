# from telebot.apihelper import send_message
from telethon import events, Button
from telethon.events import StopPropagation
from telethon import TelegramClient

from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from datetime import date, datetime, timedelta

import aiosqlite
import bl_as_modul
import cfg
import sl_tm
from PIL import Image
bot = bl_as_modul.client
import shutil
import os


async def create_connection():
    # os.remove(cfg.user_db)
    db = await aiosqlite.connect(cfg.user_db)
    cursor = await db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects';")

    if not await cursor.fetchone():
        await cursor.execute(cfg.sql_create_user_table)

    return cursor, db


async def close_connection(conn):
    await conn[0].close()
    await conn[1].close()


async def add_user(conn, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13):  # Вставляем данные в таблицу bot_chat_id
    user = (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13)
    async with aiosqlite.connect(cfg.user_db) as db:
        await db.execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user)
        await db.commit()


async def find_user(cursor, n0, n2, n9):  # поиск юзера

    if n9 == 1:
        bci = (n0, n9)
        await cursor[0].execute('SELECT * FROM projects WHERE bot_chat_id=? and chn=?', bci)
        user_string = await cursor[0].fetchone()  # возвращается кортеж
    elif n9 == 2:  # 2 признак, все строки
        bci = (n0, )
        await cursor[0].execute('SELECT * FROM projects WHERE bot_chat_id=?', bci)
        user_string = await cursor[0].fetchall()  # возвращается кортеж кортежей

    elif n2 != 0:  # признак,  строки выбора или удаления
        bci = (n0, n2)
        await cursor[0].execute('SELECT * FROM projects WHERE bot_chat_id=? and channel_chat_id=?', bci)
        user_string = await cursor[0].fetchone()  # возвращается кортеж
        # user_string = 1
        raise StopPropagation

    return user_string


async def update_user(conn, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13):  # Обновляем данные
    # cursor = conn.cursor()
    user = (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13)
    del_user = (n1, 1)
    await conn[0].execute('DELETE FROM projects WHERE bot_chat_id = ? and chn=?', del_user)
    await conn[1].commit()
    await conn[0].execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user)
    await conn[1].commit()   # Сохраняем изменения



async def add_hashtag(message, hashtag):

    if hashtag == 'hands':
        hashtag = '#Hands'
    elif hashtag == 'think':
        hashtag = '#Подумай'
    elif hashtag == 'stolen':
        hashtag = '#Украдено'
    elif hashtag == 'ads':
        hashtag = '#Реклама'
    elif hashtag == 'sight':
        hashtag = '#Мнение'
    elif hashtag == 'humor':
        hashtag = '#Юмор'
    elif hashtag == 'news':
        hashtag = '#Новости'

    conn = await create_connection()
    u = await find_user(conn, message.chat.id, '', 1)

    if u[3] == 10:
       telo = u[4] + '\n' + '<a href="' + u[6] + '">' + hashtag + '</a>'
    else:
       telo = u[5] + '\n' + '<a href="' + u[6] + '">' + hashtag + '</a>'


    await bot.send_message(u[0],'<b>' + u[2] + '</b>' + '\n\n' + telo, parse_mode='html', link_preview=False)

    await update_user(conn, u[0], u[1], u[2], 10, telo, telo, u[6], u[7], u[8], u[9], u[10], u[11], u[12])
    await close_connection(conn)


async def just_text(event):
    telo = event.message.text + '\n'  # Просто текст
    if round(telo.count('ьь') / 2) - telo.count('ьь') / 2 == 0.5 or telo.count('ьь') == 1:
        await bot.send_message(event.chat_id, 'Вы неправильно оформили выделение жирным шрифтом', parse_mode='html', link_preview=False)
    else:
        while (True):
            try:
                index = telo.index('ьь')
                telo = telo[:index] + '<b>' + telo[index + 2:]

                index = telo.index('ьь', index)
                telo = telo[:index] + '</b>' + telo[index + 2:]
            except ValueError:
                break

    conn = await create_connection()
    u = await find_user(conn, event.chat_id, '', 1)
    # тут
    await update_user(conn, u[0], u[1], u[2], 9, '', telo, u[6], u[7], u[8], u[9], u[10], u[11], u[12])
    await close_connection(conn)

async def Name_ch_(SelStr):
    k = len(SelStr)
    spisok = ['', '', '', '', '', '']
    i = 0
    while i < k:
        SS = SelStr[i]
        spisok.insert(i, SS[2])
        i = i + 1
        # await message.Message.answer_document(text=spisok[i])

    return spisok


async def sel_chan(channel, id_message, s, od):

    await bot.delete_messages(channel, id_message)

    conn = await create_connection()
    etud = await find_user(conn, channel, '', 2)
    vis = etud[s]

    if od == 1:
        n = await find_user(conn, channel, '', 1)   # 1 зачем???????
        if n:  #  == True
            await update_user(conn, n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7], 0, n[9], '', n[11], n[12])

    del_user = (vis[0], vis[2])
    await conn[0].execute('DELETE FROM projects WHERE bot_chat_id = ? and channel_name = ?', del_user)
    await conn[1].commit()

    if od == 1:
        visi = (vis[0], vis[1], vis[2], vis[3], vis[4], vis[5], vis[6], vis[7], 1, vis[9], '', n[11], vis[12])
        await conn[0].execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', visi)
        await conn[1].commit()

    await close_connection(conn)

    conn = await create_connection()
    u = await find_user(conn, channel, '', 1)
    await update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], 0, '', '', 0)
    await close_connection(conn)


async def snd_chl_i(event):  # Immediately

    #  видео с каментом    pkanal = 11 mm=2
    #  Водяной знак        pkanal = 5     u[3]
    #  Работа со ссылками  pkanal = 6
    #  Картинка с каментом pkanal = 11 mm=1
    #  instant view        pkanal = 22
    #  просто сообщение    pkanal = 9
    #  сообщение c хэште   pkanal = 10
    # bot.delete_message(message.chat.id, message.message_id)
    #  await bot.delete_messages(channel, id_message)

    sender = await event.get_sender()
    channel = sender.id
    conn = await create_connection()
    u = await find_user(conn, channel, '', 1)
    await close_connection(conn)

    if u[3] == 5 or u[3] == 6 or u[3] == 100 or u[3]-2000 == 5 or u[3]-2000 == 6 or u[3]-2000 == 100:
        await bot.send_message(channel, 'Пустые сообщения не отправляются в канал', parse_mode='html',
                               link_preview=False)
    else:  # Выбираем стиль отправки
        # conn = await create_connection()
        # u = await find_user(conn, sender.id, '', 1)
        x2, x3, x4, x5, x6, x7 = await processing_button_data(u[11])
        if u[0] > 0:
            if u[3] == 9 or u[3] == 10 or u[3]-2000 == 9 or u[3]-2000 == 10:  # u[4] u[5]
                if not u[11]:
                    msg = await bot.send_message(u[1] * (-1), u[5], parse_mode='html', link_preview=False)
                else:
                    msg = await bot.send_message(u[1] * (-1), u[5], parse_mode='html', link_preview=False,
                                                 buttons=[[Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                                                          [Button.url(x3, x2.strip())]
                                                          ])
                #  await bot.delete_messages(u[1] * (-1), msg.id)
            elif u[3] == 11 or u[3]-2000 == 11:  # Картинка или видео с каментом
                if u[7] == 2:
                    msg = await bot.send_file(u[1] * (-1), u[10], caption=u[5], parse_mode='html',
                    buttons=[
                    [Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                    [Button.url(x3, x2.strip())]])
                else:
                    if not u[11]:
                        msg = await bot.send_file(u[1], u[10], caption=u[5], parse_mode='html')
                    else:
                        msg = await bot.send_file(u[1], u[10], caption=u[5], parse_mode='html',
                                                buttons=[
                                                [Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                                                [Button.url(x3, x2.strip())] ])

            elif u[3] == 22 or u[3]-2000 == 22:
                msg = await bot.send_message(u[1], u[4], parse_mode='html', disable_web_page_preview=False,
                    buttons=[
                    [Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                    [Button.url(x3, x2.strip())]])
            else:
                msg = await bot.send_message(u[1] * (-1), u[4], parse_mode='html', link_preview=False,
                    buttons=[
                    [Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                    [Button.url(x3, x2.strip())]])
        else:
            await bot.send_message(u[0], 'Вы не являетесь Администратором канала', parse_mode='html',
                                   link_preview=False)



async def for_cron(event):  # для переноса в крон

    sender = await event.get_sender()
    channel = sender.id
    conn = await create_connection()
    u = await find_user(conn, channel, '', 1)
    await close_connection(conn)

    conn_d = await sl_tm.create_conn_date()
    t = await sl_tm.find_date(conn_d, u[0], u[1], u[3])  # id берем для уникальности,

    if u[4] == 'delimm':
        await sl_tm.add_mess_string(u[0], u[1], u[2], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', '', msg.id)
    else:
        await sl_tm.update_info(conn_d, t[0], t[1], msg.id, t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11],
                                t[12], t[13], t[14], 0)

    await sl_tm.close_connection_d(conn_d)

    # для переноса в крон


async def snd_clear_info_cnl(event):  # чистим строку информации о канале
    sender = await event.get_sender()
    channel = sender.id
    conn = await create_connection()
    u = await find_user(conn, channel, '', 1)
    await update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], 0, '', '', u[12])
    await close_connection(conn)



async def run_dt(event):  # запуск выбора времени даты
    calendar, step = DetailedTelegramCalendar(telethon=True, min_date=date.today()).build()
    await event.respond(f"Select {LSTEP[step]}", buttons=calendar)



async def snd_chl_s(event):  # Ok дата время


    sender = await event.get_sender()
    channel = sender.id

    conn = await create_connection()
    u = await find_user(conn, channel, '', 1)
    conn_d = await sl_tm.create_conn_date()

    if u[12] == 0:

        t = await sl_tm.find_date(conn_d, u[0], u[1], u[3])   # тут ошибка
        await sl_tm.update_info(conn_d, t[0], t[1], event.original_update.msg_id, t[3], t[4], t[5], t[6], t[7], t[8],
                                t[9], t[10], t[11], t[12], t[13], t[14], u[3])
        await sl_tm.close_connection_d(conn_d)
        await update_user(conn, u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9],
                          u[10], u[11], event.original_update.msg_id)
        await close_connection(conn)



    # 0 id бота          используется в имени мм файла
    if len(u[10]) > 0:
        name_mm_file = str(u[0]) + str(event.original_update.msg_id) + u[10][(u[10].rindex('.')):]
        full_mm_path = cfg.mm_file_path + name_mm_file
        # cf = open(full_mm_path, 'w')
        # cf.write(u[10])
        # cf.close()
        shutil.copyfile(u[10], full_mm_path)
    # 2 id  сообщения    используется в имени мм файла

    if u[4] == 'sch' or u[4] == 'del' or u[4] == 'delimm':
        if u[4] == 'delimm':
            await snd_chl_i(event)

        conn = await create_connection()
        await update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], 0, '', '', 0)  # u[11] u[9]
        await close_connection(conn)

    # это останется......................................
    conn = await create_connection()
    u = await find_user(conn, channel, '', 1)
    if u[4] == 'schdel':  #
        await update_user(conn, u[0], u[1], u[2], u[3], 'del', u[5], u[6], u[7], u[8], u[9], u[10], u[11], u[12])
        await run_dt(event)
    await close_connection(conn)
    # это останется......................................


async def combo_f(event):
    sender = await event.get_sender()
    channel = sender.id
    id_message = event.message_id
    conn = await create_connection()
    u = await find_user(conn, channel, '', 1)
    x2, x3, x4, x5, x6, x7 = await processing_button_data(u[11])

    await close_connection(conn)
    await bot.delete_messages(channel, id_message)  # удаляю слово Комб

    if u[7] > 0:

        # if message.message_id - 1:
        # await bot.delete_message(channel, id_message - 1)  # удаляю сообщение для комб

        if u[3]-2000 == 10 or u[3]-2000 == 9 or u[3] == 10 or u[3] == 9:
            telo = u[4]
        if u[7] == 1:  # mm == 1  photo
            photo = Image.open(u[10])
            photo_path = f'{u[10]}.jpeg'
            photo.save(photo_path, 'JPEG')
            if not u[11]:
                with open(photo_path, 'rb') as fi:
                    info = await bot.send_file(u[0], fi, caption='<b>' + u[2] + '</b>' + '\n\n' + u[5], parse_mode='html')
            else:
                with open(photo_path, 'rb') as fi:
                    info = await bot.send_file(u[0], fi, caption='<b>' + u[2] + '</b>' + '\n\n' + u[5],
                                               parse_mode='html',
                                               buttons=[
                                                   [Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                                                   [Button.url(x3, x2.strip())]
                                               ])


        elif u[7] == 2:  # mm == 2  video .file_id   # 123
            with open(u[10], 'rb') as fi:
                info = await bot.send_file(u[0], fi, caption=u[5], parse_mode='html',
                    buttons=[
                    [Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                    [Button.url(x3, x2.strip())]
                            ])

        conn = await create_connection()
        u = await find_user(conn, channel, '', 1)
        await update_user(conn, u[0], u[1], u[2], 11, u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11], u[12])
        await close_connection(conn)

    else:
        await bot.send_message(channel, 'Нет медиафайла!', parse_mode='html',
                               link_preview=False)

    # await close_connection(conn)


async def processing_button_data(telo):
    count_but = telo.count('\n')
    try:
        if count_but == 0:
            x2 = telo[telo.rindex(' '):]
            x3 = telo[:telo.rindex(' ')]  # кнопка
            x4 = ''
            x5 = ''
            x6 = ''
            x7 = ''
        elif count_but == 1:
            but1 = telo[:telo.index('\n')]
            but2 = telo[(telo.index('\n') + 1):]

            x2 = but1[but1.rindex(' '):]
            x3 = but1[:but1.rindex(' ')]  # кнопка
            x4 = but2[but2.rindex(' '):]
            x5 = but2[:but2.rindex(' ')]  # кнопка
            x6 = ''
            x7 = ''
        elif count_but == 2:
            but1 = telo[:telo.index('\n')]

            but2 = telo[(telo.index('\n') + 1):(telo.rindex('\n') - 1)]

            but3 = telo[(telo.rindex('\n') + 1):]

            x2 = but1[but1.rindex(' '):]
            x3 = but1[:but1.rindex(' ')]  # кнопка
            x4 = but2[but2.rindex(' '):]
            x5 = but2[:but2.rindex(' ')]  # кнопка
            x6 = but3[but3.rindex(' '):]
            x7 = but3[:but3.rindex(' ')]  # кнопка
    except ValueError:
        x2 = ''
        x3 = ''
        x4 = ''
        x5 = ''
        x6 = ''
        x7 = ''

    return x2, x3, x4, x5, x6, x7




async def snd_feature_choice(event, feat):  # ставим признак выбора
    sender = await event.get_sender()
    channel = sender.id
    conn = await create_connection()
    u = await find_user(conn, channel, '', 1)
    await update_user(conn, u[0], u[1], u[2], u[3], feat, u[5], u[6], u[7], u[8], u[9], u[10], u[11], u[12])
    await close_connection(conn)