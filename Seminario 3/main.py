from flask import Flask, render_template
from flask import request
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
from informacion import *

app = Flask(__name__)
GoogleMaps(app)


@app.route("/buscar", methods=['POST'])
def buscar():
	termino = request.form['text'] 
	coordenadas = getTweetsSearch(termino)
	
	mymap = Map(
		identifier="view-side",
		lat=40.3450396,
		lng=-3.6517684,
		zoom=6,
		markers=coordenadas,
		style="height:800px;width:800px;margin:0;"
	) 
	return render_template('mapa.html', mymap=mymap)

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)