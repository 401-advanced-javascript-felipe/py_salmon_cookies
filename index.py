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
    return render_template("sales.html", total=42)

@app.route('/create', methods=['POST'])
def create():
    data = mongo.db.locations.insert({"location": "TerrorBone"})
    return "Data created"