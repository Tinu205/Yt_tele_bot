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

def rise(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Creating a frequency table to keep the
    # score of each word

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score
    # of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq



    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text

    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    
    return summary



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
    if fulnk:
        if check_link(fulnk):
            try:
                transcript = give_subs(check_link(fulnk))
                if len(transcript) <= MAX_MESSAGE_LENGTH:
                    bot.reply_to(message, transcript)
                    up_transcript = rise(transcript)
                    print(f"transcript: {up_transcript}")
                else:
                    chunks = [transcript[i:i+MAX_MESSAGE_LENGTH] for i in range(0, len(transcript), MAX_MESSAGE_LENGTH)]
                    for chunk in chunks:
                        bot.reply_to(message, chunk)
                        time.sleep(1)  # Delay between sending chunks
                    up_transcript = rise(transcript)
                    print(f"transcript: {up_transcript}")
            except Exception as e:
                #bot.reply_to(message, f"### Message from developer: The Telegram API doesn't allow sending too many strings, so please bear with us until we fix this. You can try with videos with fewer subtitles. Thank you! Error: {e}")
                print(f"{e}")
        else:
            bot.reply_to(message, "Enter a valid link")
    else:
        bot.reply_to(message, "Command usage: /getsubs <link>")

bot.infinity_polling()
