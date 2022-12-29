from display import Display
from eintrag import Eintrag

#Auslesen
def read():
    with open("database.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt

#Neuen eintrag machen
def new_entry(product_name, amount, energy, fat, fat_acids, carbs, sugar, protein, salt):
    current_content = read()
    new_content = current_content + f"{product_name},{amount},{energy},{fat},{fat_acids},{carbs},{sugar},{protein},{salt}\n"
    with open("database.csv", "w") as open_file:
        open_file.write(new_content)

#Darstellung auf index Seite
def display():
    lines = read()
    display = Display([])
    for line in lines.split("\n"):
        entry = line.split(",")
        # leeres csv war = 1
        if len(entry) > 1:
            eintrag = Eintrag(
                entry[0],
                float(entry[1]),
                float(entry[2]),
                float(entry[3]),
                float(entry[4]),
                float(entry[5]),
                float(entry[6]),
                float(entry[7]),
                float(entry[8])
            )
            display.eintraege.append(eintrag) #Fügrt neuen Eintrag hinzu
    # Berechnung der Gesamtmenge
    for eintrag in display.eintraege:
        display.total_energy += calculate_value(eintrag.amount, eintrag.energy)
        display.total_fat += calculate_value(eintrag.amount, eintrag.fat)
        display.total_fat_acids += calculate_value(eintrag.amount, eintrag.fat_acids)
        display.total_carbs += calculate_value(eintrag.amount, eintrag.carbs)
        display.total_sugar += calculate_value(eintrag.amount, eintrag.sugar)
        display.total_protein += calculate_value(eintrag.amount, eintrag.protein)
        display.total_salt += calculate_value(eintrag.amount, eintrag.salt)

    return display

#Funktion für Berechnung der Gesamtmenge
def calculate_value(amount, value):
    return (value / 100) * amount #echte Menge berechnen, aus 100g/ml


def compare_value():
    ist = (energy, fat, fat_acids, carbs, sugar, protein, salt)
    soll = (15, 10, 5, 4, 3, 2, 1)
    if ist > soll:
        return "zu viel"
    else ist = soll:
        return "perfekt"
    elif:
        return "zu wenig"
