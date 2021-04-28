if pkanal == 10:
    telo = vkanal + '\n' + '<a href="' + skanal + '">#Hands</a>'
else:
    telo = telo + '\n' + '<a href="' + skanal + '">#Hands</a>'

bot.delete_message(message.chat.id, message.message_id)
if message.message_id - 1:
    bot.delete_message(message.chat.id, message.message_id - 1)

bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
vkanal = telo
telo = ''
pkanal = 10



if pkanal == 10:
    telo = vkanal + '\n' + '<a href="' + skanal + '">#Подумай</a>'
else:
    telo = telo + '\n' + '<a href="' + skanal + '">#Подумай</a>'

bot.delete_message(message.chat.id, message.message_id)
if message.message_id - 1:
    bot.delete_message(message.chat.id, message.message_id - 1)

bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
vkanal = telo
telo = ''
pkanal = 10

if pkanal == 10:
    telo = vkanal + '\n' + '<a href="' + skanal + '">#Украдено</a>'
else:
    telo = telo + '\n' + '<a href="' + skanal + '">#Украдено</a>'

bot.delete_message(message.chat.id, message.message_id)
if message.message_id - 1:
    bot.delete_message(message.chat.id, message.message_id - 1)

bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
vkanal = telo
telo = ''
pkanal = 10

if pkanal == 10:
    telo = vkanal + '\n' + '<a href="' + skanal + '">#Реклама</a>'
else:
    telo = telo + '\n' + '<a href="' + skanal + '">#Реклама</a>'
bot.delete_message(message.chat.id, message.message_id)
if message.message_id - 1:
    bot.delete_message(message.chat.id, message.message_id - 1)
bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
vkanal = telo
telo = ''
pkanal = 10




if pkanal == 10:
    telo = vkanal + '\n' + '<a href="' + skanal + '">#Мнение</a>'
else:
    telo = telo + '\n' + '<a href="' + skanal + '">#Мнение</a>'
bot.delete_message(message.chat.id, message.message_id)
if message.message_id - 1:
    bot.delete_message(message.chat.id, message.message_id - 1)
bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
vkanal = telo
telo = ''
pkanal = 10

if pkanal == 10:
    telo = vkanal + '\n' + '<a href="' + skanal + '">#Юмор</a>'
else:
    telo = telo + '\n' + '<a href="' + skanal + '">#Юмор</a>'
bot.delete_message(message.chat.id, message.message_id)
if message.message_id - 1:
    bot.delete_message(message.chat.id, message.message_id - 1)
bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)
vkanal = telo
telo = ''
pkanal = 10

if pkanal == 10:
    telo = vkanal + '\n' + '<a href="' + skanal + '">#Новости</a>'
else:
    telo = telo + '\n' + '<a href="' + skanal + '">#Новости</a>'

bot.delete_message(message.chat.id, message.message_id)
if message.message_id - 1:
    bot.delete_message(message.chat.id, message.message_id - 1)
bot.send_message(message.chat.id, telo, parse_mode='html', disable_web_page_preview=True)

vkanal = telo
telo = ''
pkanal = 10





if skanal == '' and pv == 0:
    HSK1 = '<b>Не забудьте сделать бота администратором вашего канала и отправить боту ссылку на канал</b>'
    pv = 1
elif pv == 2:

    HSK1 = '<b>Ваш канал </b>' + skanal
    pv = 3

bot.delete_message(message.chat.id, message.message_id)
bot.send_message(message.chat.id, HSK, parse_mode='html', disable_web_page_preview=True)
bot.send_message(message.chat.id, HSK1, parse_mode='html', disable_web_page_preview=True)

telo = ''
vkanal = ''
pkanal = 100





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

pkanal = 9






elif '/t.me/' in message.text or message.text.find('@') == 0:  # устанавливаем канал пользователя

if not message.text.find(
        '@') == -1:  # Нашел @    Тут что-то ни хрена не работает// а С ХЕРА БУДЕТ РАБОТАТЬ ЕСЛИ ПОПАЛ СЮДА ПО УСЛОВИЮ /t.me
    skanal = 'https://t.me/' + message.text[1:]
else:
    skanal = message.text

telo = ''
vkanal = ''
pkanal = 100
bot.delete_message(message.chat.id, message.message_id)
bot.send_message(message.chat.id, 'Вы установили свой канал как ' + skanal, parse_mode='html',
                 disable_web_page_preview=True)

UniqueUserChat = str(message.chat.id)
f = open(UniqueUserChat, 'w')
f.write(message.text)
f.close()
f = open(UniqueUserChat, 'r')
f.close()

pv = 2




if os.path.exists(str(message.chat.id)):
    f = open(str(message.chat.id), 'r')
    bot.send_message(message.chat.id, 'Ваш канал ' + f.read(), parse_mode='html', disable_web_page_preview=True)
    f.close()
