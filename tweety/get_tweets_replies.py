#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import csv
import json

# load Twitter API credentials

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_token = info['ACCESS_KEY']
    access_token_secret = info['ACCESS_SECRET']

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)

# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The Twitter user who we want to get tweets from
name = "Starbucks"
# Number of tweets to pull
tweetCount = 200

#initialize a list to hold all the tweepy Tweets
alltweets = []

#make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name = name,count=200)

#save most recent tweets
alltweets.extend(new_tweets)

#save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1

#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
    print("getting tweets before %s" % (oldest))

    #all subsiquent requests use the max_id param to prevent duplicates
    new_tweets = api.user_timeline(screen_name = name,count=200,max_id=oldest)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #update the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    print("...%s tweets downloaded so far" % (len(alltweets)))



# Calling the user_timeline function with our parameters
#results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled


for tweet in alltweets:
   # printing the text stored inside the tweet object
   print(tweet.text)
# transforming the tweets into a 2D array that will be used to populate the csv


outtweets = [[tweet.id_str, tweet.created_at,
tweet.text.encode('utf-8')] for tweet in alltweets]

# writing to the csv file

with open('starbucks_replies.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'created_at', 'text'])
    writer.writerows(outtweets)
