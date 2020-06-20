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
tweets_total = 0
most_retweeted = {}
sources = {}

class MyStreamWordCounter(tweepy.StreamListener):
  def on_status(self, status):
    global tweets_total

    text = self.extract_text(status)
    self.track_retweets(status)
    self.track_sources(status)

    tweets_total += 1
    save_to_file({ 'count': tweets_total }, filename="number_tweets.json")

    tweet_without_symbols = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ", text).split())

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
    print("-------\n")

    return result

  def extract_text(self, tweet):
    if hasattr(tweet, "retweeted_status"):  # Check if Retweet
      try:
        return tweet.retweeted_status.extended_tweet["full_text"]
      except AttributeError:
        return tweet.retweeted_status.text
    else:
      try:
        return tweet.extended_tweet["full_text"]
      except AttributeError:
        return tweet.text

  def track_retweets(self, tweet):
    global most_retweeted

    if hasattr(tweet, "retweeted_status"):  # Check if Retweet
      id_rt = tweet.retweeted_status.id_str
      if id_rt in most_retweeted:
        most_retweeted[id_rt] += 1
      else:
        most_retweeted[id_rt] = 1

      save_to_file(most_retweeted, filename="most_retweeted.json")

  def track_sources(self, tweet):
    global sources

    source = tweet.source
    if source in sources:
      sources[source] += 1
    else:
      sources[source] = 1

    save_to_file(sources, filename="sources.json")

  @classmethod
  def empty_vars(self):
    global words
    global result
    global tweets_total
    global sources
    global most_retweeted

    words = []
    result = {}
    sources = {}
    most_retweeted = {}
    tweets_total = 0
