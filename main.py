import csv

def main():
    print("DietLab")

    fieldnames = ["groupe", "sous-groupe", "nom", "calories", "proteines", "glucides", "lipides", "calcium", "fer", "vitamine-c"]
    #Lecture du fichier des données csv
    with open("./data/Table-Alimentaire-DietLab.csv") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=";")

        food_datafile = {}
        #Pour chaque ligne du fichier csv, on crée une paire clé/valeur dans notre dictionnaire
        #La clé primaire sera le nom de l'aliment, suivi d'un sous dictionnaire de clé/valeur représentant les caractéristiques de l'aliment
        for row in reader:
            food_datafile[row[reader.fieldnames[2]]] = {k: v for k, v in row.items() if k != reader.fieldnames[2]}

    search_answer = input("Quel aliment souhaitez-vous : ") 
    """if answer in food_datafile:
        print(food_datafile[answer])
    else:
        print("Aliment incorrect")"""

    search_list = []
    #Food = le nom de chaque élément , clé primaire du datafile
    for food in food_datafile:
        if food.lower().startswith(search_answer.lower()):
            search_list.append(food)

    print("Choississez parmis les élements suivants..")
    for i in range(len(search_list)):
        print(f"{i+1}. {search_list[i]}")
    result_answer = input("Votre choix : ")

    print(search_list[int(result_answer)-1])
         
main()