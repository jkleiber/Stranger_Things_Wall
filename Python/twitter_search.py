#!/usr/bin/python
import re
import serial
from time import sleep
from credentials import *

regex = re.compile('[^a-zA-Z]')
sft = re.compile('#UPBStrangerThings')
#myPort = serial.Serial('/dev/ttyUSB0', 115200, timeout = 10)
myPort = serial.Serial('/dev/ttyS1', 115200, timeout = 10)
myPort.write("Hello, world!")

tweet_id_list = []

while True:
    try:
        print "Searching..."
        ['#UPBStrangerThings','#upbstrangerthings','#UPBstrangerthings']
        
        
        
	     # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            if tweet['id'] not in tweet_id_list:
                no_hashtag = sft.sub('',  tweet['text'], flags=re.IGNORECASE)
                text_only = regex.sub('', no_hashtag).encode('ascii', 'ignore')
                print text_only
                tweet_id_list.append(tweet['id'])
                
                for character in text_only:
                    print character
                    myPort.write(character)
                    sleep(0.5)
                    
    except Exception: #We don't care about handling errors. We cannot display them to the wall anyways
        pass

	sleep(60)

myPort.close()
