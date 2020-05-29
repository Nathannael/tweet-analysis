import tweepy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
nltk.download('stopwords')

words = []

class MyStreamWordCounter(tweepy.StreamListener):
  def on_status(self, status):
    blacklist = stopwords.words('portuguese')
    blacklist.extend(['netflix', 'rt', 'https', 't', 'co', 'q'])

    tweet_text = status.text.lower()

    print("Tweet:")
    print(status.text)
    print("\n")

    print("Tokens:")
    tokens = [ word for word in tokenizer.tokenize(tweet_text) if not word in blacklist ]
    print(tokens)
    print("\n")

    words.extend(tokens)

    # print("Blobs:")
    # blob = TextBlob(status.text)
    # print(blob.tags)
    # print(blob.noun_phrases)
    # print("\n")

    print("MAIS COMUNS:")
    fdist = nltk.FreqDist(words)
    print(fdist.most_common(10))
    print("\n\n\n")
