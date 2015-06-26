#! /usr/local/bin/python
# -*-coding:utf-8-*-

import tweepy
import MeCab
import ConfigParser

# read conf
conf = ConfigParser.SafeConfigParser()
conf.read('secret.ini')

consumer_key = conf.get('oauth','consumer_key')
consumer_secret = conf.get('oauth','consumer_secret')
access_token = conf.get('oauth','access_token')
access_token_secret = conf.get('oauth','access_token_secret')
negaposi_dictionary = conf.get('negaposi','dict')

# setting mecab
m = MeCab.Tagger("-Ochasen")

# read dictionary file
f = open(negaposi_dictionary).readlines()
dict = {}
score_list = []

for i in f:
	a = i.strip().split(":")
	dict.setdefault(a[0],{})["yomi"] = a[1]
	dict.setdefault(a[0],{})["pos"] = a[2]
	dict.setdefault(a[0],{})["score"] = a[3]
	dict.setdefault(a[1],{})["pos"] = a[2]
	dict.setdefault(a[1],{})["score"] = a[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

your_tweets = api.user_timeline()

print your_tweets
