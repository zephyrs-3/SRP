import tweepy
import sys
import preprocessor as p
import nltk
from nltk.stem import WordNetLemmatizer
from flask import Flask, request, render_template
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_0123456789~'''

nltk.download('wordnet')

import csv
from nltk.tokenize import sent_tokenize, word_tokenize


consumer_key = "qzZhq8Zml22gD91APqeekciNK"                # authorization tokens
consumer_secret = "MacfJtwBkHbwd99hAJ65lDN6FB6GaDCLk6b91x1F0GSZDG83PR"
access_key = "1267426961694945288-8MRBc5pYifWZilRkX3vHzkM3ZX7WSL"
access_secret = "HBxtEcmijdFRnBEy47QmIHTRbkFbjl13c9SNMFWE6M3iq"

def listtostring(s):                                    #to convert list to string
    str1 = " "
    return (str1.join(s))

#Extract tweets from twitter
# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.id_str)
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

        # check if text has been truncated
        if hasattr(status,"extended_tweet"):
            text = status.extended_tweet["full_text"]
        else:
            text = status.text



        '''
        remove_characters = [",","\n"]
        for c in remove_characters:
            text.replace(c," ")
            quoted_text.replace(c, " ")
        '''
        text1 = listtostring(text)
        text1 = text.replace(",", " ").replace("\n", " ")                   #replacing , and \n for csv encoding
        text1=p.clean(text1)
        lemmatizer = WordNetLemmatizer()                                    # lemmatisation,punctuation removal,tokenisation
        lemr = ""
        for word in text1.split():
            lem = (lemmatizer.lemmatize(word, pos="v"))
            lem = (lemmatizer.lemmatize(lem))
            lemr = lemr + lem + " "

        no_punct = ""
        for char in lemr:
            if char not in punctuations:
                no_punct = no_punct + char

        data = word_tokenize(no_punct)
        wordsFiltered = []

        for w in data:
            wordsFiltered.append(w)
            text1=listtostring(wordsFiltered)
        with open("optweet.csv", "a", encoding='utf-8') as f:  #store pre-processed tweet in csv
            f.write("%s\n" % (text1))
            import toneanal                                #calling cat,emo,pol analyser programs
            toneanal.catfunc()
            import docemo
            docemo.emofunc()

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()

app = Flask(__name__)

@app.route('/')
def hello_world():
        return render_template("homepage.html")

@app.route('/crises1')
def crises1():
        tags = taglist3 # any no.of hashtags can be given
        # print(type(tags))
        stream.filter(languages=["en"], track=tags)
        return render_template("index2.html")

@app.route('/crises2')
def crises2():
        tags = taglist1 # any no.of hashtags can be given
        # print(type(tags))
        stream.filter(languages=["en"], track=tags)
        return render_template("index2.html")

@app.route('/crises3')
def crises3():
        tags = taglist4 # any no.of hashtags can be given
        # print(type(tags))
        stream.filter(languages=["en"], track=tags)
        return render_template("index2.html")

@app.route('/crises4')
def crises4():
        tags = taglist2 # any no.of hashtags can be given
        # print(type(tags))
        stream.filter(languages=["en"], track=tags)
        return render_template("index2.html")

@app.route('/form')
def form():
        return render_template("form.html")

#Extract tweets from twitter
# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(StreamListener, self).__init__()
        self.max_tweets = 5
        self.num_tweets = 0

    def on_status(self, status):
        print(status.id_str)
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

        # check if text has been truncated
        if hasattr(status,"extended_tweet"):
            text = status.extended_tweet["full_text"]
        else:
            text = status.text



        '''
        remove_characters = [",","\n"]
        for c in remove_characters:
            text.replace(c," ")
            quoted_text.replace(c, " ")
        '''
        text1 = listtostring(text)
        text1 = text.replace(",", " ").replace("\n", " ")                   #replacing , and \n for csv encoding
        text1=p.clean(text1)
        lemmatizer = WordNetLemmatizer()                                    # lemmatisation,punctuation removal,tokenisation
        lemr = ""
        for word in text1.split():
            lem = (lemmatizer.lemmatize(word, pos="v"))
            lem = (lemmatizer.lemmatize(lem))
            lemr = lemr + lem + " "

        no_punct = ""
        for char in lemr:
            if char not in punctuations:
                no_punct = no_punct + char

        data = word_tokenize(no_punct)
        wordsFiltered = []

        for w in data:
            wordsFiltered.append(w)
            text1=listtostring(wordsFiltered)
        with open("optweet.csv", "a", encoding='utf-8') as f:  #store pre-processed tweet in csv
            f.write("%s\n" % (text1))
            import toneanal                                    #calling cat,emo,pol analyser programs
            toneanal.catfunc()
            import docemo
            docemo.emofunc()
            self.num_tweets += 1
            if self.num_tweets <= self.max_tweets:
                if self.num_tweets % 100 == 0:  # just to see some progress...
                    print('Number of tweets captured so far: {}'.format(self.num_tweets))
                return True
            else:
                return False

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()



if __name__ == "__main__":

    #tagd=sys.argv[1]
    #print(tagd)
    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)


    streamListener = StreamListener()                      # initialize stream
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
    with open("optweet.csv", "w", encoding='utf-8') as f:
        f.write("tweets\n")
    taglist1 = ["IndoPakistaniWars"]
    taglist2 = ["KoreanConflict"]
    taglist3 = ["corona","covid 19"]
    taglist4 = ["climate change"]
    #taglist4 = ["culturalgenocide","UyghurGenocide"]
    #print(taglist1)
    #if(tagd=="COVID-19 outbreak (2020)"):
    app.run(debug='true')







                     #filtering only english tweets