from display import Display, Eintrag, Compare

def empty_csv():
    with open("database.csv", "w") as open_file:
        open_file.write("")
    return

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
    return

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

#vergleicht die Eingaben der Produkte mit den empfohlenen Werten aus dem Internet
def compare_value():
    ist = display()
    soll = (1500, 10, 5, 4, 3, 2, 1)
    percentage = 5
    energy_percent = soll[0] /100 * percentage
    energy = abs(ist.total_energy - soll[0])
    compare = Compare(
        energy = ist.total_energy - soll[0],
        fat = ist.total_fat - soll[1],
        fat_acids = ist.total_fat_acids - soll[2],
        carbs = ist.total_carbs - soll[3],
        sugar = ist.total_sugar - soll[4],
        protein = ist.total_protein - soll[5],
        salt = ist.total_salt - soll[6],
        is_energy_good= energy_percent >= energy)
    return compare

