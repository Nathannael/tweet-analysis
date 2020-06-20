from dotenv import load_dotenv
load_dotenv()

import os
import tweepy
import time

from stream_listeners.word_counter import MyStreamWordCounter

from lib.tools import save_to_file


class Analysis:
  @classmethod
  def perform(self, keyword):
    auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
    auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret'))

    api = tweepy.API(auth)
    myStreamListener = MyStreamWordCounter()

    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    save_to_file({})

    print('Iniciando')
    print(keyword)

    myStream.filter(track=[keyword], languages=['en'], is_async=True)
    return myStream

  @classmethod
  def stop(self, streamer):
    MyStreamWordCounter.empty_vars()
    streamer.disconnect()
