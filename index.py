from settings import NAME
from flask import Flask, escape, request, render_template, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/salmonCookies"
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
    return render_template("sales.html", bend = bend_data, redmond = redmond_data, prineville = prineville_data)

@app.route('/create', methods=['POST'])
def create():
    data = mongo.db.locations.insert_many([
    {"city": "Bend", "sales": [13, 5, 7, 8, 0]},
    {"city": "Redmond", "sales": [1, 6, 15, 3, 4]},
    {"city": "Prineville", "sales": [9, 12, 11, 14, 10]},
])

    return "Data created"

@app.route('/destroy', methods=['POST'])
def destroy():
    data = mongo.db.locations.drop()
    return "Data destroyed"