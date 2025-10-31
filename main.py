import csv

def main():
    print("DietLab")

    fieldnames = ["nom", "categorie", "calories", "proteines", "lipides", "glucides", "calcium", "fer", "vitamine-C"]
    #Lecture du fichier des données csv
    with open("./data/food.csv") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)

        food_datafile = {}
        #Pour chaque ligne du fichier csv, on crée une paire clé/valeur dans notre dictionnaire
        #La clé primaire sera le nom de l'aliment, suivi d'un sous dictionnaire de clé/valeur représentant les caractéristiques de l'aliment
        for row in reader:
            food_datafile[row[reader.fieldnames[0]]] = {k: v for k, v in row.items() if k != reader.fieldnames[0]}

    answer = input("Quel aliment souhaitez-vous : ") 
    if answer in food_datafile:
        print(food_datafile[answer])
    else:
        print("Aliment incorrect")       
main()