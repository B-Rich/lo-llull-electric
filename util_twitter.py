import tweepy
import twitter_keys

consumer_key, consumer_secret, access_token, access_token_secret = twitter_keys.getKeys()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

'''
user = api.get_user('twitter')


print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)
'''

api.update_status("Lore Ipsum...")
