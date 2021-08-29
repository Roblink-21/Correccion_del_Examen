import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "ORZlMw6WjbrZonjuCSLYGQiiU"
csecret = "na7ZSr4LDg9ALWCkR9OiXcaALzgZqpNIC8Zpx8i81gGyJMBc1b"
atoken = "1415799839380676620-q5GeAzTs1akXG7HO5bIynkmamTNn06"
asecret = "WG97EowAEKKVUmf5CGxUZYstmGAAr9V3sVRic9nVbRutj"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://Andres:admin@localhost:5984/')
try:
    db = server.create('ciudad5')
except:
    db = server['ciudad5']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-79.29,-0.4,-77.66,0.3])