from telethon.tl.custom import Button
from telethon import TelegramClient
from telethon.tl import types
from telethon.tl.types import (
    KeyboardButtonRow,
    KeyboardButtonCallback,
)


import cfg
# import user_info

def bot_bot():
    # bot = telebot.TeleBot(cfg.token)
    # bt = Bot(token=cfg.token)
    # dp = Dispatcher(bot)
    # bt = TelegramClient('BlAs12020', 1544232, '588b56542f3bde27c7d75eb8ba704cdc').start(bot_token=cfg.token)
    return bt

client = TelegramClient('BlAs12020', 1544232, '588b56542f3bde27c7d75eb8ba704cdc')
client.start(bot_token=cfg.token)


HS = "Здравствуйте." \
     "\n" \
     "\n" \
     "Этот бот предназначен для помощи при создании сообщений в вашем канале. Для того, " \
     "чтобы начать пользоваться:" \
     "\n" \
     " - Добавьте бота в Администраторы." \
     "\n" \
     " - Перешлите боту любое сообшение из канала" \
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
     "<a href='https://t.me/joinchat/UxMjcxD8b7UY00vf'>Подписаться на мой канал</a>"     \
     "\n" \
     "v3.0" \


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
    '<b>любая другая</b> ссылка добавляется к тексту гиперссылкой со словами “Читать далее…"' \
    '\n' \
    'Все вопросы и предложения по работе бота только в чате моего канала.' \
    '<a href="https://t.me/joinchat/UxMjcxD8b7UY00vf"> Подписаться на канал</a>'


markup1 = types.ReplyInlineMarkup(
    rows=[
        KeyboardButtonRow(
            buttons=[
                KeyboardButtonCallback(text="Tk", data="tk"),
                KeyboardButtonCallback(text="Gs", data=b"/gs"),
                KeyboardButtonCallback(text="Bal", data=b"/bal"),
            ]
        ),
        KeyboardButtonRow(
            buttons=[
                KeyboardButtonCallback(text="Task", data=b"/task"),
                KeyboardButtonCallback(text="Games", data=b"/games"),
                KeyboardButtonCallback(text="Balance", data=b"/balance"),
            ]
        )
    ]
)

Main_menu_btn_old = [
        [
            Button.text('News'),
            Button.text('Think'),
            Button.text('ADS'),
            Button.text('Hands'),
            Button.text('Help')
        ],
        [
            Button.text('Humor', resize=True, single_use=True),
            Button.text('Stolen'),
            Button.text('Sight'),
            Button.text('Comb'),
            Button.text('Send')
        ]
    ]


# , resize=True, single_use=True
Main_menu_btn = [
            Button.text('🚑   Help', resize=True),
            Button.text('#️⃣ h-tag'),
            Button.text('🛠  Tools'),
            Button.text('🏹   Send')
                 ]



hlp_but = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Выбрать канал", data=b"wrkchsel_c"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Удалить канал", data=b"wrkchdel_c"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Выйти из меню", data=b"wrkchotval"), ]),
            ]
        )


hsht_but = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="🗞  News", data=b"hsht_n"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="🚜  Hands", data=b"hsht_h"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="🤔  Think", data=b"hsht_t"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="🔭  Stolen", data=b"hsht_s"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="📢    ADS", data=b"hsht_a"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="🤹🏻‍️  Humor", data=b"hsht_hum"), ]),

            ]
        )

tools_but = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="🔛 Actions with channels", data=b"tools_ch"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="🔲 Add buttons", data=b"tools_but"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="🔀 Comb", data=b"tools_cmb"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="🧾 Info schedule", data=b"tools_inf"), ]),
            ]
        )

schinf_but = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=" Edit", data=b"mschinf_ed"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=" Delete", data=b"mschinf_del"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text=" Return", data=b"mschinf_ret"), ]),
            ]
        )

edsch = types.ReplyInlineMarkup(
            rows=[
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Photo / Video", data=b"edsch1"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Text", data=b"edsch2"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Buttons", data=b"edsch3"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Date Time", data=b"edsch4"), ]),
                KeyboardButtonRow(buttons=[KeyboardButtonCallback(text="Exit menu", data=b"edsch5"), ]),
            ]
        )
