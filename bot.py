import os
from main import give_subs,check_link
import telebot


bot_tok = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(bot_tok)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello!!, please type `/help` to get help !!")

    print(f"{message.from_user.username}:{message.from_user.first_name} -> {message.text}")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Type `/getsubs` then paste the link for your video!! ")

    print(f"{message.from_user.username}:{message.from_user.first_name} -> {message.text}")

@bot.message_handler(commands=['getsubs'], content_types=["text"])
def f_link(message):
    arr = message.text.strip()  # Remove leading/trailing whitespace
    fulnk = arr.split("getsubs")[1].strip()  # Remove leading/trailing whitespace
    print(f"{message.from_user.username}:{message.from_user.first_name} -> {message.text}")
    if (fulnk):
        try:
            bot.reply_to(message,give_subs(check_link(fulnk)))
        except:
            bot.reply_to(message,"### Message form developer the telegram api dosent allows to send too many strings so please bare with until we fix this, you can try with videos with less subs!!!, thank you!!")
    else:
        bot.reply_to(message, "Command usage: /getsubs <link>")

bot.infinity_polling()
