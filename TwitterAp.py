#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:07:36 2020

@author: clintonpotter
"""

from twython import Twython
import json

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

results = python_tweets.search(q= 'from:TheRock', count = 100)
all_tweets = results['statuses']

for tweet in all_tweets:
    print(tweet['text'])
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')    



