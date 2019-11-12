#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:31:36 2019

@author: prudhveer
"""

import json
import os
import sys
import tweepy
from tweepy import API
from tweepy import OAuthHandler
from tweepy import AppAuthHandler
from tweepy import Cursor
import datetime
startDate = datetime.datetime(2019, 9, 9, 0, 0, 0)
endDate =   datetime.datetime(2019, 9, 4, 0, 0, 0)



consumer_key='bFfMzi17BoJp6KmtYJELlXP2K'
consumer_secret='lVga8tf5WLoQArnsXg7kZ0NBOq11UuTCUYW3tPpeSxmHwtEO2r'
auth = AppAuthHandler(consumer_key,consumer_secret)
api = API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if __name__ == '__main__':
    user=sys.argv[1];
    #client=get_twitter_client()
    fname = "{}_only_hashtags12.json".format(user)


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
replies=[]
replies1=[]
replies2=[]





with open(fname, 'w') as f:
    for full_tweets in Cursor(api.search,q="#MarinaSilva",include_rts=False).items(100000000000):
           if not full_tweets.retweeted and 'RT @' not in full_tweets.text:
#               if full_tweets.lang == "hi":
                        tweet_id=full_tweets.id
                        print("Tweet :",full_tweets.text)
                        
                        json.dump(full_tweets._json,f,ensure_ascii=False)
                        f.write("\n")
#                        for reply in get_reply1(user,full_tweets.id):
                            #if reply.created_at < endDate and reply.created_at > startDate:
 #                               json.dump(reply._json,g,ensure_ascii=False)
  #                              g.write("\n")


  #for elements in replies:
#     print("Replies :",elements)
#  replies.clear()
        #for ligaments in tweetsFinal1:
#print("tweets:",ligaments)


#for elements in replies:
#print("Replies :",elements)



