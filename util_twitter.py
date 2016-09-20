import tweepy
import twitter_keys


def twit_text(text):
	consumer_key, consumer_secret, access_token, access_token_secret = twitter_keys.getKeys()

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	api.update_status(test)
