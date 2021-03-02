import telebot
from telebot import types
from app import bl_as_modul

bot = bl_as_modul.bot_telebot()
#  bot = telebot.TeleBot("token")

data = [
    ("яблоки", 100, 10),  # Название, цена за кг, остаток
    ("груши", 150, 5),
    ("сливы", 200, 30),
    ("персики", 250, 16),
    ("абрикосы", 300, 1),
]


def get_keyboard(position):
    kb = telebot.types.InlineKeyboardMarkup()
    temp_arr = []  # костыль в pyTelegramBotAPI, чтобы расположить потом кнопки в ряд
    if position > 0:  # если есть куда смещаться «влево», ставим стрелку влево
        temp_arr.append(types.InlineKeyboardButton(text="←", callback_data=f"show_{position - 1}"))
    temp_arr.append(types.InlineKeyboardButton(text=f"Купить {data[position][0]}", callback_data=f"buy_{position}"))
    if position < len(data) - 1:  # # если есть куда смещаться «вправо», ставим стрелку вправо
        temp_arr.append(types.InlineKeyboardButton(text="→", callback_data=f"show_{position + 1}"))
    kb.add(*temp_arr)  # продолжение костыля. Хз, может быть, есть вариант лучше
    return kb


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Здравствуйте! Введите команду /showcase, чтобы посмотреть наши фрукты!")


@bot.message_handler(commands=["showcase"])
def cmd_showcase(message):
    bot.send_message(message.chat.id,
                     f"Предлагаем Вам следующий товар:\n\nНазвание: {data[0][0]}\nЦена за 1 кг: {data[0][1]} руб.\n"
                     f"Осталось: {data[0][2]} шт.\n\nДля просмотре товаров используйте стрелки ниже.",
                     reply_markup=get_keyboard(0))


@bot.callback_query_handler(func=lambda call: call.data.startswith("buy"))
def callback_buy(call):
    position = int(call.data.split("_")[1])
    bot.send_message(call.message.chat.id, f"Вы успешно купили {data[position][0]}!")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, types.InlineKeyboardMarkup())
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("show"))
def callback_buy(call):
    position = int(call.data.split("_")[1])
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f"Предлагаем Вам следующий товар:\n\nНазвание: {data[position][0]}\n"
                               f"Цена за 1 кг: {data[position][1]} руб.\n"
                               f"Осталось: {data[position][2]} шт.\n\nДля просмотре товаров используйте стрелки ниже.",
                          reply_markup=get_keyboard(position))
    bot.answer_callback_query(call.id)


if __name__ == "__main__":
    bot.infinity_polling()