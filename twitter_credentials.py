#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

# create a dictionary to store your twitter credentials

twitter_cred = dict()

# Enter your own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = 'wGyDy46GXGCkYh7uFmzVmMVG9'
twitter_cred['CONSUMER_SECRET'] = 'lZJwRnNJi5L03l1adTLtJFY8rktZuO617VfaG0H2xeIN5NG1g2'
twitter_cred['ACCESS_KEY'] = '1187837983258374144-no6MrW7Ocqaf1TDys7CkDq2wPvJ9Sq'
twitter_cred['ACCESS_SECRET'] = 'LauB50AaYeK6uG8RUJAZt7gtrzHcVsHD1971nJPCKJEAj'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public

with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)
