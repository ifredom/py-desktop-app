#!/usr/bin/python
#coding:utf-8
import tweepy

# https://apps.twitter.com/获取自己的appKey
# 代理，系统代理模式改为 全局模式
#填写twitter提供的开发Key和secret
consumer_key = 'dkYGHcJMl4enNsNIMJYE3vx0M'
consumer_secret = 'F0zCq4ietgc0zAIvDeugLGOeou8AMpyTXk7O8WirvdZe9aI1G5'
access_token = '796625332501671936-nu7pw8sL71pVTztbXjooyZnT5Q8xrfL'
access_token_secret = '1GAx8IQPtaDiIZ9BMB4SgpphIGjZdcWbrEjnDD5YaEmtf'

#提交你的Key和secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#获取类似于内容句柄的东西
api = tweepy.API(auth)

#打印我自己主页上的时间轴里的内容
my_public_tweets = api.home_timeline()

#打印其他用户主页上的时间轴里的内容
other_public_tweets = api.user_timeline('LeoDiCaprio')

#hello python 发送到自己的帐号上
api.update_status('hello python for twitter')

#搜索具有League of Legends(lol英雄联盟的全称)的关键词的帐号
for tweet in tweepy.Cursor(api.search,q='League of Legends').items(10):
    print('Tweet by: @' + tweet.user.screen_name)

for tweet in my_public_tweets:
    print(tweet.text)

for tweet in other_public_tweets:
    print(tweet.text)
