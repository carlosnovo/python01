# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
# Seminario 3
# 13/04/2015
# Autores:
#   Francisco Jose Macias Periñan
#   Carlos Alberto Novo Foncubierta

import twitterAPI
import json
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

twitter_api =  twitterAPI.oauth_login()

app = Flask(__name__)
GoogleMaps(app)

def busca_tweets(palabra) :
    resultados = twitter_api.search.tweets(q=palabra, count='100', geocode="36.5320510864,-6.2976899147,100km")
    tweets = resultados['statuses']

    coord = []
    for tweet in tweets :
        if tweet['coordinates'] is not None: 
            coord.append([tweet["coordinates"].values()[1][1], tweet["coordinates"].values()[1][0]])
    
    return coord

def definirMapa(coord):
    mapa = Map(
        identifier="view-side",
        lat=37.34632165458624,
        lng=--4.576500650000071,
        zoom=7,
        markers=coord,
        style="height:500px;width:800px;margin:0;"
    ) 
    return mapa

@app.route('/')
def defecto():
    mapa = definirMapa(buscarTweets("cadiz"))
    return render_template('localizacion.html', palabra="hola", mymap=mapa)
@app.route('/palabra/<palabra>')
def personalizada(palabra):
    mapa = definirMapa(buscarTweets(palabra))
    return render_template('localizacion.html', palabra=palabra, mymap=mapa)

if __name__ == "__main__":
    app.run(debug=True)
