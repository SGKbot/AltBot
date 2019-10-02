import telebot;
bot = telebot.TeleBot('930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s');
markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
itembtnPrivet  = telebot.types.KeyboardButton('Привет')
itembtnPoka    = telebot.types.KeyboardButton('Пока')
itembtncProba  = telebot.types.KeyboardButton('#Проба')
itembtndAmour  = telebot.types.KeyboardButton('Я тебя люблю')
itembtneEmpty  = telebot.types.KeyboardButton('Empty')
markup.row(itembtnPrivet, itembtnPoka, itembtncProba)
markup.row(itembtndAmour, itembtneEmpty)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == '#Проба':
        bot.send_sticker(message.chat.id, '#Проба(https://t.me/sgk_proba)')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
