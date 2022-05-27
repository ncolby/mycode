#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
from flask import redirect
app = Flask(__name__)

pokedata = [{
  "pokemons": {
    "charmander": {
      "img": "https://wallpaperaccess.com/full/18953.jpg"
    },
    "bulbasaur": {
      "img": "https://i.pinimg.com/originals/ed/d4/ff/edd4ff3473e3a85b774d79fcadc0886b.gif"
    },
    "squirtle": {
      "img": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d7ebf501-d835-4c15-9782-1332ea9fb086/de2sg3g-dc38958a-9028-43b3-ad0e-b12f4648b184.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q3ZWJmNTAxLWQ4MzUtNGMxNS05NzgyLTEzMzJlYTlmYjA4NlwvZGUyc2czZy1kYzM4OTU4YS05MDI4LTQzYjMtYWQwZS1iMTJmNDY0OGIxODQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.vGRTu_AZpaNTP-cE1Fa3yXJBr8eNWnQDtos_vISTlQM"
    }
  }
}]

choice = ""

@app.route("/")
def jsonroute():
    return jsonify(pokedata)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/choicemade", methods= ["POST", "GET"])
def starter():
    # 3 to this function?
    startermon = request.args.get("startermon")
    return render_template("starter.html", data = pokedata, mon = startermon)


@app.route("/setpokemon", methods = ["POST"])
def setpokemon():
    # 1  can I send starter from this root
    if request.form.get("nm"):
        choice = request.form.get("nm")
    else:
        choice = "charmander"

    print(choice)
    # 2 through this redirect
    print(url_for("starter", startermon = choice))
    return redirect(url_for("starter", startermon = choice))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
