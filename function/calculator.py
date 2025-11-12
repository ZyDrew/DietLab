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

