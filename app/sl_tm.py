import user_info
import bl_as_modul
import aiosqlite
from telethon.tl import types
from telethon.tl.types import (
    KeyboardButtonRow,
    KeyboardButtonCallback,
)

from datetime import date, datetime, timedelta

mdate_db = './mdate.db'
bot = bl_as_modul.client

tempAM_but = types.ReplyInlineMarkup(
    rows=[
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="12", data=b"timeam12"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="11", data=b"timeam11"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 1", data=b"timeam1"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="10", data=b"timeam10"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 2", data=b"timeam2"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 9", data=b"timeam9"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 3", data=b"timeam3"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 8", data=b"timeam8"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 4", data=b"timeam4"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 7", data=b"timeam7"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 5", data=b"timeam5"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 6", data=b"timeam6"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="PM", data=b"timeam_pm"),
                                   ]
                          ),
    ]
)

tempPM_but = types.ReplyInlineMarkup(
    rows=[
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="24", data=b"timepm24"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="23", data=b"timepm23"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="13", data=b"timepm13"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="22", data=b"timepm22"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="14", data=b"timepm14"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="21", data=b"timepm21"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="15", data=b"timepm15"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="20", data=b"timepm20"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="16", data=b"timepm16"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="19", data=b"timepm19"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="17", data=b"timepm17"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="AM", data=b"timepm_am"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="18", data=b"timepm18"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
    ]
)


min_but = types.ReplyInlineMarkup(
    rows=[
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 0", data=b"timem0"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="55", data=b"timem55"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text=" 5", data=b"timem5"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="50", data=b"timem50"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="10", data=b"timem10"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="45", data=b"timem45"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="15", data=b"timem15"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="40", data=b"timem40"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="20", data=b"timem20"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="35", data=b"timem35"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="25", data=b"timem25"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   ]
                          ),
        KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Re", data=b"timere"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="30", data=b"timem30"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="  ", data=b"s"),
                                   KeyboardButtonCallback(text="Ok", data=b"timeok_tm"),
                                   ]
                          ),
    ]
)


