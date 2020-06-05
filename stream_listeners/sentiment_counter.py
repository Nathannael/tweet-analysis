import tweepy
import json
from textblob import TextBlob

neutral = 0
positive = 0
negative = 0

class MyStreamSentimentCounter(tweepy.StreamListener):
  def on_data(self, data):
    tweet = json.loads(data)

    text = None

    try:
      text = self.extract_text(tweet)
    except BaseException as e:
      print("Error on_data %s" % str(e))

    if text:
      print(text)
      polarity = TextBlob(text).translate(to='en').sentiment.polarity

      print("A polaridade é " + str(polarity))
      if (polarity > 0):
        global positive
        positive = positive + 1
      elif polarity < 0:
        global negative
        negative = negative + 1
      else:
        global neutral
        neutral = neutral + 1

      print("sentimentos:")
      print("positive: ", str(positive))
      print("negative: ", str(negative))
      print("neutral: ", str(neutral))
      print("\n\n\n")

  def on_error(self, status):
    if status == 420:
        return False
    print(status)

  def extract_text(self, tweet):
    try:
      #RT
      return tweet['retweeted_status']['extended_tweet']['full_text']
    except KeyError:
      try:
        #tweets longos
        return tweet['extended_tweet']['full_text']
      except KeyError:
        try:
          #tweets curtos
          return tweet['text']
        except BaseException as e:
          print("Error on_data %s" % str(e))
          return None
