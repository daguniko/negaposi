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

# setting mecab
m = MeCab.Tagger("-Ochasen")

# read "単語感情極性対応表"
f = open('pn_ja.dic').readlines()
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


#https://apps.twitter.com/app/8368214/keys
#http://tt-house.com/2013/08/twitter-nega-posi.html

# # for line in your_tweets:
# # 	print line.text
# # 	node = m.parseToNode(line.text.encode("utf-8"))
# # 	while node:
# # 		if node.feature.split(",")[0] == '形容詞':
# # 			if dict[node.feature.split(",")[6]]:
# # 				score_list.append(dict[node.feature.split(",")[6]]["score"].strip())

# # 		node = node.next


# # print score_list

# # sum_score = 0.0
# # for i in score_list:
# # 	sum_score += float(i)
# # average_score = sum_score / len(score_list)
# # print average_score