async def sl_time(event):
    sender = await event.get_sender()
    channel = sender.id  # 275965108
    hr = 25
    mnt = 61

    if event.data == b"timeam_pm":
        await event.edit("PM", buttons=tempPM_but)
    elif event.data == b"timepm_am":
        await event.edit("AM", buttons=tempAM_but)
    elif event.data == b"timere":
        await event.edit("pm", buttons=tempPM_but)
    elif event.data == b"timeam12":
        await event.edit("12 часов.  выберете минуты", buttons=min_but)
        hr = 12
    elif event.data == b"timeam1":
        await event.edit("1 час.  выберете минуты", buttons=min_but)
        hr = 1
    elif event.data == b"timeam2":
        await event.edit("2 часа.  выберете минуты", buttons=min_but)
        hr = 2
    elif event.data == b"timeam3":
        await event.edit("3 часа.  выберете минуты", buttons=min_but)
        hr = 3
    elif event.data == b"timeam4":
        await event.edit("4 часа.  выберете минуты", buttons=min_but)
        hr = 4
    elif event.data == b"timeam5":
        await event.edit("5 часов.  выберете минуты", buttons=min_but)
        hr = 5
    elif event.data == b"timeam6":
        await event.edit("6 часов.  выберете минуты", buttons=min_but)
        hr = 6
    elif event.data == b"timeam7":
        await event.edit("7 часов.  выберете минуты", buttons=min_but)
        hr = 7
    elif event.data == b"timeam8":
        await event.edit("8 часов.  выберете минуты", buttons=min_but)
        hr = 8
    elif event.data == b"timeam9":
        await event.edit("9 часов.  выберете минуты", buttons=min_but)
        hr = 9
    elif event.data == b"timeam10":
        await event.edit("10 часов.  выберете минуты", buttons=min_but)
        hr = 10
    elif event.data == b"timeam11":
        await event.edit("11 часов.  выберете минуты", buttons=min_but)
        hr = 11
    elif event.data == b"timepm23":
        await event.edit("23 часа.  выберете минуты", buttons=min_but)
        hr = 23
    elif event.data == b"timepm24":
        await event.edit("24 часа.  выберете минуты", buttons=min_but)
        hr = 24
    elif event.data == b"timepm13":
        await event.edit("13 часов.  выберете минуты", buttons=min_but)
        hr = 13
    elif event.data == b"timepm14":
        await event.edit("14 часов.  выберете минуты", buttons=min_but)
        hr = 14
    elif event.data == b"timepm15":
        await event.edit("15 часов.  выберете минуты", buttons=min_but)
        hr = 15
    elif event.data == b"timepm16":
        await event.edit("16 часов.  выберете минуты", buttons=min_but)
        hr = 16
    elif event.data == b"timepm17":
        await event.edit("17 часов.  выберете минуты", buttons=min_but)
        hr = 17
    elif event.data == b"timepm18":
        await event.edit("18 часов.  выберете минуты", buttons=min_but)
        hr = 18
    elif event.data == b"timepm19":
        await event.edit("19 часов.  выберете минуты", buttons=min_but)
        hr = 19
    elif event.data == b"timepm20":
        await event.edit("20 часов.  выберете минуты", buttons=min_but)
        hr = 20
    elif event.data == b"timepm21":
        await event.edit("21 час.  выберете минуты", buttons=min_but)
        hr = 21
    elif event.data == b"timepm22":
        await event.edit("22 часа.  выберете минуты", buttons=min_but)
        hr = 22
    elif event.data == b"timem0":
        await event.edit(" 0 минут", buttons=min_but)
        mnt = 0
    elif event.data == b"timem5":
        await event.edit(" 5 минут", buttons=min_but)
        mnt = 5
    elif event.data == b"timem10":
        await event.edit(" 10 минут", buttons=min_but)
        mnt = 10
    elif event.data == b"timem15":
        await event.edit(" 15 минут", buttons=min_but)
        mnt = 15
    elif event.data == b"timem20":
        await event.edit(" 20 минут", buttons=min_but)
        mnt = 20
    elif event.data == b"timem25":
        await event.edit(" 25 минут", buttons=min_but)
        mnt = 25
    elif event.data == b"timem30":
        await event.edit(" 30 минут", buttons=min_but)
        mnt = 30
    elif event.data == b"timem35":
        await event.edit(" 35 минут", buttons=min_but)
        mnt = 35
    elif event.data == b"timem40":
        await event.edit(" 40 минут", buttons=min_but)
        mnt = 40
    elif event.data == b"timem45":
        await event.edit(" 45 минут", buttons=min_but)
        mnt = 45
    elif event.data == b"timem50":
        await event.edit(" 50 минут", buttons=min_but)
        mnt = 50
    elif event.data == b"timem55":
        await event.edit(" 55 минут", buttons=min_but)
        mnt = 55
    elif event.data == b"timeok_tm":
        await event.edit("Данные внесены")
        # m = await bot.send_message(channel, 'можно формировать следушее сообщение')
        await user_info.snd_chl_s(event)
        # break

    if not (hr == 25 and mnt == 61):
        conn = await user_info.create_connection()
        t = await user_info.find_user(conn, channel, '', 1)
        await user_info.close_connection(conn)

        conn_d = await create_conn_date()
        if t[12] == 0:
            u = await find_date(conn_d, t[0], t[1], t[3])   # pkanal берем для уникальности, а по Ок меняем на id
        else:
            u = await find_date(conn_d, t[0], t[1], t[12])

        while (True):
            try:
                if event.data.startswith(b"timeam") or event.data.startswith(b"timepm"):
                    bias_hour = datetime.now().hour - datetime.utcnow().hour
                    hr = hr - bias_hour

                    if t[4] == 'sch' or t[4].startswith('sch'):  #
                        await update_info(conn_d, u[0], u[1], u[2], u[3], hr, u[5], u[6], u[7], u[8], u[9], u[10],
                                          u[11], u[12], u[13], u[14], 0)
                        await close_connection_d(conn_d)
                    elif t[4].startswith('del'):
                        await update_info(conn_d, u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], hr, u[10],
                                          u[11], u[12], u[13], u[14], 0)
                        await close_connection_d(conn_d)
                    break
                elif event.data.startswith(b"timem"):
                    if t[4] == 'sch' or t[4].startswith('sch'):  #
                        await update_info(conn_d, u[0], u[1], u[2], mnt, u[4], u[5], u[6], u[7], u[8], u[9], u[10],
                                          u[11], u[12], u[13], u[14], 0)
                        await close_connection_d(conn_d)
                    elif t[4].startswith('del'):  # мгновенно и удалить
                        await update_info(conn_d, u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], mnt, u[9], u[10],
                                          u[11], u[12], u[13], u[14], 0)
                        await close_connection_d(conn_d)

                    break
            except Exception:  # Зачем?
               # if event.data.startswith(b"timeam") or event.data.startswith(b"timepm"):
                   # await add_mess_string(event.chat_id, event.chat_id, event.chat_id, hr, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
                    break
            break



