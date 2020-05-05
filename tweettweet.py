import tweepy
import json
from os import environ

consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_key = environ['ACCESS_KEY']
access_secret = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def filter(fulltweet):
    a_file = open("translated_words.txt", "r")
    bad_word = {}
    for line in a_file:
        stripped_line = line.strip()
        x, y = stripped_line.split(" = ")
        bad_word[x] = y
    a_file.close()
    fulltweet = fulltweet.lower()
    for bad in bad_word:
        if bad == 'fuck':
            newtweet = fulltweet.replace(bad, bad_word[bad])
        else:
            newtweet = newtweet.replace(bad, bad_word[bad])
    return(newtweet)

# Function to extract tweets 
def get_tweets_by_name(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth, wait_on_rate_limit=True)
        newtweet = api.user_timeline(id = username)
        listtweet = []
        for i in range(0,5):
            status = newtweet[i]
            json_str = json.dumps(status._json)
            #deserialise string into python object
            parsed = json.loads(json_str)
            new = filter(parsed["text"])
            listtweet.append(new)

            # print(json.dumps(parsed, indent=4, sort_keys=True))
        return(listtweet)

# Function to extract tweets 
def get_tweets_by_word(word): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth, wait_on_rate_limit=True)
        newtweet = api.search(q = word, result_type = "popular")
        listtweet = []
        for i in range(0,5):
            status = newtweet[i]
            json_str = json.dumps(status._json)
            #deserialise string into python object
            parsed = json.loads(json_str)
            stringit = str(parsed["text"])
            new = filter(stringit)
            listtweet.append(new)

            # print(json.dumps(parsed, indent=4, sort_keys=True))
        return(listtweet)
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    word = input("word:")
    get_tweets_by_word(word)
