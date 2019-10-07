import telebot;                                                            #  Подключение модуля из стандартной библиотеки
bot = telebot.TeleBot('930977876:AAFpDgzP81IKXIULREWXIeWbxTxHGydHg6s'); 
from telebot import types                                                  #  подключаем атрибут

markup = types.ReplyKeyboardMarkup(True, True)                             #  Создаем объект типа ReplyKeyboardMarkup()

itembtnPrivet  = types.KeyboardButton('Привет')                            
itembtnPoka    = types.KeyboardButton('Пока')
itembtncProba  = types.KeyboardButton('#Проба')
itembtndAmour  = types.KeyboardButton('Я тебя люблю')
itembtneEmpty  = types.KeyboardButton('Empty')
markup.row(itembtnPrivet, itembtnPoka, itembtncProba)                      #  добавляем построчно элементы
markup.row(itembtndAmour, itembtneEmpty)

@bot.message_handler(commands=['start'])                                   #  декоратор
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup)

@bot.message_handler(content_types=['text'])                                #  декоратор
def send_text(message):                                                     # Определим функцию
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
