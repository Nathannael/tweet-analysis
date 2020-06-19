from dotenv import load_dotenv
load_dotenv()

import os
import tweepy
import time

# from stream_listeners.sentiment_counter import MyStreamSentimentCounter
# from stream_listeners.spacy_sentiment_counter import MySpacySentimentCounter
# from stream_listeners.word_counter import MySpacySentimentCounter
from stream_listeners.word_counter import MyStreamWordCounter
from stream_listeners.series_ranking import MyStreamSeriesRanking

from lib.tools import SERIES
from lib.tools import save_to_file


class Analysis:
  @classmethod
  def perform(self, keyword):
    auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
    auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret'))

    api = tweepy.API(auth)
    myStreamListener = MyStreamWordCounter()

    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.words = []
    myStream.result = {}
    print('Iniciando')
    print(keyword)
    save_to_file({})
    myStream.filter(track=[keyword], languages=['en'], is_async=True)
    return myStream
