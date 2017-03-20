# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:43:25 2017

@author: Justin Kleiber
"""
import oauth2
import json
import serial
from time import sleep
from credentials import *
import re

#tweets we have seen before
tweet_id_list = []

#this is how you authenticate yourself with Twitter nowadays (OAuth2)
def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

sleep(60)

serialPort = serial.Serial('/dev/ttyS0', 115200, timeout = 10)

#Tests serial port communication with a themed message on startup
#serialPort.write("Welcome to the upside down")

#Run the program forever
while(True):
    try:
        #find tweets with the #UPBStrangerThings hashtag. Note: not case sensitive
        tweets_json = json.loads(oauth_req( 'https://api.twitter.com/1.1/search/tweets.json?q=%23upbstrangerthings',
                              twitter_access_token, twitter_access_token_secret))
        #print tweets_json
    
        #Iterate through all the tweets we found
        for tweet in tweets_json['statuses']:
            #We only care about tweets we have not seen, and we also want to ignore retweets
            if tweet['id'] not in tweet_id_list and 'retweeted_status' not in tweet:
                tweet_id_list.append(tweet['id']) #add tweet to list of seen tweets
                                
                first_hashtag = tweet['text'].find('#')
                if not first_hashtag == -1:
                    clean_text = tweet['text'][:first_hashtag]
                else:
                    clean_text = tweet['text']
            
                #remove urls
                clean_text = re.sub(r"http\S+", "", clean_text)
            
                for character in clean_text:
                    print character
                    try:
                        serialPort.write(character.encode())
                    except:
                        pass
                    sleep(0.75)
    except KeyError: #We don't care about handling errors. We cannot display them to the wall anyways
        print "Retweeted_Status not found"
    sleep(60)
                
serialPort.close()