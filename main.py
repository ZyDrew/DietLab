from constants import PERIODS
from function.data_manager import read_food_datafile, save_to_json, load_json
from function.user_input import get_period, get_food_name, select_from_food_list, get_quantity
from function.search_engine import find_matching_food, display_foods
from function.calculator import calculate_macro
from function.display import show_summary_table

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

    #L'utilisateur encode la quantité de l'aliment sélectionné
    food_quantity = get_quantity()
    
    #Calcul du résultat des macro-nutriment pour l'aliment sélectionné
    macro_value_dict = calculate_macro(food_datafile[selected_food], food_quantity, selected_period)
    
    #Enregistrement du record
    save_to_json(selected_food, macro_value_dict)

    #Affichage du tableau récapitulatif
    show_summary_table(load_json())


         
main()