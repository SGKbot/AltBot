import bl_as_modul
import shutil
from telethon import events, Button
from telethon.events import StopPropagation
from telethon.tl import types
from telethon import TelegramClient, events, Button
from telethon.tl.custom.message import Message
from telethon.client.messages import MessageMethods

import sl_tm
import user_info
from datetime import date, datetime, time
import os
import glob
import cfg
bot = bl_as_modul.client

async def exampl_send():
    d = datetime.today()
    conn_d = await sl_tm.create_conn_date()
    u_send = await find_cron(conn_d, d.minute, d.hour, d.day, d.month, d.year, 'send')
    u_del = await find_cron(conn_d, d.minute, d.hour, d.day, d.month, d.year, 'del')
    await sl_tm.close_connection_d(conn_d)

    if u_send:  # len(u_send) > 0
        i = 0
        while i < len(u_send):
            pr = u_send[i]
            msg = await snd_schl(pr, 1)
            i = i + 1
            del_user = (pr[0], pr[1], pr[2])
            conn_d = await sl_tm.create_conn_date()
            await conn_d[0].execute('DELETE FROM messdate WHERE '
                                    'bot_chat_id = ? and channel_chat_id = ?  and unic_mess_id = ?', del_user)
            await conn_d[1].commit()
            file_path_ = await file_path_sch(pr)
            if file_path_:
                os.remove(file_path_)
            if pr[12] > 0:  # сообшение отправлено, но его надо потом удалить (год не пустой) - меняем id
                user = (pr[0], pr[1], msg.id, pr[3], pr[4], pr[5], pr[6], pr[7], pr[8], pr[9], pr[10], pr[11],
                        pr[12], pr[13], pr[14])
                await conn_d[0].execute('INSERT INTO messdate VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                        user)
                await conn_d[1].commit()  # Сохраняем изменения
            await sl_tm.close_connection_d(conn_d)
    if u_del:
        i = 0
        while i < len(u_del):
            pr = u_del[i]
            await bot.delete_messages(pr[1] * (-1), pr[2])
            del_user = (pr[0], pr[1], pr[2])
            conn_d = await sl_tm.create_conn_date()
            await conn_d[0].execute('DELETE FROM messdate WHERE '
                                    'bot_chat_id = ? and channel_chat_id = ?  and unic_mess_id = ?', del_user)
            await conn_d[1].commit()
            await sl_tm.close_connection_d(conn_d)
            i = i + 1


async def find_cron(cursor, min_, hr, day, month, year, sd):  # поиск юзера sd признак отправки / удаления
    bci = (min_, hr, day, month, year)
    if sd == 'send':
        await cursor[0].execute('SELECT * FROM messdate WHERE min_snd=? and hr_snd=? and day_snd=? and month_snd=? '
                                'and year_snd=?', bci)
        user_string = await cursor[0].fetchall()  # возвращается кортеж кортежей
    elif sd == 'del':
        await cursor[0].execute('SELECT * FROM messdate WHERE min_del=? and hr_del=? and day_del=? and month_del=? '
                                'and year_del=?', bci)
        user_string = await cursor[0].fetchall()  # возвращается кортеж кортежей

    return user_string



async def snd_schl(pr, recipient):  # отправка отложенного, recipient 1 в канал, 2 в бот

    if recipient == 1:
        rcp = pr[1] * (-1)
    elif recipient == 2:
        rcp = pr[0]


    if len(pr[14]) > 0:
        x2, x3, x4, x5, x6, x7 = await user_info.processing_button_data(pr[14])

    # 0 id бота          используется в имени мм файла
    full_mm_path = await file_path_sch(pr)
    # 2 id  сообщения    используется в имени мм файла

    if not os.path.exists(full_mm_path):  # нет мм файла
        if not pr[14]:
            msg = await bot.send_message(rcp, pr[13], parse_mode='html', link_preview=False)
        else:
            msg = await bot.send_message(rcp, pr[13], parse_mode='html', link_preview=False,
                                             buttons=[[Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                                                      [Button.url(x3, x2.strip())]])
    else:  # Картинка или видео с каментом
        if not pr[14]:
            msg = await bot.send_file(rcp, full_mm_path, caption=pr[13], parse_mode='html')
        else:
            msg = await bot.send_file(rcp, full_mm_path, caption=pr[13], parse_mode='html',
                                          buttons=[[Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                                                  [Button.url(x3, x2.strip())]])

    if recipient == 2:
        await bot.send_message(rcp, 'Ваши действия', buttons=bl_as_modul.schinf_but)

    return msg


async def file_path_sch(pr):
    # 0 id бота          используется в имени мм файла
    # 2 id  сообщения    используется в имени мм файла
    name_mm_file = str(pr[0]) + str(pr[2])  # имя без расширения
    mmf = glob.glob(cfg.mm_file_path + name_mm_file + '.*')  # кортеж
    try:
        full_mm_path = mmf[0]
    except Exception:
        full_mm_path = ''
    return full_mm_path


async def all_send_ch(event):  # ищем все отложенные сообщения и для удаления
    sender = await event.get_sender()
    channel = sender.id

    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, channel, '', 1)
    await user_info.close_connection(conn)

    conn_d = await sl_tm.create_conn_date()
    all_bc = (u[0], u[1])
    await conn_d[0].execute('SELECT * FROM messdate WHERE bot_chat_id = ? and channel_chat_id = ?', all_bc)
    spisok = await conn_d[0].fetchall()  # возвращается кортеж кортежей
    await sl_tm.close_connection_d(conn_d)

    return spisok


async def all_sd_keyb(spisok):  # создаем клаву для вывода списка отложенных

    k = len(spisok)
    sp = ['', '', '', '', '', '', '', '', '', '']
    i = 0
    while i < k:
        SS = spisok[i]
        t = await time_info(SS[3], SS[4], SS[5], SS[6], SS[7])
        t2 = ''
        if SS[12] > 0:
            t2 = await time_info(SS[8], SS[9], SS[10], SS[11], SS[12])
        sp.insert(i, SS[13][:20] + t + t2)
        i = i + 1

    return sp

async def time_info(t1, t2, t3, t4, t5):
    t = ' ' + str(t2) + ':' + str(t1) + ' ' + str(t3) + '.' + str(t4) + '.' + str(t5-2000)
    return t

async def transf_sch(event):  # перенос из табл отложенных в табл текущих
    sender = await event.get_sender()
    channel = sender.id
    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, channel, '', 1)
    await user_info.close_connection(conn)
    if 0 < u[9] < 11:
        spisok = await all_send_ch(event)
        pr = spisok[u[9] - 1]
        mmf = await file_path_sch(pr)
        pkanal = 11
        if not mmf:
            mmf = ''
            pkanal = 9
        conn = await user_info.create_connection()
        await user_info.update_user(conn, pr[0], pr[1], u[2], pkanal, u[4], pr[13], u[6], u[7], u[8], u[9], mmf, pr[14], pr[2])
        await user_info.close_connection(conn)


async def update_corrected(event):
    sender = await event.get_sender()
    channel = sender.id
    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, channel, '', 1)
    await user_info.close_connection(conn)
    if 0 < u[9] < 11:
        spisok = await all_send_ch(event)
        pr = spisok[u[9] - 1]
        mmf = await file_path_sch(pr)

        if not mmf == u[10]:
            if mmf:
                os.remove(mmf)

        if len(u[10]) > 0:
            name_mm_file = str(u[0]) + str(pr[2]) + u[10][(u[10].rindex('.')):]
            full_mm_path = cfg.mm_file_path + name_mm_file
            if not u[10] == full_mm_path:
                shutil.copyfile(u[10], full_mm_path)

        conn_d = await sl_tm.create_conn_date()
        await sl_tm.update_info(conn_d, pr[0], pr[1], pr[2], pr[3], pr[4], pr[5], pr[6], pr[7], pr[8], pr[9], pr[10],
                                pr[11], pr[12], u[5], u[11], 0)
        await sl_tm.close_connection_d(conn_d)


        await user_info.snd_clear_info_cnl(event)


async def date_utc_msk(date_in):
    date_in_sec = datetime.timestamp(date_in)
    msk = 3*60*60
    date_out = datetime.fromtimestamp(date_in_sec - msk)

    return date_out