else:
    bot.send_message(message.chat.id, 'Введите имя вашего канала в формате https://t.me/SGK_espace', parse_mode='html',
                     disable_web_page_preview=True, reply_markup=markup)




    if os.path.exists(str(message.chat.id)):
        t = open(str(message.chat.id), 'r')
        skanal = t.read()
        t.close()
        pv = 2
    else:
        bot.send_message(message.chat.id, 'Введите имя вашего канала в формате https://t.me/SGK_espace',
                         parse_mode='html', disable_web_page_preview=True, reply_markup=markup)
        skanal=''
_________________________________
ydl_opts = {'outtmpl': video_path,
                                    'merge_output_format': 'mkv',
                                    'noplaylist': 'true',
                                    'ignoreerrors': 'true',
                                    'quiet': True,
                                    'max_filesize': 5120000000,
                                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                                    'filename': video_path_out}
_________________________________________________________________________
ydl_opts = {'outtmpl': video_path, 'merge_output_format': 'mkv', 'max_filesize': 7000000000,
            'filename': video_path_out}

"bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"





keyb_cm = types.InlineKeyboardMarkup()  # наша клавиатура
key_yes_cm = types.InlineKeyboardButton(text='Да', callback_data='cm_yes')  # кнопка «Да»
keyb_cm.add(key_yes_cm)  # добавляем кнопку в клавиатуру
key_no_cm = types.InlineKeyboardButton(text='Нет', callback_data='cm_no')
keyb_cm.add(key_no_cm)
question = 'Запустить менеджер каналов?'
message_keyb_cm = bot.send_message(message.from_user.id, text=question, reply_markup=keyb_cm)


@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("cm"))
def callback_worker_cm(call):
    global message_keyb_mf
    global message_keyb_cm

    if call.data == "cm_yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.delete_message(message.chat.id, message_keyb_cm.message_id)
        # bot.send_message(message.chat.id, 'Да', parse_mode='html', disable_web_page_preview=True)

        keyb_mf = types.InlineKeyboardMarkup()  # наша клавиатура
        key_1_mf = types.InlineKeyboardButton(text='Выбрать канал', callback_data='mf_1')  # кнопка «Да»
        keyb_mf.add(key_1_mf)  # добавляем кнопку в клавиатуру
        key_2_mf = types.InlineKeyboardButton(text='Добавть канал', callback_data='mf_2')
        keyb_mf.add(key_2_mf)
        key_3_mf = types.InlineKeyboardButton(text='Удалить канал', callback_data='mf_3')
        keyb_mf.add(key_3_mf)

        question = 'Выберите действие'
        message_keyb_mf = bot.send_message(message.from_user.id, text=question, reply_markup=keyb_mf)

        # bot.delete_message(message.chat.id, message_keyb_mf.message_id)

        @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("mf"))
        def callback_worker_mf(call):

            global message_keyb_mf

            if call.data == "mf_1":  # call.data это callback_data, которую мы указали при объявлении кнопки
                bot.delete_message(message.chat.id, message_keyb_mf.message_id)

                pr = inl_keyb3('name_keyb', 'name_b', 'Вышло?', '123', '456', '', message)

            elif call.data == "mf_2":  # call.data это callback_data, которую мы указали при объявлении кнопки
                bot.delete_message(message.chat.id, message_keyb_mf.message_id)
            elif call.data == "mf_3":  # call.data это callback_data, которую мы указали при объявлении кнопки
                bot.delete_message(message.chat.id, message_keyb_mf.message_id)




    elif call.data == "cm_no":
        bot.send_message(message.chat.id, 'Нет',
                         parse_mode='html', disable_web_page_preview=True)




