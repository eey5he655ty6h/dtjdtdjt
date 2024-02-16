import telebot

token = "6704909847:AAGs7nmzWI3dIo4wyO1Ed-v1unDYoCZh-rs"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "هلو")

@bot.message_handler(func=lambda m: "بايو" in m.text)
def bio(message):
    bot.reply_to(message, "ممنوع")

bot.polling()