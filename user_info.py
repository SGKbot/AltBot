import cfg
import sqlite3
import bl_as_modul

import telebot

# import bot

# from sqlite3 import Error
# from cfg import user_db


bot = bl_as_modul.bot_telebot()

def create_connection():
    conn = sqlite3.connect(cfg.user_db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects';")

    if not cursor.fetchone():
        cursor.execute(cfg.sql_create_user_table)

    return conn


def close_connection(conn):
    conn.close()


def add_user(conn, n1, n2, n3, n4, n5, n6, n7, n8):  # Вставляем данные в таблицу bot_chat_id
    cursor = conn.cursor()
    user = (n1, n2, n3, n4, n5, n6, n7, n8)
    cursor.execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?)', user)
    conn.commit()   # Сохраняем изменения


def find_user(conn, n1):  # поиск юзера

    bci = (n1,)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects WHERE  bot_chat_id=?', bci)
    user_string = cursor.fetchone()  # возвращается кортеж

    return user_string


def acquaintance(message):  # знакомство
    bot.send_message(message.chat.id, cfg.Pr, parse_mode='html', disable_web_page_preview=True)


def update_user(conn, n1, n2, n3, n4, n5, n6, n7, n8):  # Обновляем данные
    cursor = conn.cursor()
    user = (n1, n2, n3, n4, n5, n6, n7, n8)
    del_user = (n1,)
    cursor.execute('DELETE FROM projects WHERE bot_chat_id = ?', del_user)
    conn.commit()
    cursor.execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?)', user)
    conn.commit()   # Сохраняем изменения



def add_hashtag(message, hashtag):

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

    conn = create_connection()
    u = find_user(conn, message.chat.id)

    if u[3] == 10:
       telo = u[4] + '\n' + '<a href="' + u[6] + '">' + hashtag + '</a>'
    else:
       telo = u[5] + '\n' + '<a href="' + u[6] + '">' + hashtag + '</a>'

    if message.message_id:
        bot.delete_message(message.chat.id, message.message_id)

    if message.message_id-1:
        bot.delete_message(message.chat.id, message.message_id-1)

    bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)

    update_user(conn, u[0], u[1], u[2], 10, telo, '', u[6], u[7])
    close_connection(conn)



def help_bl_as(message):

    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, bl_as_modul.HSK, parse_mode='html', disable_web_page_preview=True)

    conn = create_connection()
    u = find_user(conn, message.chat.id)
    update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0)
    close_connection(conn)


def just_text(message):
    telo = message.text + '\n'  # Просто текст
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

    conn = create_connection()
    u = find_user(conn, message.chat.id)
    update_user(conn, u[0], u[1], u[2], 9, '', telo, u[6], u[7])
    close_connection(conn)