@bot.message_handler(content_types=['video'])  # Водяной знак видео p=7 ??????
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
    message_keyb_WM = bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

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
            u = user_info.find_user(conn, message.chat.id, 1)
            text = u[2]
            user_info.update_user(conn, u[0], u[1], u[2], 7, u[4], u[5], u[6], 2, u[8], u[9])
            user_info.close_connection(conn)

            txt = TextClip(text, color='red', fontsize=w // 20)
            txt_col = txt.on_color(size=(my_clip.w + txt.w, txt.h), color=(0, 0, 0), pos=(120, 'center'), col_opacity=0)

            # Этот пример демонстрирует эффект движущегося текста, где позиция является функцией времени (t, в секундах).
            # Конечно, вы можете исправить положение текста вручную. Помните, что вы можете использовать строки,
            # как 'top', 'left', чтобы указать позицию

            txt_mov = txt_col.set_pos(lambda t: (
            max(w / 50, int(w - w * (t + 2) / clip_duration)), max(5 * h / 6, int(h * t / clip_duration))))
            # Записать файл на диск
            final = CompositeVideoClip([my_clip, txt_mov])
            final.duration = my_clip.duration

            video_path = f'{f.name}.mp4'

            # bot.send_chat_action(message.chat.id, action='record_video')
            # bot.send_video(message.chat.id, '82428c1ff4a97038984f32ab98bda266')   гифку ну никак

            final.write_videofile(video_path, fps=24, codec='libx264')

            bot.delete_message(message.chat.id, message.message_id)  # удаляем ненужное сообщение

            with open(video_path, 'rb') as fi:
                info_video = bot.send_video(message.chat.id, fi)

            os.remove(f.name)
            file_info_video = bot.get_file(info_video.video.file_id)





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
            font = ImageFont.truetype(cfg.user_font, width // 20)
            pos = (width // 2, height - height // 10)

            conn = user_info.create_connection()
            u = user_info.find_user(conn, message.chat.id, 1)
            text = u[2]
            user_info.close_connection(conn)

            drawing.text(pos, text, fill=black, font=font)
            pos = (1 + width // 2, 1 + height - height // 10)
            drawing.text(pos, text, fill=black, font=font)
            pos = (2 + width // 2, 2 + height - height // 10)
            drawing.text(pos, text, fill=black, font=font)
            photo_path = f'{f.name}.jpeg'
            photo.save(photo_path, 'JPEG')
            bot.send_chat_action(message.chat.id, action='upload_photo')

            with open(photo_path, 'rb') as fi:
                info = bot.send_photo(message.chat.id, fi)
            os.remove(f.name)
            os.remove(photo_path)

            conn = user_info.create_connection()
            u = user_info.find_user(conn, message.chat.id, 1)
            user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8], U[9])
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
            u = user_info.find_user(conn, message.chat.id, 1)
            user_info.update_user(conn, u[0], u[1], u[2], 5, u[4], u[5], u[6], 1, u[8])
            user_info.close_connection(conn)

 elif len(n2) > 0: #  признак,  строки выбора или удалкния
        bci = (n1, n2)
        cursor.execute('SELECT * FROM projects WHERE bot_chat_id=? and channel_chat_id=?', bci)
        user_string = cursor.fetchone()  # возвращается кортеж

conn = user_info.create_connection()
u = user_info.find_user(conn, message.chat.id, '', 1)
user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], 1, 0)
tt = u[9]
u = user_info.find_user(conn, message.chat.id, chaname[tt], 3)
user_info.update_user(conn, u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], 0)
user_info.close_connection(conn)



photo = Image.open(u[10])
photo_path = f'{u[10]}.jpeg'
photo.save(photo_path, 'JPEG')
        with open(photo_path, 'rb') as fi:
            info = await bot.send_file(u[0], fi)

while (True):
    try:
        if event.data.startswith(b"am") or event.data.startswith(b"pm"):
            await update_info(conn, u[0], u[1], u[2], hr, u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11], u[12])
        elif event.data.startswith(b"m"):
            await update_info(conn, u[0], u[1], u[2], u[3], mnt, u[5], u[6], u[7], u[8], u[9], u[10], u[11], u[12])
    except NameError:
        break
    except Exception:
        if event.data.startswith(b"am") or event.data.startswith(b"pm"):
            await add_mess_string(messagechat_id, senderid, mess_id, hr, 0, 0, 0, 0, 0, 0, 0, 0, '')
    break

async def update_info(conn, n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12):  # Обновляем данные
    user = (n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12)
    del_user = (n0, n1, n2)
    await conn[0].execute('DELETE FROM projects WHERE bot_chat_id = ? and channel_chat_id = ?  and unic_mess_id = ?', del_user)
    await conn[1].commit()
    await conn[0].execute('INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', user)
    await conn[1].commit()   # Сохраняем изменения


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

    calendar, step = DetailedTelegramCalendar(telethon=True, min_date=date.today()).build()
    await event.respond(f"Select {LSTEP[step]}", buttons=calendar)

    # await bot.send_message(channel, ' Введите время', buttons=sl_tm.tempAM_but)

    conn = await user_info.create_connection()
    u = await user_info.find_user(conn, sender.id, '', 1)
    # await user_info.close_connection(conn)

    if u[0] > 0:
        if u[3] == 9 or u[3] == 10:  # u[4] u[5]
            msg = await bot.send_message(u[1] * (-1), u[5], parse_mode='html', link_preview=False)
            await sl_tm.un_mes(event, u[1], msg.id)
            #  await bot.delete_messages(u[1] * (-1), msg.id)
        elif u[3] == 11:  # Картинка или видео с каментом
            if u[7] == 2:
                await bot.send_video(u[1] * (-1), file_info_video.file_id, caption=u[5], parse_mode='html')  # 123
            else:
                await bot.send_file(u[1], u[10], caption=u[5], parse_mode='html')
        elif u[3] == 22:
            await bot.send_message(u[1], u[4], parse_mode='html', disable_web_page_preview=False)
        else:
            await bot.send_message(u[1] * (-1), u[4], parse_mode='html', link_preview=False)
        await user_info.update_user(conn, u[0], u[1], u[2], 100, '', '', u[6], 0, u[8], u[9], '')
    else:
        await bot.send_message(u[0], 'Вы не являетесь Администратором канала', parse_mode='html',
                               link_preview=False)

await user_info.close_connection(conn)

# 0 id бота          используется в имени мм файла
# 1 id канала
# 2 id  сообщения    используется в имени мм файла
# 3 минуты отправки
# 4 часы отправки
# 5 дата отправки
# 6 месяц отправки
# 7 год отправки
# 8 минуты удаления
# 9 часы удаления
# 10 дата удаления
# 11 месяц удаления
# 12 год удаления
# 13 текст сообщения c хештегом
# 14 кнопки url


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

