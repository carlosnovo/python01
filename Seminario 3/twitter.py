# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import twitter
import io
import json
__author__ = 'Francisco Jose Macias Periñan, Carlos Alberto Novo Foncubierta'

# Go to http://twitter.com/apps/new to create an app and get these items
# See https://dev.twitter.com/docs/auth/oauth for more information on Twitter's OAuth implementation
def login():
    CONSUMER_KEY = '5gEpPPIsEsfM9bfSn5pC36is2'
    CONSUMER_SECRET = 'BqY7CGo82XMhCnJJDBdFje4KpLfF4JCy4TJMXqyAUbAJm6DcD9'
    OAUTH_TOKEN = '369164054-NHiU8nuEVALkToTwPmz7g16q5kc97RaDHodE0ISN'
    OAUTH_TOKEN_SECRET = 'ZH4KT9rKBzvUaLp99oj2DAEE0QA21app8FMdTXIXdRPpx'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(domain='api.twitter.com', api_version='1.1', auth=auth)

#Función para grabar la información en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Función para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()