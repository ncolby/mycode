#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template


app = Flask(__name__)

# forgot the @
@app.route("/")
@app.route("/start")
def start():
    return render_template("home.html")

@app.route("/correct")
def success():
    return f"Outstanding, all hail the lich king"

@app.route("/login", methods = ["POST"])
def login():
    if request.form.get("nm") == "i don't know but he was right".lower():
        return redirect("/correct")
    
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
