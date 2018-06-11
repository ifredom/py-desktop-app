#!/usr/bin/python
# -*- coding:utf-8 -*-
import tweepy
import json

class TwitterConfig(object):

    def __init__(self):
        self.getConf()

    def getConf(self):
        with open('config/config.json', 'r') as f:
            self.config = json.load(f)
            self.consumer_key = self.config['consumer_key']
            self.consumer_secret = self.config['consumer_secret']
            self.access_token = self.config['access_token']
            self.access_token_secret = self.config['access_token_secret']

    def getAPI(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api

twitterconfig = TwitterConfig()
api = twitterconfig.getAPI()

other_public_tweets = api.user_timeline('LeoDiCaprio')

for tweet in other_public_tweets:
    print(tweet.text)

if __name__ == '__main__':
    pass

