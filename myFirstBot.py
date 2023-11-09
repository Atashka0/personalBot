import telebot
from telebot import types

bot = telebot.TeleBot('YOUR API KEY')

@bot.message_handler(commands = ['start'])
def commands(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode = 'html')

@bot.message_handler(commands = ['website'])
def website(message):
    markUp = types.InlineKeyboardMarkup()
    markUp.add(types.InlineKeyboardButton("Visit my website", url = "https://atashka0.github.io/"))
    bot.send_message(message.chat.id, 'Visit my personal website', reply_markup = markUp)

@bot.message_handler(commands = ['help'])
def website(message):
    markUp = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
    website = types.KeyboardButton('Website')
    start = types.KeyboardButton('Start')
    markUp.add(website, start)
    bot.send_message(message.chat.id, 'Choose what u need:', reply_markup = markUp)

@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "HiHi!", parse_mode = "html")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode = "html")
    elif message.text == "photo":
        photo = open('couple.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "I can't get u, sry", parse_mode = 'html')

bot.polling(none_stop=True)
