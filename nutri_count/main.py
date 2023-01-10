from flask import Flask
from flask import render_template
from flask import request

from nutri_count_database import new_entry, display, compare_value, empty_csv

app = Flask("nutri_count")


@app.route("/", methods=["GET", "POST"])  # Startseite
def start():
    if request.method == "POST":
        empty_csv()
    display_data = display() #zeigt inhalt von csv
    return render_template("index.html", display=display_data, seitentitel="Home")


@app.route("/new", methods=["GET", "POST"])  # add new product
def new():
    title = "Neues Produkt"
    if request.method == "GET":
        return render_template("nutri_form.html", seitentitel=title)

    if request.method == "POST":  # Werte generieren
        product_name = request.form["product_name"]
        amount = request.form["amount"]
        energy = request.form["energy"]
        fat = request.form["fat"]
        fat_acids = request.form["fat_acids"]
        carbs = request.form["carbs"]
        sugar = request.form["sugar"]
        protein = request.form["protein"]
        salt = request.form["salt"]
        new_entry(product_name, amount, energy, fat, fat_acids, carbs, sugar, protein, salt)
        return render_template("nutri_form.html", seitentitel=title, entry_added = True)

@app.route("/compare")
def compare():
    show = compare_value()
    return render_template("compare.html", seitentitel="Vergleichen", show_compare=show)



@app.route("/viz")  # display nutris
def grafik():
    return "hoi, siehe hier deine übersicht?"


if __name__ == "__main__":
    app.run(debug=True, port=5550)
