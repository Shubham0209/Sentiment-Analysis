from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="4VAiBAB6w1zkRmZ491JpOhv"
csecret="24J1JrSoXLQj0j468IKseentO94evrCtmqlHGVxc1CDIJZ"
atoken="1027182879401435132AtzdplfPmZ3QdG8l5lqRojY"
asecret="dlwhNXVnACOs4oRyeOlcE2cKBCekLVUmKYLtkxHS"

class listener(StreamListener):

    def on_data(self, data):
        all_data=json.loads(data)
        tweet= ascii(all_data["text"])
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["education"])
		