sql_create_mess_table = """ CREATE TABLE IF NOT EXISTS messdate (
                                        bot_chat_id integer,       
                                        channel_chat_id integer,   
                                        unic_mess_id integer,      
                                        min_snd integer,           
                                        hr_snd integer,            
                                        day_snd integer,           
                                        month_snd integer,         
                                        year_snd integer,          
                                        min_del integer,           
                                        hr_del integer,            
                                        day_del integer,           
                                        month_del integer,         
                                        year_del integer,          
                                        telo text,                 
                                        but_text                   
                                    ); """




async def create_conn_date():
    db = await aiosqlite.connect(mdate_db)
    cursor = await db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='messdate';")
    if not await cursor.fetchone():
        await cursor.execute(sql_create_mess_table)
    return cursor, db


async def find_date(cursor, n0, n1, n2):  # поиск юзера
        bci = (n0, n1, n2)
        await cursor[0].execute('SELECT * FROM messdate WHERE bot_chat_id=? and channel_chat_id=? and unic_mess_id=?', bci)
        user_string = await cursor[0].fetchone()  # возвращается кортеж
        # raise StopPropagation
        return user_string





async def add_mess_string(n0, n1, n2,  n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14):
    user = (n0, n1, n2,  n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14)

    async with aiosqlite.connect(mdate_db) as db:
        await db.execute('INSERT INTO messdate VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user)
        await db.commit()

async def close_connection_d(conn_d):
    await conn_d[0].close()
    await conn_d[1].close()

async def update_info(conn_d, n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, dop):  # Обновляем данные
    user = (n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14)
    if dop == 0:
        del_user = (n0, n1, n2)  # во втором входе в базах 9 а приходит id
    else:
        del_user = (n0, n1, dop)

    await conn_d[0].execute('DELETE FROM messdate WHERE bot_chat_id = ? and channel_chat_id = ?  and unic_mess_id = ?', del_user)
    await conn_d[1].commit()
    await conn_d[0].execute('INSERT INTO messdate VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user)
    await conn_d[1].commit()   # Сохраняем изменения


async def dmy(result, event):  # вводим дату первый вход отложенное сообщение
    conn_d = await create_conn_date()
    ic = result.timetuple()
    sender = await event.get_sender()
    channel = sender.id
    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, channel, '', 1)
    await user_info.close_connection(conn)

    if u[4] == 'sch' or u[4].startswith('sch'):  # отложенное
        await add_mess_string(u[0], u[1], u[3], 0, 0, ic.tm_mday, ic.tm_mon, ic.tm_year, 0, 0, 0, 0, 0, u[5], u[11])
    elif u[4].startswith('del'):  # мгновенно и удалить
        if u[12] != 0:
            t = await find_date(conn_d, u[0], u[1], u[12])
        else:
            t = await find_date(conn_d, u[0], u[1], u[3])  # тут ошибка

        try:
            await update_info(conn_d, t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9],
                              ic.tm_mday, ic.tm_mon, ic.tm_year, t[13], t[14], 0)
        except Exception:
            await add_mess_string(u[0], u[1], u[3], 0, 0, 0, 0, 0, 0, 0, ic.tm_mday, ic.tm_mon, ic.tm_year,
                                  u[5], u[11])

    await close_connection_d(conn_d)



async def un_mes(event, rec, msg_id):  # вводим уникальный id сообщния

    conn_d = await create_conn_date()
    u = await find_date(conn_d, event.chat_id, event.chat_id, event.chat_id)
    await update_info(conn_d, event.chat_id, rec, msg_id, u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11], u[12],
                      u[13], u[14], u[2])

