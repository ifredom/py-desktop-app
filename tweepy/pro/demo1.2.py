#!/usr/bin/python
# coding:utf-8
import tweepy
import json

consumer_key = 'dkYGHcJMl4enNsNIMJYE3vx0M'
consumer_secret = 'F0zCq4ietgc0zAIvDeugLGOeou8AMpyTXk7O8WirvdZe9aI1G5'
access_token = '796625332501671936-nu7pw8sL71pVTztbXjooyZnT5Q8xrfL'
access_token_secret = '1GAx8IQPtaDiIZ9BMB4SgpphIGjZdcWbrEjnDD5YaEmtf'

# 获取特朗普的最新twitter

# 提交你的Key和secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# 获取类似于内容句柄的东西
api = tweepy.API(auth)

# 写文件，不存在就创建
def wfile(data):
    with open("test.json", "w") as f:
        f.write(json.dumps(data, indent=2))

# 读文件
def rfile():
    with open("test.json", "r") as f:
        json_obj = json.load(f)

# 打印其他用户主页上的时间轴里的内容。美国总统.特朗普
other_public_tweets = api.user_timeline('realDonaldTrump')
dicts = []
for tweet in other_public_tweets:
    temp = {}
    temp['text'] = tweet.text
    dicts.append(temp)
wfile(dicts)
