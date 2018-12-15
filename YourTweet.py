#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 07:41:01 2018

@author: john
"""

from flask import Flask, request #import main Flask class and request object
from twython import Twython

APP_KEY = 'MWQadaodeKZ02JKLfkJA8OhF9'  # Customer Key here
APP_SECRET = 'hVGVTiEtAEFwzLZLB6gpa8IaI2xrdv9l4G7S61AbcI3lrPwcU3'  # Customer secret here
OAUTH_TOKEN = '2942702198-rybhZK6kteq3c1KyIoXXLtV3C49Q8LlW2VkQcz5'  # Access Token here
OAUTH_TOKEN_SECRET = 'ErFaebAlbAfL1e4yh2NjEx1VBCFQq8En6OurUbHYyUKKY'  # Access Token Secret here

app = Flask(__name__) #create the Flask app

@app.route('/twitter')
def twitter():
    tweet = request.args.get('tweet') #if key doesn't exist, returns None
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    twitter.update_status(status=tweet)
    return '''<h1>Your tweet is: {}</h1>'''.format(tweet)    

if(__name__) == '__main__':
    app.run(debug=True)  