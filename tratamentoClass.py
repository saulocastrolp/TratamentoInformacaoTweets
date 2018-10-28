# -*- coding: utf-8 -*-
from unicodedata import normalize
import re

class Tratamento:

    def __init__(self, tweet=None):
        self.tweet = tweet

    ### Remove acentuações ###
    def remover_acentos(self, expr):
       return normalize('NFKD', expr).encode('ASCII', 'ignore').decode('ASCII')

    ### Remove caracteres especiais ###
    def removeChrEspeciais(self, expr):
        return re.sub(r'[^a-zA-Z0-9\\]', '', expr)

    ### Identifica Links ###
    def identificaLinks(self, expr):
        if(re.match(r'^https?:/.*$', expr)):
            return True
        return False

    ### Identifica Retweets ###
    def identificaRTs(self, expr):
        if(re.match(r'^rt\s?@\w+:', expr)):
            return True
        return False
    
    ### Identifica Mentions ###
    def identificaMentions(self, expr):
        if(re.match(r'@\b\w*\W?\w*', expr)):
            return True
        return False

    def getTweet(self):
        return self.tweet
    
    def setTweet(self, tweet):
        self.tweet = tweet