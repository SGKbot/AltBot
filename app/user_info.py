# from telebot.apihelper import send_message
from telethon.events import StopPropagation

import aiosqlite
import bl_as_modul
import cfg

bot = bl_as_modul.client


async def create_connection():
    db = await aiosqlite.connect(cfg.user_db)
    cursor = await db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects';")

    if not await cursor.fetchone():
        await cursor.execute(cfg.sql_create_user_table)

    return cursor, db


async def close_connection(conn):
    await conn[0].close()
    await conn[1].close()


async def add_user(conn, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11):  # Вставляем данные в таблицу bot_chat_id

    user = (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11)
    # await conn[0].execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user)
    # await conn[0].commit()   # Сохраняем изменения

    async with aiosqlite.connect(cfg.user_db) as db:
        await db.execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user)
        await db.commit()


async def find_user(cursor, n0, n2, n9):  # поиск юзера

    # cursor = conn.cursor()
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


# async def acquaintance(message):  # знакомство
    # message.chat.id,
  #  await send_message(message.chat_id, cfg.Pr, parse_mode='html', link_preview=False)
     #   message.answer(cfg.Pr, parse_mode='html', disable_web_page_preview=True)


async def update_user(conn, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11):  # Обновляем данные
    # cursor = conn.cursor()
    user = (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11)
    del_user = (n1, 1)
    await conn[0].execute('DELETE FROM projects WHERE bot_chat_id = ? and chn=?', del_user)
    await conn[1].commit()
    await conn[0].execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user)
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

    await update_user(conn, u[0], u[1], u[2], 10, telo, telo, u[6], u[7], u[8], u[9], u[10])
    await close_connection(conn)


async def help_bl_as(message):  # удалить
    # bot.delete_message(s)
    # await message.delete()
    await message.answer(bl_as_modul.HSK, parse_mode='html', disable_web_page_preview=True)

    conn = await create_connection()
    u = await find_user(conn, message.chat.id, '', 1)
    await update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], u[9], u[10])
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
    await update_user(conn, u[0], u[1], u[2], 9, '', telo, u[6], u[7], u[8], u[9], u[10])
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
        if n == True:
            await update_user(conn, n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7], 0, n[9], '')

    del_user = (vis[0], vis[2])
    await conn[0].execute('DELETE FROM projects WHERE bot_chat_id = ? and channel_name = ?', del_user)
    await conn[1].commit()

    if od == 1:
        visi = (vis[0], vis[1], vis[2], vis[3], vis[4], vis[5], vis[6], vis[7], 1, vis[9], '')
        await conn[0].execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', visi)
        await conn[1].commit()

    await close_connection(conn)
