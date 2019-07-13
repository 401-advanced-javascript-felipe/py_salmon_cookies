from settings import NAME
from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Adam:', NAME)
    f"NAME: {NAME}"
    return render_template("hello.html", name=NAME)