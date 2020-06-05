import tweepy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import json

tokenizer = RegexpTokenizer(r'\w+')
nltk.download('stopwords')

words = []

series = [
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
]


results = {}

class MyStreamSeriesRanking(tweepy.StreamListener):
  def on_status(self, status):
    print(status.text)

    for serie in series:
      if serie.lower() in status.text.lower():
        results[serie] = results.get(serie, 0) + 1

    json_file = json.dumps(results)
    f = open("data.json","w")
    f.write(json_file)
    f.close()

    print(results)
