from telethon import TelegramClient, events
from datetime import date
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

api_id = 123456
api_hash = "1233456789"
bot_token = '1219481769:AAFrlaSczx4xa0OtsBGp51dESfNmoJrH6zg'

bot = TelegramClient("bot", api_id, api_hash)

class MyStyleCalendar(DetailedTelegramCalendar):
    empty_month_button = ""
    empty_year_button = ""


@bot.on(events.NewMessage(pattern="/start"))
async def reply_handler(event):
    calendar, step = DetailedTelegramCalendar(telethon=True, min_date=date.today()).build()
    await event.respond(f"Select {LSTEP[step]}", buttons=calendar)


@bot.on(events.CallbackQuery(pattern=DetailedTelegramCalendar.func(telethon=True)))
async def calendar_handler(event):
    result, key, step = DetailedTelegramCalendar(telethon=True, min_date=date.today()).process(event.data.decode("utf-8"))

    if not result and key:
        await event.edit(f"Select {LSTEP[step]}", buttons=key)
    elif result:
        await event.edit(f"You selected {result}")


bot.start(bot_token=bot_token)
with bot:
    bot.run_until_disconnected()