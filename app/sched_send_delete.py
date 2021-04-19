import bl_as_modul
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
            msg = await snd_schl(pr)
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



async def snd_schl(pr):  # отправка отложенного

    if len(pr[14]) > 0:
        x2, x3, x4, x5, x6, x7 = await user_info.processing_button_data(pr[14])

    # 0 id бота          используется в имени мм файла
    full_mm_path = await file_path_sch(pr)
    # 2 id  сообщения    используется в имени мм файла

    if not os.path.exists(full_mm_path):  # нет мм файла
        if not pr[14]:
            msg = await bot.send_message(pr[1] * (-1), pr[13], parse_mode='html', link_preview=False)
        else:
            msg = await bot.send_message(pr[1] * (-1), pr[13], parse_mode='html', link_preview=False,
                                             buttons=[[Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                                                      [Button.url(x3, x2.strip())]])
    else:  # Картинка или видео с каментом
        if not pr[14]:
            msg = await bot.send_file(pr[1], full_mm_path, caption=pr[13], parse_mode='html')
        else:
            msg = await bot.send_file(pr[1], full_mm_path, caption=pr[13], parse_mode='html',
                                          buttons=[[Button.url(x5, x4.strip()), Button.url(x7, x6.strip())],
                                                  [Button.url(x3, x2.strip())]])
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