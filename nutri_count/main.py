from flask import Flask
from flask import render_template
from flask import request

from nutri_count_database import new_entry, display

app = Flask("nutri_count")


@app.route("/")  # Startseite
def start():
    display_data = display()
    return render_template("index.html", display=display_data, seitentitel="start")


@app.route("/new", methods=["GET", "POST"])  # add new product
def new():
    if request.method == "GET":
        return render_template("nutri_form.html", seitentitel="Neues Produkt")

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
        print(f"Produktname: {product_name}")  # Werte ausgeben in console
        print(f"Menge:(ml oder g) {amount}")
        print(f"Energie: {energy}")
        print(f"Fett: {fat}")
        print(f"Davon Fettsäuren: {fat_acids}")
        print(f"Kohlenhydrate: {carbs}")
        print(f"Davon Zucker: {sugar}")
        print(f"Eiweiss: {protein}")
        print(f"Salz: {salt}")
        new_entry(product_name, amount, energy, fat, fat_acids, carbs, sugar, protein, salt)
        return "Produkt wurde erfolgreich hinzugefügt!"


@app.route("/viz")  # display nutris
def grafik():
    return "hoi, siehe hier deine übersicht?"


@app.route("/advice")  # Gives you an advice
def advice():
    return "hoi, hier eine Empfehlung!"


if __name__ == "__main__":
    app.run(debug=True, port=5550)
