import csv, json, os, sys
from constants import FIELDNAMES, DATA_FILE

def read_food_datafile():
    filename = get_data_path(DATA_FILE)

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=FIELDNAMES, delimiter=";")

        food_datafile = {}
        #Pour chaque ligne du fichier csv, on crée une paire clé/valeur dans notre dictionnaire
        #La clé primaire sera le nom de l'aliment, suivi d'un sous dictionnaire de clé/valeur représentant les caractéristiques de l'aliment
        for row in reader:
            food_datafile[row[reader.fieldnames[2]]] = {k: v for k, v in row.items() if k != reader.fieldnames[2]}
    
    return food_datafile

def save_to_json(food_name, macro_dict, json_file):
    filename = get_output_path(json_file)

    if os.path.exists(filename):
        food_data = []
        with open(filename, mode="r", encoding="utf-8") as read_file:
            food_data = json.load(read_file)
        
        food_data.append({"name" : food_name, "details" : macro_dict})
        with open(filename, mode="w", encoding="utf-8") as write_file:
            json.dump(food_data, write_file)
    else:
        food_data = [{"name" : food_name, "details" : macro_dict}]
        with open(filename, mode="w", encoding="utf-8") as write_file:
            json.dump(food_data, write_file)

def load_json(json_file):
    filename = get_output_path(json_file)

    if os.path.exists(filename):
        with open(filename, mode="r", encoding="utf-8") as f:
            return json.load(f)
        
def get_data_path(filename):
    #Pour exécutable Windows
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    
    #Pour dev Linux
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, "..", "data", filename)

def get_output_path(filename):
    if hasattr(sys, "_MEIPASS"):
        base_path = os.path.dirname(sys.executable)  # dossier du .exe
    else:
        base_path = os.path.dirname(os.path.dirname(__file__))

    output_dir = os.path.join(base_path, "data")
    os.makedirs(output_dir, exist_ok=True)

    return os.path.join(output_dir, filename)

    