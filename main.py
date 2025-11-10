from constants import PERIODS
from function.data_manager import read_food_datafile
from function.user_input import get_period, get_food_name, select_from_food_list, get_quantity
from function.search_engine import find_matching_food, display_foods

def main():
    print("DietLab")

    #Lecture du fichier des données csv
    food_datafile = read_food_datafile()

    #L'utilisateur encode la période souhaitée
    period_index = get_period()
    selected_period = PERIODS[period_index]
    
    #L'utilisateur encode l'aliment souhaité
    food_name = get_food_name()
    search_list = find_matching_food(food_name, food_datafile)

    #L'utilisater choisit parmi la liste de correspondance
    display_foods(search_list)
    list_index = select_from_food_list(search_list)
    selected_food = search_list[list_index]

    #L'utilisateur encode la quantité de l'aliment selectionné
    food_quantity = get_quantity()
    
    ##à changer
    macro_result = float(food_quantity) / 100

    print(f"Element : {selected_food} enregistré")
    print(f"Période : {selected_period}")
    print(
f"""
Valeurs macro. 
Calories : {float(food_datafile[selected_food]["calories"])*macro_result}
Protéines : {float(food_datafile[selected_food]["proteines"])*macro_result}
""")
         
main()