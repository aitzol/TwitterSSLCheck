import tweepy
import os

CONSUMER_KEY = os.environ.get('APP_CONSUMER_KEY',None)
CONSUMER_SECRET = os.environ.get('APP_CONSUMER_SECRET', None)

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', None)
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEM_SECRET', None)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class TestListener(tweepy.streaming.StreamListener):
    def on_data(self, raw_data):
        print 'If you can see this, your server supports new Twitter SSL cert'
        return False

stream = tweepy.streaming.Stream(auth, TestListener())
stream.userstream()

