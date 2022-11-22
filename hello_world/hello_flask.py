import random

from flask import Flask
from flask import render_template

app = Flask("Hello World")


@app.route("/greet_all")
def greet_all():
    auswahl = ["Michi", "Jackson", "Urs", "Peter"]
    return render_template('hello_all.html', alle_namen=auswahl)

@app.route('/franz') #URL
def hello_world():
    auswahl = ["Michi", "Jackson", "Urs", "Peter"]
    ausgewaehlter_name = random.choice(auswahl)
    return render_template('hello.html', name= ausgewaehlter_name)

@app.route('/hallo')
def hallo_world():
    return '<h1>Hallo, World!<h1>'

@app.route('/calc
def calc():
    zahl_1 = 2
    zahl_2 = 3
    summe = zahl_1 + zahl_2
    return render_template(summe)


if __name__ == "__main__":
   app.run(debug=True, port=5000)
