def calculate_macro(selected_food, quantity, period):
    multiplier = float(quantity) / 100

    macro_dict = {}
    macro_dict["quantity"] = quantity
    macro_dict["period"] = period
    macro_dict["calories"] = float(selected_food["calories"]) * multiplier
    macro_dict["proteins"] = float(selected_food["proteines"]) * multiplier
    macro_dict["carbs"] = float(selected_food["glucides"]) * multiplier
    macro_dict["fat"] = float(selected_food["lipides"]) * multiplier
    macro_dict["calcium"] = float(selected_food["calcium"]) * multiplier
    macro_dict["iron"] = float(selected_food["fer"]) * multiplier
    macro_dict["vitamin_c"] = float(selected_food["vitamine-c"]) * multiplier

    return macro_dict

def sum_macros(food_data, period=None):
    calories = proteins = carbs = fat = calcium = iron = vitamin_c = 0

    for food in food_data:
        _, details = next(iter(food.items()))
        
        #Permet de filtrer sur les éléments de la période donnée , seulement si on a précisé une période en paramètre
        #period = None , on calcule tout
        #period != None , on calcule seulement si food[period] = period donnée
        if period and details["period"] != period:
            continue
        
        calories += details["calories"]
        proteins += details["proteins"]
        carbs += details["carbs"]
        fat += details["fat"]
        calcium += details["calcium"]
        iron += details["iron"]
        vitamin_c += details["vitamin_c"]

    
    return calories, proteins, carbs, fat, calcium, iron, vitamin_c