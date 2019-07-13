from settings import NAME
from flask import Flask, escape, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/salmonCookies"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    print('Name:', NAME)
    f"NAME: {NAME}"
    return render_template("hello.html", name=NAME)

@app.route('/sales')
def sales():
    return render_template("sales.html", total=42)

@app.route('/create')
def create():
    print(mongo)
    data = mongo.db.insert({"location": "redmond"})
    return render_template("hello.html", total=42)