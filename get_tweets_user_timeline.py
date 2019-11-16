import os
from requests_oauthlib import OAuth1Session
import csv
import json

# load Twitter API credentials

# ref: https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_token = info['ACCESS_KEY']
    access_token_secret = info['ACCESS_SECRET']


params = {"ids": "30973", "format": "detailed"}

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')
print("Got OAuth token: %s" % resource_owner_key)

# # Get authorization
base_authorization_url = 'https://api.twitter.com/oauth/authorize'
authorization_url = oauth.authorization_url(base_authorization_url)
print('Please go here and authorize: %s' % authorization_url)
verifier = input('Paste the PIN here: ')

# # Get the access token
access_token_url = 'https://api.twitter.com/oauth/access_token'
oauth = OAuth1Session(consumer_key,
                     client_secret=consumer_secret,
                     resource_owner_key=resource_owner_key,
                     resource_owner_secret=resource_owner_secret,
                     verifier=verifier)

oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens['oauth_token']
access_token_secret = oauth_tokens['oauth_token_secret']

# Make the request
oauth = OAuth1Session(consumer_key,
                       client_secret=consumer_secret,
                       resource_owner_key=access_token,
                       resource_owner_secret=access_token_secret)
new_tweets = oauth.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Starbucks&count=200&include_rts=1&exclude_replies=1", params = params)



print("Response status: %s" % new_tweets.status_code)
print("Body: %s" % new_tweets.text)

#Save it in the JSON format

with open('starbucks_data_compare.json','w') as outfile:
    json.dump(new_tweets.text, outfile)
