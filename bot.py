import os
from main import give_subs,check_link
import telebot
from summarizer import rise
import time

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
        if(check_link(fulnk)):
            try:
                transcript = give_subs(check_link(fulnk))
                bot.reply_to(message,transcript)
                # bot.reply_to(message,"Summarising your transcript . . .")
                up_transcript = rise(transcript)
                # time.sleep(2)
                print(f"transcript: {up_transcript}")
                # bot.reply_to(message,up_transcript)
            except Exception as e:
                bot.reply_to(message,f"### Message form developer the telegram api dosent allows to send too many strings so please bare with until we fix this, you can try with videos with less subs!!!, thank you!!{e}")
                
        else:
            bot.reply_to(message,"Enter a valid Link")
    else:
        bot.reply_to(message, "Command usage: /getsubs <link>")

bot.infinity_polling()
