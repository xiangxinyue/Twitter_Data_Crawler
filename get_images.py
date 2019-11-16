#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
import json
import wget

#Twitter Authentication
with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_token = info['ACCESS_KEY']
    access_token_secret = info['ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Creating tweepy api
api = tweepy.API(auth)

user = "Starbucks"

#Getting all tweets
all_tweets = api.user_timeline(screen_name= user, count=200,
include_rts=False, exclude_replies=True)

last_tweet_id = all_tweets[-1].id

#Getting more tweets
while True:
    more_tweets = api.user_timeline(screen_name=user, count=200,
    include_rts=False,
    exclude_replies=True,
    max_id=last_tweet_id - 1)

    if len(more_tweets) == 0:
    break

    else:
        last_tweet_id = more_tweets[-1].id - 1
        all_tweets = all_tweets + more_tweets

image_files = set()
for status in all_tweets:
    media = status.entities.get('media', [])
if len(media) &amp;amp;amp;amp;gt; 0:
    image_files.add(media[0]['media_url'])

print ('Downloading ' + str(len(image_files)) + ' images.....')
for image_file in image_files:
    wget.download(image_file)
