from lib.tools import save_to_file
import re

import tweepy
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

nlp = spacy.load("en_core_web_md")

words = []
result = {}
count = 0

class MyStreamWordCounter(tweepy.StreamListener):
  def on_status(self, status):
    global count

    count += 1
    save_to_file({ 'count': count }, filename="number_tweets.json")

    tweet_without_symbols = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",status.text).split())

    result = self.tokenize_using_spacy(tweet_without_symbols, 'NOUN')
    save_to_file(result)

  def tokenize_using_spacy(self, tweet, pos):
    doc = nlp(tweet)

    for token in doc:
        if token.is_stop:
            continue
        if token.pos_ == pos:
            if token.lemma_ in result:
                result[token.lemma_] += 1
            else:
                result[token.lemma_] = 1

    print(doc)

    return result

  @classmethod
  def empty_vars(self):
    global words
    global result
    global count

    words = []
    result = {}
    count = 0
