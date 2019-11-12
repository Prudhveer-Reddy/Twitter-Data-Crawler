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



consumer_key='bFfMzi17BoJp6KmtYJELlXP2K'
consumer_secret='lVga8tf5WLoQArnsXg7kZ0NBOq11UuTCUYW3tPpeSxmHwtEO2r'
auth = AppAuthHandler(consumer_key,consumer_secret)
api = API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if __name__ == '__main__':
    user=sys.argv[1];
    #client=get_twitter_client()
    fname = "{}_only_tweets.json".format(user)


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
replies=[]
replies1=[]
replies2=[]



def get_reply1(user,tweet_id):
    sinceID=tweet_id
    
    searchQuery="to:" +user+ " since_id:"+ str(sinceID)+" filter:replies"
    print(searchQuery)
    maxTweets = 20
    tweetsPerQry=100
    tweetCount = 0
    max_id = -1
    print("getting replies for "+user+" "+str(tweet_id))
    while tweetCount< maxTweets:
        try:
            if (max_id<=0):
                
                replies= api.search(q=searchQuery, count = tweetsPerQry ,sinceID = sinceID)
            else:
                replies= api.search(q=searchQuery, count = tweetsPerQry ,max_id=str(max_id-1)   ,sinceID = sinceID)
            for reply in replies:
                
                if(tweetCount == maxTweets):
                    break
                if reply.in_reply_to_status_id==sinceID:
                    yield reply
                    print("replies: ",reply.text)
                    tweetCount += 1
                if (len(replies) != 0):
                    max_id = replies[-1].id
            print(tweetCount)
                
        except tweepy.TweepError as e:
            print("ERROR>>>"+str(e))
            break;


with open(fname, 'w') as f:
        for full_tweets in Cursor(api.user_timeline,id=user).items(8000):
           if not full_tweets.retweeted and 'RT @' not in full_tweets.text:
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



