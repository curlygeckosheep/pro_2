# Importiert flask stuff
from flask import Flask
from flask import render_template
from flask import request
# importiert functions from nutri_count_database
from nutri_count_database import new_entry, display, compare_value, empty_csv
# Erstelle flask app
app = Flask("nutri_count")

# Route für homepage
@app.route("/")  # startseite
def start():
    # Zeigt Inhalt von csv, bzw. das Ergebnis von Summe
    display_data = display()
    # rendert template und inhalt von display() funktion
    return render_template("index.html", display=display_data, seitentitel="Home")

# Route für Produktliste, GET für darstellen, POST für löschen
@app.route("/products", methods=["GET", "POST"])
def products():
    # Wenn delete button gedrückt wird, wird data.csv geleert
    if request.method == "POST":
        #Ruft löschfuntkion auf.
        empty_csv()
    # Zeigt Inhalt von csv, bzw. die einzelnen Einträge
    show_data = display()
    # Rendert template und Inhalt von display() Funktion
    return render_template("products.html", display=show_data, seitentitel="Produkte")

# Route für hinzufügen von neuem Orodukt, GET für darstellen, POST für löschen.
@app.route("/new", methods=["GET", "POST"])
def new():
    title = "Neues Produkt"
    if request.method == "GET":
        return render_template("nutri_form.html", seitentitel=title)

    if request.method == "POST":
        # Werte holen aus Formular
        product_name = request.form["product_name"]
        amount = request.form["amount"]
        energy = request.form["energy"]
        fat = request.form["fat"]
        fat_acids = request.form["fat_acids"]
        carbs = request.form["carbs"]
        sugar = request.form["sugar"]
        protein = request.form["protein"]
        salt = request.form["salt"]
        # Schreibt neuen Eintrag ins CSV, mit Einträgen aus Formular
        new_entry(product_name, amount, energy, fat, fat_acids, carbs, sugar, protein, salt)
        # Rendert template und added Bestätigung.
        return render_template("nutri_form.html", seitentitel=title, entry_added=True)

# Route für Vergleich von Werten
@app.route("/compare")
def compare():
    # Holt Werte für Vergleich
    compare_result = compare_value()
    # Rendert template und Ergebnids von vergleich aus
    return render_template("compare.html", compare_result=compare_result)

# Route für barcharts
@app.route('/compare_chart')
def compare_chart():
    # Holt Werte für Vergleich
    compare_result = compare_value()
    # Namen für Labels
    labels = ['Energy', 'Fat', 'Fat acids', 'Carbs', 'Sugar', 'Protein', 'Salt']
    # Holt gesamt Energiewert
    energy_ist = [compare_result.energy]
    # Soll Energiewert
    energy_soll = [10460]
    # Holt gesamt Werte des Restes
    nutri_ist = [compare_result.fat.__round__(2), compare_result.fat_acids.__round__(2),
                 compare_result.carbs.__round__(2), compare_result.sugar.__round__(2),
                 compare_result.protein.__round__(2), compare_result.salt.__round__(2)]
    # Sollwerte für Rest
    nutri_soll = [65, 22, 275, 50, 62, 6]
    # Direkter Python code für die barcharts
    # Sämtliche Werte werden in den Zeilen oberhalb geliefert.
    energyData = {
        'labels': ['Energy'],
        'datasets': [
            {
                'label': 'Ist', 'data': energy_ist,
                'backgroundColor': 'red'
            },
            {
                'label': 'Soll',
                'data': energy_soll,
                'backgroundColor': 'green'
            }
        ]
    }

    nutriData = {
        'labels': labels[1:],
        'datasets': [
            {
                'label': 'Ist',
                'data': nutri_ist,
                'backgroundColor': 'red'
            },
            {
                'label': 'Soll',
                'data': nutri_soll,
                'backgroundColor': 'green'
            }
        ]
    }
    return render_template("compare_chart.html", energyData=energyData, nutriData=nutriData)


if __name__ == "__main__":
    app.run(debug=True, port=5550)
