import os
from settings import NAME
from flask import Flask, escape, request, render_template, url_for
from flask_pymongo import PyMongo

MONGO_URL = os.environ.get('MONGODB_URI')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/salmonCookies";


app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URL
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    print('Name:', NAME)
    f"NAME: {NAME}"
    return render_template("home.html", name=NAME)

@app.route('/sales')
def sales():
    bend_data = mongo.db.locations.find_one({"city": "Bend" })
    redmond_data = mongo.db.locations.find_one({"city": "Redmond" })
    prineville_data = mongo.db.locations.find_one({"city": "Prineville" })
    if bend_data is None:
        bend_data = {"city": "Bend", "sales": [0, 0, 0, 0, 0]}

    if redmond_data is None:
        redmond_data = {"city": "Redmond", "sales": [0, 0, 0, 0, 0]}

    if prineville_data is None:
        prineville_data = {"city": "Prineville", "sales": [0, 0, 0, 0, 0]}

    return render_template("sales.html", bend = bend_data, redmond = redmond_data, prineville = prineville_data)

@app.route('/create', methods=['POST'])
def create():
    data = mongo.db.locations.insert_many([
    {"city": "Bend", "sales": [13, 5, 7, 8, 0]},
    {"city": "Redmond", "sales": [1, 6, 15, 3, 4]},
    {"city": "Prineville", "sales": [9, 12, 11, 14, 10]},
])

    return render_template("home.html", name=NAME)

@app.route('/destroy', methods=['POST'])
def destroy():
    data = mongo.db.locations.drop()
    return render_template("home.html", name=NAME)