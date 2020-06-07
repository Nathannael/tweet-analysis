import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import tweepy
from lib.tools import SERIES
from lib.tools import save_to_file

tokenizer = RegexpTokenizer(r'\w+')
nltk.download('stopwords')

words = []

results = {}

class MyStreamSeriesRanking(tweepy.StreamListener):
  def on_status(self, status):
    print(status.text)
    print('\n----\n')

    for serie in SERIES:
      if serie.lower() in status.text.lower():
        results[serie] = results.get(serie, 0) + 1

    save_to_file(results)
