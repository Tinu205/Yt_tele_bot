import os
from main import give_subs
import telebot
import re
bot_tok = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(bot_tok)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello!!, please type `/help` to get help !!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,"Type `/getsubs` then paste the link for your video!! ")


@bot.message_handler(commands = ['getsubs'],content_types=["text"]) 
def f_link(message):
    arr = message.text
    fulnk = arr.split("getsubs")[1]
    if(fulnk):
        bot.reply_to(message,give_subs(fulnk))
    else:
        bot.reply_to(message,"Command usage /givesubs <link>")



bot.infinity_polling()