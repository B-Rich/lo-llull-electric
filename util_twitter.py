import tweepy
import twitter_keys

consumer_key, consumer_secret, access_token, access_token_secret = twitter_keys.getKeys()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def twit_text(text):
    global api
    api.update_status(text)

def get_twits(username):
    global api
    twits = api.user_timeline(username)
    return twits

def get_following(username):
    global api
    return api.friends_ids(username)
