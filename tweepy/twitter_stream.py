from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# Appropriate libraries from Tweepy to trawl the twitter stream are located in the import  files above. 

# In order to extract data from twitter you require a consumer key, tokens as well as secrets code obtained directly from the twitter website
# Those can be found in the following strings below
consumerKey = 'QtjbyJiJ3NLR2nYuU5SVbaEMF' 
consumerSecret = 'jDiECspRBGt9SdrieY3BBOtIDXFiFox3zZjAY4i7gCzAjSPd8y'
aToken = '721453542519795712-LNBQIFa7V7uhzt2YyUC92yvX7twmbCl'
aSecret = '1iZRfVomihmYf7PWgbyjtJ3YStpfW5BwKKY5gjRxCRawz'

# The required class that obtains the data from Twitter and prints it out can be found in the following class below. 
class listener(StreamListener):

	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status
		return True

# The functions that are required in order to call the consumer keys and the twitter stream are found in the following code.
auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(aToken, aSecret) 

twitterStream = Stream(auth, listener())
twitterStream.filter(track="Restaurants")
