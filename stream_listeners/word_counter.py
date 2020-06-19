import tweepy
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from lib.tools import save_to_file

tokenizer = RegexpTokenizer(r'\w+')
nltk.download('stopwords')
nlp = spacy.load("en_core_web_md")

words = []
result = {}

class MyStreamWordCounter(tweepy.StreamListener):
  def on_status(self, status):
    result = self.tokenize_using_spacy(status.text, 'NOUN')
    save_to_file(result)

  def tokenize_by_stopwords(self, tweet):
    banlist = stopwords.words('english')
    banlist.extend(['rt', 'https', 't', 'co', 'q'])

    tweet_text = tweet.lower()

    tokens = [ word for word in tokenizer.tokenize(tweet_text) if not word in banlist ]

    words.extend(tokens)

    fdist = nltk.FreqDist(words)
    return dict(fdist.most_common(10))

  def tokenize_using_spacy(self, tweet, pos):
    doc = nlp(tweet)

    for token in doc:
        if token.is_stop:
            continue
        if token.pos_ == pos:
            if token.lemma_ in result:
                result[token.lemma_] += 1
            else:
                result[token.lemma_] = 1

    print(doc)

    return result

  @classmethod
  def empty_vars(self):
    global words
    global result

    words = []
    result = {}
