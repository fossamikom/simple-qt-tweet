#!/usr/bin/python

import tweepy
import sys
import webbrowser 
import urllib

CONSUMER_KEY = 'gYMpKX6YWDP5rBwvCcriQ'
CONSUMER_SECRET = 'ulK4WA6gtB5FekyPYRrOXVCxeqvwP66leFfNq5DY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url =auth.get_authorization_url()
print 'Membuka browser untuk melakukan autentication'
webbrowser.open(auth_url)
print  auth_url
inputs = raw_input('Setelah autentication tekan enter ').strip()
try:
	auth.get_access_token(inputs)
except tweepy.TweepError:
    print 'error !! gagal mendapatkan access token'
api = tweepy.API(auth)
f=open('ACCESS_KEY' ,'w')
f1=open('ACCESS_SECRET','w')
f2=open('user_info' ,'w')

f.write(auth.access_token.key)
f1.write(auth.access_token.secret)

f.close()
auser=api.me()
print auser.id
f2.write('%s\n' % auser.screen_name)
f2.write('%s' % auser.id)
f2.close
f1.close 

urllib.urlretrieve (auser.profile_image_url, "%s.jpg" % auser.id)
















