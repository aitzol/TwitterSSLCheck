import tweepy
import os
import sys

CONSUMER_KEY = os.environ.get('CONSUMER_KEY',None)
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', None)

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', None)
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET', None)

class TestListener(tweepy.streaming.StreamListener):
    def on_data(self, raw_data):
        print 'If you can see this, your server supports new Twitter SSL cert'
        return False


def main():
    if CONSUMER_KEY==None or CONSUMER_SECRET==None \
      or ACCESS_TOKEN==None or ACCESS_TOKEN_SECRET==None:
        print 'You must set all the environment variales, see README.rst'
        sys.exit()

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = tweepy.streaming.Stream(auth, TestListener())
    stream.userstream()
    
if __name__=='__main__':
    main()
