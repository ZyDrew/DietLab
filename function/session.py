from constants import PERIODS
from function.calculator import calculate_macro
from function.data_manager import load_json, save_to_json
from function.display import food_error, show_summary_table, display_foods, recap_error
from function.search_engine import find_matching_food
from function.user_input import enter_to_exit, get_period, get_food_name, select_from_food_list, get_quantity, get_continue_or_change_period

def run_program_loop(user_menu, food_datafile, console):
    match user_menu:
        case 1:
            #L'utilisateur encode la période souhaitée
            period_index = get_period(console)

            loop = True
            while loop:
                add_food_item(food_datafile, PERIODS[period_index], console)
                loop = get_continue_or_change_period(console)
        case 2:
            datas = load_json()
            if datas:
                show_summary_table(datas, console)
            else: 
                recap_error(console)
            enter_to_exit()
        case 3:
            exit()
        case _:
            pass

def add_food_item(food_datafile, period, console):

    #L'utilisateur encode l'aliment souhaité
    search_list = food_name_process(food_datafile, console)

    #L'utilisater choisit parmi la liste de correspondance
    display_foods(search_list)
    list_index = select_from_food_list(search_list, console)
    selected_food = search_list[list_index]

    #L'utilisateur encode la quantité de l'aliment sélectionné
    food_quantity = get_quantity(console)
    
    #Calcul du résultat des macro-nutriment pour l'aliment sélectionné
    macro_value_dict = calculate_macro(food_datafile[selected_food], food_quantity, period)
    
    #Enregistrement du record
    save_to_json(selected_food, macro_value_dict)

def food_name_process(food_datafile, console):
    loop = True
    while loop:
        food_name = get_food_name(console)
        search_list = find_matching_food(food_name, food_datafile)

        if not search_list:
            food_error()
        else:
            loop = False
    
    return search_list