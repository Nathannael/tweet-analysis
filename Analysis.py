from dotenv import load_dotenv
load_dotenv()

import os
import tweepy


from sentiment_counter import MyStreamSentimentCounter
from word_counter import MyStreamWordCounter



auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret'))

api = tweepy.API(auth)
myStreamListener = MyStreamSentimentCounter()
# myStreamListener = MyStreamWordCounter()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

print("iniciando")
myStream.filter(track=['Netflix'], languages=['pt'])
