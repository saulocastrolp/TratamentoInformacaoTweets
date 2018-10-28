# -*- coding: utf-8 -*-
import tweepy
import datetime
from datetime import timedelta
from pytz import timezone

consumer_key = 'uQsgy2D7ygLhn1vmfAirjw'
consumer_secret = 'zy9WFiyPWVCQ3JFdE9DQRVNomRaLEw4lFRpeLQjJPw'
access_token = '47124237-tqhXldXHVHJNvuE8Zxz39eSEvqJdktNlPew8vaayU'
access_token_secret = 'PNj07Mw7WKlOzKWRolcUogarQ7Str9QvqhSvPOhIEw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

startSince = '2014-09-18 00:00:00'
endUntil = '2014-09-18 18:44:00'
for tweet in tweepy.Cursor(api.search,q="*",count=100,\
                           lang="pt",\
                           geocode="-19.649077,-44.066359,8km",\
                           since_id="2017-02-14").items():

    print(tweet.text)
    fuso_horario = timezone('America/Sao_Paulo')
    print(datetime.datetime.astimezone(tweet.created_at))
    break

        
