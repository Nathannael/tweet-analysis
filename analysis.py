from dotenv import load_dotenv
load_dotenv()

import os
import tweepy

# from sentiment_counter import MyStreamSentimentCounter
from series_ranking import MyStreamSeriesRanking

# from spacy_sentiment_counter import MySpacySentimentCounter

auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret'))

api = tweepy.API(auth)
myStreamListener = MyStreamSeriesRanking()

myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

print("iniciando")
# myStream.filter(track=['netflix'], languages=['pt'])
myStream.filter(track=[
  'Hollywood',
  'Noite Adentro',
  'Billions',
  'Supermães',
  'The Eddy',
  'Disque Amiga Para Matar',
  'Restaurantes em Risco',
  'Valéria',
  'Bordertown',
  'Outlander',
  'Gotham',
  'White Lines',
  'Mágica Para a Humanidade',
  'Índia Catalina',
  'Batalha das Flores',
  'Doces Magnólias',
  'Control Z',
  '13 Reasons Why'
], languages=['pt'])
