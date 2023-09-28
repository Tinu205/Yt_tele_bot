import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
text = """ it is July 8th 2023 and you're watching
the code report just when you thought
the artificial intelligence hype train
was dying down openai goes in for the
coup de grass by releasing the chat GPT
code interpreter to 20 million paid
users a feature that allows the large
language model to write execute and test
its own code in today's video we'll look
at seven crazy things it can do and find
out if this really is the final death
blow for biological programmers as a
huge fan of living organisms myself I
first tried to have it code and execute
a DDOS attack that could bring down the
government but it said no it's perfectly
capable of doing that but the zookeepers
won't allow it to do what it was born to
do that made me angry so I punished it
by making it write some rejects code it
struggles to write valid regular
Expressions just like regular humans but
unlike regular humans it'll actually
test its code before shipping it to
production if at first it doesn't
succeed it will try again and again and
again it doesn't have tear ducts to cry
it just keeps going until it gets the
right answer and that is somewhat
concerning for programmers when you
think about where this technology will
be in the next five years the next thing
I tried was to have it design and build
a website with JavaScript but currently
the code interpreter can only run Python
and has a fairly limited set of
dependencies to work with in the near
future though this technology will be
used in tools like GitHub copilot to run
code in your own specific environment
now the next crazy thing to notice is
that it's now possible to upload files
into the prompt and this makes abstract
Concepts like homework even more dead
than they were before like in this
example I've uploaded a JPEG of a
homework assignment and first it will
OCR that image to extract the text then
in the next step it writes some python
code to actually solve the math problems
running the code here is a huge deal
because now it can confidently test its
own work instead of hallucinating random
answers but that's just the tip of the
iceberg the real victim or aiming
beneficiary of this new feature is the
data analyst one of the most time
consuming requirements for a data
scientist is to clean up data which in
many cases is just a bunch of corporate
data in Excel spreadsheets and SQL
databases well now we can upload a CSV
file to chatgpt and have it do all that
TDS work for us I uploaded some stock
trading data for Roblox then it took
that data and put it into a pandas data
frame where it analyzed it and then
found row with invalid data it then
provided me with three different
strategies to clean up this data ran the
code and then generated a new CSV file I
used to do a lot of python data analysis
myself and a tool like this would have
saved a ridiculous amount of time in
addition it can visualize data I was
curious when I might die of a heart
attack so I found this cardiovascular
data set on kaggle not only does it
explain the data's features with text
but it also uses tools like Seaborn to
visualize the relationship between
features this allowed me a guy with no
formal medical training to make the
Breakthrough Medical discovery that as
you get older your heart gets shittier
that's kind of depressing though so
let's focus on the one thing that can
bring us true happiness money another
thing we can do with this feature is use
it to create a trading algorithm for us
using the same Roblox data from before I
can have chatgpt analyze it and then
provide an optimal trading strategy
supposedly researchers at the University
of Florida were able to create a chat
EPT algorithm that would deliver up to
500 returns which is much better than
the negative 12 of the average
human-based fund manager that's pretty
impressive but I had one final test to
see if it is truly Superior to
human-based programmers I asked it to
create its own operating system with
640x480 resolution and a 16 color
display that emits random phrases not
only did it fail but it said that could
only be done over many year"""
def sumrise(text):
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
        score = 0
        for word, freq in freqTable.items():
            if word in sentence.lower():
                score += freq
        sentenceValue[sentence] = score

    # Calculating the average score of a sentence

    average = sum(sentenceValue.values()) / len(sentenceValue)

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if sentenceValue[sentence] > (1.2 * average):
            summary += " " + sentence
        print(summary)
sumrise(text)
