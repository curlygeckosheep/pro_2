from flask import Flask
from flask import render_template
from flask import request

from nutri_count_database import new_entry, display, compare_value, empty_csv

app = Flask("nutri_count")

@app.route("/")  # Startseite
def start():
    display_data = display() #zeigt inhalt von csv
    return render_template("index.html", display=display_data, seitentitel="Home")

@app.route("/products", methods=["GET", "POST"] )
def products():
    if request.method == "POST":
        empty_csv()
    show_data = display()    #zeigt inhalt von csv
    return render_template("products.html",display=show_data, seitentitel="Produkte")


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
    compare_result = compare_value()
    return render_template("compare.html", compare_result=compare_result)

@app.route('/compare_chart')
def compare_chart():
    compare_result = compare_value()
    labels = ['Energy', 'Fat', 'Fat acids', 'Carbs', 'Sugar', 'Protein', 'Salt']
    ist = [compare_result.energy, compare_result.fat, compare_result.fat_acids, compare_result.carbs, compare_result.sugar, compare_result.protein, compare_result.salt]
    soll = [10460, 65, 22, 275, 50, 62, 6]
    data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Ist',
                'data': ist,
                'backgroundColor': 'blue'
            },
            {
                'label': 'Soll',
                'data': soll,
                'backgroundColor': 'green'
            }
        ]
    }
    return render_template("compare_chart.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5550)
