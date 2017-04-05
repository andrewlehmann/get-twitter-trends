import tweepy
import keyring

# Set all keys
consumer_key = keyring.get_password('Twitter', 'ConsumerKey') #'kTKrup9MEEYYIaGFXIH09d4dT'
secret_key = keyring.get_password('Twitter', 'ConsumerSecret')
access_token = keyring.get_password('Twitter', 'AccessToken')
access_token_secret =  keyring.get_password('Twitter', 'AccessSecret')

# Connect to Twitter API
auth = tweepy.OAuthHandler(consumer_key, secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
trends = api.trends_place(1)

# Retrieve trend data
data = trends[0]
trends = data['trends']

# Create list of trend names and print
names = []

for trend in trends:
	names.append(trend['name'])
for entry in range(10):
	print(names[entry])
