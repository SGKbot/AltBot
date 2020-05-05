import telebot
import cfg
# import user_info

def bot_telebot():
    bot = telebot.TeleBot(cfg.token)
    return bot


HS = "Здравствуйте." \
     "\n" \
     "\n" \
     "Этот бот предназначен для помощи при создании сообщений в вашем канале. Для того, " \
     "чтобы начать пользоваться:" \
     "\n" \
     " - Введите имя канала, куда вы будете отправлять сообщения в формате " \
     "https://t.me/SGK_espace " \
     "\n" \
     " - Добавьте бота в Администраторы." \
     "\n \n" \
     "Теперь Вы можете прикреплять к своим сообщениям хэштеги, автоматически добавлять" \
     " ссылку на источник, скачивать видео с youtube, добавлять к изображению водяной знак." \
     "\n" \
     "<a href='https://telegra.ph/file/8ed76b876a0b67a01ef66.mp4'> " \
     "Посмотреть короткое видео по работе бота.</a>" \
     "\n \n" \
     "Простота бота накладывает ограничения - вы всегда работаете только с последним ВИДИМЫМ в боте сообщением." \
     " Настроить расположение водяного знака нельзя. Любая отправленная ссылка (кроме на ютуб) формирует “Читать далее”." \
     " Ссылка на ютуб скачивает видео. Отправленная картинка или видео возвращаются с водяным знаком. " \
     "\n" \
     "Данный проект не является коммерческим, поэтому у него нет специального чата поддержки. " \
     "Если у вас возникнет необходимость обсудить работу бота зарегистрируйтесь на моем канале или " \
     "<a href='https://t.me/joinchat/EHLktEzzYJXpERD7UgaHFQ'>задайте вопрос сразу в чате.</a> " \
     "\n" \
     "<a href='https://t.me/SGK_espace'>Подписаться на мой канал</a>"     \
     "\n" \
     "v1.2" \


HSK = '\n \n' \
    '<b>       Клавиши:</b>' \
    '\n' \
    '<b>Теги:</b>' \
    '\n' \
    '<b>News</b>      Новости' \
    '\n' \
    '<b>Stolen</b>      Украдено' \
    '\n' \
    '<b>Think</b>      Подумай' \
    '\n' \
    '<b>ADS</b>         Реклама' \
    '\n' \
    '<b>Sight</b>       Мнение автора' \
    '\n' \
    '<b>Hands</b>     Дача, своими руками' \
    '\n' \
    '<b>Humor</b>    Юмор' \
    '\n \n' \
    '<b>       Действия:</b>' \
    '\n' \
    '<b>Comb</b>    Объединить картинку или видео с сообщением' \
    '\n' \
    '<b>Send</b>      Отправить подготовленное сообщение в ваш канал' \
    '\n' \
    '<b>Help</b>       Помощь по боту' \
    '\n \n' \
    '<b>       Действия без клавиш:</b>' \
    '\n' \
    'Отправить боту текст в двойных русских буквах -  <b>ьь</b>выделить жирным шрифтом<b>ьь</b> .' \
    '\n' \
    'Отправить боту gif_ку - возвращает полную информацию о файле, в том числе id .' \
    '\n' \
    '<b>Отправить боту картинку</b> возвращается картинка с указанием на ваш канал.' \
    '\n' \
    '<b>Отправить боту видеофайл</b> возвращается видео с бегущей строкой вашего канала.' \
    '\n' \
    '<b>Отправка боту ссылки</b>' \
    '\n' \
    '<b>- на ютуб</b> возвращает видеофайл' \
    '\n' \
    '<b>- на ваш канал</b> в последующем, если вам надо, добавляет в тег гиперссылку на канал, пишет на картинке, отправленной боту вашу ссылку, добавляет в видео бегущую строку с вашей ссылкой.' \
    '\n' \
    'Формат https://t.me/SGK_espace' \
    '\n' \
    '<b>любая другая</b> ссылка добавляется к тексту гиперссылкой со словами “Читать далее…"' \
    '\n' \
    'Все вопросы и предложения по работе бота только в чате моего канала.' \
    '<a href="https://t.me/SGK_espace"> Подписаться на канал</a>'
