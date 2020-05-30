from dotenv import load_dotenv
load_dotenv()

import os
import tweepy

from sentiment_counter import MyStreamSentimentCounter

from spacy_sentiment_counter import MySpacySentimentCounter

auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret'))

api = tweepy.API(auth)
myStreamListener = MySpacySentimentCounter()
# myStreamListener = MyStreamWordCounter()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

print("iniciando")
myStream.filter(track=['Netflix'], languages=['pt'])