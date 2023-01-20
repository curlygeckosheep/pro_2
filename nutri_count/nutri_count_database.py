from datatype import Display, Eintrag, Compare

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

#Erstellt Eintrag in CSV
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
            display.eintraege.append(eintrag) #Fügt neuen Eintrag hinzu

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
    ist = display() #holt die Summe der Werte
    soll = (10460, 65, 22, 275, 50, 62, 6) #kJ und der Rest Gramm, 19-25 Jahre alter Mann
    percentage = 10
    energy_percent = soll[0] /100 * percentage #Berechnet % für Toleranzspanne
    fat_percent = soll[1] / 100 * percentage
    fat_acids_percent = soll[2] / 100 * percentage
    carbs_percent = soll[3] / 100 * percentage
    sugar_percent = soll[4] / 100 * percentage
    protein_percent = soll[5] / 100 * percentage
    salt_percent = soll[6] / 100 * percentage
    energy = abs(ist.total_energy - soll[0])    #Definiert Wert als abs olut
    fat = abs(ist.total_fat - soll[1])
    fat_acids = abs(ist.total_fat_acids - soll[2])
    carbs = abs(ist.total_carbs - soll[3])
    sugar = abs(ist.total_sugar - soll[4])
    protein = abs(ist.total_protein - soll[5])
    salt = abs(ist.total_salt - soll[6])
    compare = Compare(                         #Berechnet Diferenz zwischen Soll und Ist
        energy = ist.total_energy - soll[0],
        fat = ist.total_fat - soll[1],
        fat_acids = ist.total_fat_acids - soll[2],
        carbs = ist.total_carbs - soll[3],
        sugar = ist.total_sugar - soll[4],
        protein = ist.total_protein - soll[5],
        salt = ist.total_salt - soll[6],

        is_energy_good= energy_percent >= energy,
        is_fat_good = fat_percent >= fat,
        is_fat_acids_good = fat_acids_percent >= fat_acids,
        is_carbs_good = carbs_percent >= carbs,
        is_sugar_good = sugar_percent >= sugar,
        is_protein_good = protein_percent >= protein,
        is_salt_good = salt_percent >= salt)
    return compare

