import tweepy, time, os
from ratio import ratio

# setting env variables
consumer_key = os.environ.get('ratio_consumer')
consumer_key_secret = os.environ.get('ratio_consumer_secret')
access_token = os.environ.get('ratio_access')
access_token_secret = os.environ.get('ratio_access_secret')
# setting mantinus twitter ID
mantinus_id = '1317082603942563843'
# list of mantinus IDs
# accessed in [-1] to always reply to most recent tweet
mantinus_tweets = []

# twitter auth
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class Stream(consumer_key, consumer_key_secret, access_token, access_token_secret):

    def on_connect():
        print('Stream connected to mantinus twitter')

    def on_data():
        '''On data recieved, ratio tweet will be accessed, '''
        

mantinus_listener = Stream(consumer_key, consumer_key_secret, access_token, access_token_secret)

mantinus_listener.filter(follow=mantinus_id, threaded=True)