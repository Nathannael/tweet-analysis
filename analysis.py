from dotenv import load_dotenv
load_dotenv()

import os
import tweepy

# from sentiment_counter import MyStreamSentimentCounter
# from spacy_sentiment_counter import MySpacySentimentCounter
from series_ranking import MyStreamSeriesRanking
from plot_graphs import PlotGraphs
import constants


auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret'))

api = tweepy.API(auth)
myStreamListener = MyStreamSeriesRanking()

myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

print("iniciando")
myStream.filter(track=constants.SERIES, languages=['pt'], is_async=True)

