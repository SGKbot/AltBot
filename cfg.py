token = '1219481769:AAFrlaSczx4xa0OtsBGp51dESfNmoJrH6zg'  # Токен бота sgk_work_bot
#  token = '930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s'  # Токен бота sgk_espace_bot



us_in = 'user_info.py'  # создание, обработка БД пользователей с атрибутами user.db
user_db = '/users/sgk/Documents/github/AltBot/user.db'  # файл с !!!ПУТЕМ!!! где хранится вся информация о пользователях с уникальными атрибутами
user_font = '/users/sgk/Documents/github/AltBot/FreeMono.ttf'
sql_create_user_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        bot_chat_id integer , 
                                        channel_chat_id integer PRIMARY KEY,
                                        channel_name text NOT NULL,
                                        pkanal integer,
                                        vkanal text,
                                        telo text,
                                        user_chan_link text,
                                        mm integer,
                                        chn integer,
                                        InlKeyBut integer,
                                        mmfid text
                                    ); """

Pr = "Давайте познакомимся." \
     "\n" \
     "\n" \
     "Перейдите в свой канал и добавьте бота в Администраторы, " \
     "\n" \
     "затем отправьте любое ваше сообщение из канала боту." \
