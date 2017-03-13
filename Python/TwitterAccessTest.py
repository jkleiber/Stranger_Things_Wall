# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:43:25 2017

@author: jklei
"""
import oauth2
import json

CONSUMER_KEY = '2vu0AHWypSQm7lNfhdCW8YEDT'
CONSUMER_SECRET = '0x023XKQTER03tychcqIOrO9rbWK8GwBfKLlnwwpLZX5mxwPXx'

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

tweets_json = json.loads(oauth_req( 'https://api.twitter.com/1.1/search/tweets.json?q=%23upbstrangerthings',
                              '360864683-JcaMwzWjrwBiEtMuAPV4I6JhcnE0PmkQYBcUCPNy',
                              'RrggArWx80l8fwqpG5BdvYcZQAenmglsPkvyHO2PKJPPO'))
#print tweets_json['statuses'][0]['id']

for tweet in tweets_json['statuses']:
    print tweet['text']