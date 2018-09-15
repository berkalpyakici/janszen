from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
app.debug = True


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
def search-text():
    if request.method == 'POST':
        city = request.form['city']
        print(city)
    return render_template('index.html')

@app.route('/search-geolocation', methods=['GET','POST'])
def search-text():
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        print(latitude, longitude)
    return render_template('index.html')


app.run()
