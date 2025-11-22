import csv, json, os
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

def save_to_json(food_name, macro_dict, json_file):
    if os.path.exists(json_file):
        food_data = []
        with open(json_file, mode="r", encoding="utf-8") as read_file:
            food_data = json.load(read_file)
        
        food_data.append({"name" : food_name, "details" : macro_dict})
        with open(json_file, mode="w", encoding="utf-8") as write_file:
            json.dump(food_data, write_file)
    else:
        food_data = [{"name" : food_name, "details" : macro_dict}]
        with open(json_file, mode="w", encoding="utf-8") as write_file:
            json.dump(food_data, write_file)

def load_json(json_file):
    if os.path.exists(json_file):
        with open(json_file, mode="r", encoding="utf-8") as f:
            return json.load(f)