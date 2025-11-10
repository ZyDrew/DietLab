from function.user_input import get_food_name

def find_matching_food(food_name, food_datafile):    
    loop = True
    while loop:
        #Recherche parmis chaque aliment, une correspondance avec l'entrée de l'utilisateur.
        #On enregistre dans une liste, tous les aliments correspondants.
        search_list = []
        #Food = le nom de chaque élément , clé primaire du datafile
        for food in food_datafile:
            if food.lower().startswith(food_name.lower()):
                search_list.append(food)
        
        if not search_list:
            print("Aucun aliment correspondant, réessayez.\n")
            food_name = get_food_name()
        else:
            loop = False
    
    return search_list

def display_foods(matching_food_name):
    print("Choisissez parmis les élements suivants..")
    for i in range(len(matching_food_name)):
        print(f"{i+1}. {matching_food_name[i]}")