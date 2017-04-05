import tweepy
import keyring

# Set all keys
consumer_key = keyring.get_password('Twitter', 'ConsumerKey')
secret_key = keyring.get_password('Twitter', 'ConsumerSecret')
access_token = keyring.get_password('Twitter', 'AccessToken')
access_token_secret =  keyring.get_password('Twitter', 'AccessSecret')

# Connect to Twitter API
auth = tweepy.OAuthHandler(consumer_key, secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Retrieve trend data as a list, use 1 to get global trends
trends = api.trends_place(1)[0]['trends']

# Create list of trend names, then print
names = [trend['name'] for trend in trends]

for name in names:
	print(name)
