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


