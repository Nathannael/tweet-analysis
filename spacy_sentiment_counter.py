from textblob import TextBlob
import tweepy
import nltk

import spacy
from spacymoji import Emoji

from collections import Counter

word_list = []

class MySpacySentimentCounter(tweepy.StreamListener):
  def on_status(self, status):
    blacklist = ['netflix', 'rt', 'https', 't', 'co', 'q', 'a', 'o', 'e', 'n', 'pq', 'vc']

    nlp = spacy.load("pt_core_news_sm")
    emoji = Emoji(nlp)
    nlp.add_pipe(emoji)

    tokens = nlp(status.text.lower())

    words = [token.text for token in tokens if token.is_stop != True and token.is_punct != True 
             and token._.is_emoji != True and token.text not in blacklist]
    word_list.extend(words)

    fdist = nltk.FreqDist(word_list)
    print('10 MAIS FREQUENTES:')
    print(fdist.most_common(10))
    print('\n')