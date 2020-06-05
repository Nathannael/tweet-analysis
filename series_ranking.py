import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import json
import tweepy
import constants

tokenizer = RegexpTokenizer(r'\w+')
nltk.download('stopwords')

words = []

results = {}

class MyStreamSeriesRanking(tweepy.StreamListener):
  def on_status(self, status):
    print(status.text)
    print('\n----\n')

    for serie in constants.SERIES:
      if serie.lower() in status.text.lower():
        results[serie] = results.get(serie, 0) + 1

    json_file = json.dumps(results)
    f = open("data.json","w")
    f.write(json_file)
    f.close()
