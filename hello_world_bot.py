#!/usr/bin/python
# -*- coding: utf-8 -*-

owner = "ojahnn"		# Name des Accounts, an den Fehlermeldungen gesendet werden
import my_config
import tweepy
import traceback

def login():
    # for info on the tweepy module, see http://tweepy.readthedocs.org/en/

    # Authentication is taken from my_config.py
    consumer_key = my_config.consumer_key
    consumer_secret = my_config.consumer_secret
    access_token = my_config.access_token
    access_token_secret = my_config.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

def stick_together_output():
	output = "Hello World!"
    return output

def tweet_something(debug):
    api = login()
    try:
        output = stick_together_output()
        if debug:
            print output
        else:
            api.update_status(status=output)
            print output
    except:
        error_msg = traceback.format_exc().split("\n", 1)[1][-130:]
        api.send_direct_message(screen_name = owner, text = error_msg + " " + time.strftime("%H:%M:%S"))

tweet_something(False)