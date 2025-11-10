import csv
from constants import FIELDNAMES, DATA_FILE

def read_food_datafile():
    with open(DATA_FILE) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=FIELDNAMES, delimiter=";")

        food_datafile = {}
        #Pour chaque ligne du fichier csv, on crée une paire clé/valeur dans notre dictionnaire
        #La clé primaire sera le nom de l'aliment, suivi d'un sous dictionnaire de clé/valeur représentant les caractéristiques de l'aliment
        for row in reader:
            food_datafile[row[reader.fieldnames[2]]] = {k: v for k, v in row.items() if k != reader.fieldnames[2]}
    
    return food_datafile