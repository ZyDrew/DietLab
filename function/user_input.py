def get_period():
    print("Choisissez la période à encoder :")
    print(
"""
1. Petit déjeuner
2. Collation du matin
3. Diner
4. Collation de l'après-midi
5. Souper
6. Collation du soir 
""")

    while True:
        result_answer = input("Votre choix (1 à 6) : ")
        try:
            result_answer = int(result_answer)
        except ValueError:
            print("Encoder un chiffre de 1 à 6 inclus\n")
            continue

        if result_answer >= 1 and result_answer <= 6:
            return result_answer-1
        else:
            print("Encoder un chiffre de 1 à 6 inclus\n")
            
def get_food_name():
    return input("Quel aliment souhaitez-vous : ")

def select_from_food_list(food_list):
    while True:
        result_answer = input(f"Votre choix (1 à {len(food_list)}) : ")

        try:
            result_answer = int(result_answer)
        except ValueError:
            print(f"Encoder un nombre de 1 à {len(food_list)} inclus\n")
            continue

        if result_answer >= 1 and result_answer <= len(food_list):
            return result_answer-1
        else:
            print(f"Encoder un nombre de 1 à {len(food_list)} inclus\n")

def get_quantity():
    while True:
        food_quantity = input("Encoder la proportion en gramme ou ml : ")

        try:
            food_quantity = float(food_quantity)
        except ValueError:
            print(f"Erreur! {food_quantity} Encoder un nombre valide\n")
            continue

        return food_quantity
            