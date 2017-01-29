from __future__ import absolute_import, print_function

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
from textblob import TextBlob

ckey = 'QtjbyJiJ3NLR2nYuU5SVbaEMF' 
csecret = 'jDiECspRBGt9SdrieY3BBOtIDXFiFox3zZjAY4i7gCzAjSPd8y'
atoken = '721453542519795712-LNBQIFa7V7uhzt2YyUC92yvX7twmbCl'
asecret = '1iZRfVomihmYf7PWgbyjtJ3YStpfW5BwKKY5gjRxCRawz'

temp = input('Please enter a restaurant name: ')
	
class listener(StreamListener):

    def on_data(self, data):
	
       decoded = json.loads(data)

       tweet = TextBlob(decoded["text"])

       datastring=('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
       print(datastring)
       print("\n")
       print("Polarity: ", decoded.sentiment.polarity)
       print('\n')
       savefile=open('twitterdata.txt','a')
       savefile.write(datastring)
       savefile.write('\n')
       savefile.close()
       return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = listener()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # GEOBOX for the locations

    stream = Stream(auth, l)
    stream.filter(track=[str(temp)+' Restaurant'], locations=[], languages=['en'])

