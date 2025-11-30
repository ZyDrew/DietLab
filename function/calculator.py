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


def calculate_bej(gender, age, height, weight, nap):
    match(gender):
        case 1:
            if age >= 0 and age < 3:
                return ((28.2 * weight) + (859 * height) - 371) * nap
            elif age >= 3 and age < 10:
                return ((15.1 * weight) + (74.2 * height) + 306) * nap
            elif age >= 10 and age < 18:
                return ((15.6 * weight) + (266 * height) + 299) * nap
            elif age >= 18 and age < 30:
                return ((14.4 * weight) + (313 * height) + 113) * nap
            elif age >= 30 and age < 60:
                return ((11.4 * weight) + (541 * height) - 137) * nap
            elif age >= 60:
                return ((11.4 * weight) + (541 * height) - 256) * nap  

        case 2:
            if age >= 0 and age < 3:
                return ((30.4 * weight) + (703 * height) - 287) * nap
            elif age >= 3 and age < 10:
                return ((15.9 * weight) + (210 * height) + 349) * nap
            elif age >= 10 and age < 18:
                return ((9.4 * weight) + (249 * height) + 462) * nap
            elif age >= 18 and age < 30:
                return ((10.4 * weight) + (615 * height) - 282) * nap
            elif age >= 30 and age < 60:
                return ((8.18 * weight) + (502 * height) - 11.6) * nap
            elif age >= 60:
                return ((8.52 * weight) + (421 * height) + 10.7) * nap 

        case _:
            pass
    