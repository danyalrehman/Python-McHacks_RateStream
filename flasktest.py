from flask import Flask, render_template, request, json
import tweepy
import codecs
from textblob import TextBlob

app = Flask(__name__)

CONSUMER_KEY = 'QtjbyJiJ3NLR2nYuU5SVbaEMF' 
CONSUMER_SECRET = 'jDiECspRBGt9SdrieY3BBOtIDXFiFox3zZjAY4i7gCzAjSPd8y'
ACCESS_KEY = '721453542519795712-LNBQIFa7V7uhzt2YyUC92yvX7twmbCl'
ACCESS_SECRET = '1iZRfVomihmYf7PWgbyjtJ3YStpfW5BwKKY5gjRxCRawz'

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/signUp',methods=['POST'])
def recordhistory():
    auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    search_results = api.search(q='Trump', count=100)
    
    for tweet in search_results:
        if tweet.lang == 'en':
            coord_string = ""
            if tweet.coordinates is not None:
                coord_string = str(tweet.coordinates[0]) + ', ' + str(tweet.coordinates[1])
            history = codecs.open('history.txt', 'a', 'utf-8')
            history.write('user: ' + tweet.user.name + ', coordinates: ' + coord_string + ', text: ' + "".join(tweet.text.splitlines()) + ', polarity: ' + str(TextBlob(tweet.text).polarity) + '\n')
            history.close()
        else:
            print(tweet.text)

    return json.dumps({'html':'<span>Great success!!</span>'})

if __name__ == "__main__":
    app.run()

