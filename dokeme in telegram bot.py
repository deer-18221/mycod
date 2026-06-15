import telebot

bot=telebot.TeleBot('8350080027:AAEi95Hh_nbM2wx1ef_zhxrvqB9D1kflZMU')

from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton

bb=InlineKeyboardButton(text="join",url="https://t.me/Twinshtt")
reply_keyboard=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)

reply_keyboard.add(bb)

@bot.message_handler(commands="start")

def start(msg):
    bot.send_message(msg.chat.id," salam khosh omadi ",reply_markup=reply_keyboard)

@bot.message_handler(func=lambda msg:True)
def check_buton(msg):
    if msg.text=="join":      
        bot.reply_to(msg,"https://t.me/Twinshtt")


bot.polling()
