from flask import Flask, render_template, request, send_from_directory

import maps
import json

app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/dependencies/<path:path>')
def send_dependencies(path):
    return send_from_directory('dependencies', path)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/search-text', methods=['GET','POST'])
def search_text():
    if request.method == 'POST':
        city = request.form['city']
        m = maps.maps();
        output = m.zipcode_data(city)

        listoflocations = []
        locationslist = ''
        indx = 0

        if output[1]:
            if output[0]:
                for val in output[0]["results"]:
                    locationslist += str(indx)+': { center: {lat: '+str(val['geometry']['location']['lat'])+', lng: '+str(val['geometry']['location']['lng'])+'}, size: 1609.34}'
                    indx += 1

                    if indx < len(output[0]["results"]):
                        locationslist += ','

                return render_template("map.html", locations = locationslist, map_zoom = 12, map_center_lat = output[1][0], map_center_lng = output[1][1])
            else:
                return render_template("map_empty.html")
        else:
            return render_template("map_error.html")


@app.route('/search-geolocation', methods=['GET','POST'])
def search_geolocation():
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']

        location_tuple = (latitude, longitude)

        m = maps.maps();
        output = m.geolocation_data(location_tuple)

        listoflocations = []
        locationslist = ''
        indx = 0

        for val in output[0]["results"]:
            locationslist += str(indx)+': { center: {lat: '+str(val['geometry']['location']['lat'])+', lng: '+str(val['geometry']['location']['lng'])+'}, size: 1609.34}'
            indx += 1

            if indx < len(output[0]["results"]):
                locationslist += ','

    return render_template("map.html", locations = locationslist, map_zoom = 12, map_center_lat = output[1][0], map_center_lng = output[1][1])

app.run(host='127.0.0.1', port=80)
