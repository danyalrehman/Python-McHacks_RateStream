import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json



CONSUMER_KEY  = 'QtjbyJiJ3NLR2nYuU5SVbaEMF'
CONSUMER_SECRET = 'jDiECspRBGt9SdrieY3BBOtIDXFiFox3zZjAY4i7gCzAjSPd8y'
ACCESS_KEY = '721453542519795712-LNBQIFa7V7uhzt2YyUC92yvX7twmbCl'
ACCESS_SECRET= '1iZRfVomihmYf7PWgbyjtJ3YStpfW5BwKKY5gjRxCRawz'

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
search_results = api.search(q="canoe restaurant", count=100)

for i in search_results:
    print(i.text)    
# Do Whatever You need to print here
