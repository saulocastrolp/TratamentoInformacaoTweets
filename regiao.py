# -*- coding: utf-8 -*-
import tweepy

consumer_key = 'uQsgy2D7ygLhn1vmfAirjw'
consumer_secret = 'zy9WFiyPWVCQ3JFdE9DQRVNomRaLEw4lFRpeLQjJPw'
access_token = '47124237-tqhXldXHVHJNvuE8Zxz39eSEvqJdktNlPew8vaayU'
access_token_secret = 'PNj07Mw7WKlOzKWRolcUogarQ7Str9QvqhSvPOhIEw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

arq = open("base.txt","a")
arq2 = open("ultid.txt","a")
i = 0

print("Alimentando Base de Tweets...")

try:
    for tweet in tweepy.Cursor(api.search,q="*",count=100,\
                           lang="pt",\
                           geocode="-19.649077,-44.066359,8km",\
                           since_id="2017-02-14").items():
        if(i==0):
            arq2.write(tweet.id_str)
            i = i + 1
        tweet.created_at
        arq.write(tweet.text)
        arq.write('\n')
except tweepy.RateLimitError as err:
    print("Limite Excedido..." + err.response)
arq.close()
arq2.close()
print("Finalizado...")



    

    

        
