import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import os
from main import give_subs, check_link
import telebot
#from summarizer import rise
import time

bot_tok = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(bot_tok)

MAX_MESSAGE_LENGTH = 4065
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello!!, please type `/help` to get help !!")
    print(f"{message.from_user.username}:{message.from_user.first_name} -> {message.text}")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Hi I can help to you to get transcripts(subtitles) of youtube videos.Type `/getsubs` then paste the link for your video!!")
    print(f"{message.from_user.username}:{message.from_user.first_name} -> {message.text}")

@bot.message_handler(commands=['getsubs'], content_types=["text"])
def f_link(message):
    arr = message.text.strip()  # Remove leading/trailing whitespace
    fulnk = arr.split("getsubs")[1].strip()  # Remove leading/trailing whitespace
    print(f"{message.from_user.username}:{message.from_user.first_name} -> {message.text}")
    if fulnk:
        if check_link(fulnk):
            try:
                transcript = give_subs(check_link(fulnk))
                if len(transcript) <= MAX_MESSAGE_LENGTH:
                    bot.reply_to(message, transcript)
                    #up_transcript = rise(transcript)
                    #print(f"transcript: {up_transcript}")
                else:
                    chunks = [transcript[i:i+MAX_MESSAGE_LENGTH] for i in range(0, len(transcript), MAX_MESSAGE_LENGTH)]
                    for chunk in chunks:
                        bot.reply_to(message, chunk)
                        time.sleep(1)  # Delay between sending chunks
                    #up_transcript = rise(transcript)
                    #print(f"transcript: {up_transcript}")
            except Exception as e:
                #bot.reply_to(message, f"### Message from developer: The Telegram API doesn't allow sending too many strings, so please bear with us until we fix this. You can try with videos with fewer subtitles. Thank you! Error: {e}")
                print(f"{e}")
        else:
            bot.reply_to(message, "Enter a valid link")
    else:
        bot.reply_to(message, "Command usage: /getsubs <link>")

bot.infinity_polling()
