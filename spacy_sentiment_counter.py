from textblob import TextBlob
import tweepy
import spacy

# python3 -m spacy download pt_core_news_sm
nlp = spacy.load("pt_core_news_sm")

class MySpacySentimentCounter(tweepy.StreamListener):
  def on_status(self, status):
    print(status.text)

    polarity = TextBlob(status.text).translate(to='en').sentiment.polarity

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
