import tweepy
import keyring

# Set all access keys for Twitter API
# keyring is a python package that one can use to retrieve
# a previously saved password so as to mask my API keys
consumer_key = keyring.get_password('Twitter', 'ConsumerKey')
consumer_secret = keyring.get_password('Twitter', 'ConsumerSecret')
access_token = keyring.get_password('Twitter', 'AccessToken')
access_secret =  keyring.get_password('Twitter', 'AccessSecret')

# Connect to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Retrieve trend data as a list, use parameter 1 for global trends
trends = api.trends_place(1)[0]['trends']

# Create and print list of names of top 50 current trends
print([trend['name'] for trend in trends])
