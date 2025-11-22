def calculate_macro(selected_food, quantity, period, frequency):
    quant_multiplier = float(quantity) / 100
    freq_multiplier = float(frequency) / 7

    macro_dict = {}
    macro_dict["quantity"] = quantity
    macro_dict["period"] = period
    macro_dict["frequency"] = frequency
    macro_dict["calories"] = float(selected_food["calories"]) * quant_multiplier * freq_multiplier
    macro_dict["proteins"] = float(selected_food["proteines"]) * quant_multiplier * freq_multiplier
    macro_dict["carbs"] = float(selected_food["glucides"]) * quant_multiplier * freq_multiplier
    macro_dict["fat"] = float(selected_food["lipides"]) * quant_multiplier * freq_multiplier
    macro_dict["calcium"] = float(selected_food["calcium"]) * quant_multiplier * freq_multiplier
    macro_dict["iron"] = float(selected_food["fer"]) * quant_multiplier * freq_multiplier
    macro_dict["vitamin_c"] = float(selected_food["vitamine-c"]) * quant_multiplier * freq_multiplier

    return macro_dict

def sum_macros(food_data, period=None):
    macros = {
        "calories": 0,
        "proteins": 0,
        "carbs": 0,
        "fat": 0,
        "calcium": 0,
        "iron": 0,
        "vitamin_c": 0,
    }

    for food in food_data:
        details = food["details"]
        
        #Permet de filtrer sur les éléments de la période donnée , seulement si on a précisé une période en paramètre
        #period = None , on calcule tout
        #period != None , on calcule seulement si food[period] = period donnée
        if period and details["period"] != period:
            continue
        
        for key in macros:
            macros[key] += details[key]

    
    return tuple(macros.values())