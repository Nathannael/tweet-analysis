from dotenv import load_dotenv
load_dotenv()

import os
import tweepy

# from stream_listeners.sentiment_counter import MyStreamSentimentCounter
# from stream_listeners.spacy_sentiment_counter import MySpacySentimentCounter
# from stream_listeners.word_counter import MySpacySentimentCounter
from stream_listeners.word_counter import MyStreamWordCounter
from stream_listeners.series_ranking import MyStreamSeriesRanking
from dashboards.plot_graphs import PlotGraphs
from lib.tools import SERIES


auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret'))

api = tweepy.API(auth)
myStreamListener = MyStreamWordCounter()

myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

print("iniciando")
myStream.filter(track='blacklivesmatter', languages=['en'], is_async=True)
PlotGraphs.commence_the_plotting()
