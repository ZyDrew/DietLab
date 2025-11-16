def find_matching_food(food_name, food_datafile):    
    #Recherche parmis chaque aliment, une correspondance avec l'entrée de l'utilisateur.
    #On enregistre dans une liste, tous les aliments correspondants.
    search_list = []
    #Food = le nom de chaque élément , clé primaire du datafile
    for food in food_datafile:
        if food.lower().startswith(food_name.lower()):
            search_list.append(food)
    
    return search_list