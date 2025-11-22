from constants import PERIODS, JSON_FILE_WEEK, JSON_FILE_DAY
from function.calculator import calculate_macro
from function.data_manager import load_json, save_to_json
from function.display import food_error, show_summary_table, display_foods, recap_error, show_sub_menu
from function.search_engine import find_matching_food
from function.user_input import get_menu_choice, enter_to_exit, get_period, get_food_name, select_from_food_list, get_quantity, get_continue_or_change_period, get_frequency

def run_menu_loop(user_menu, food_datafile, console):
    match user_menu:
        #Anamnèse journalière
        case 1:
            loop = True
            while loop:
                show_sub_menu(console, False)
                loop = run_process(get_menu_choice(console, 3), food_datafile, console, False)
        
        #Anamnèse hebdomadaire
        case 2:
            loop = True
            while loop:
                show_sub_menu(console, True)
                loop = run_process(get_menu_choice(console, 3), food_datafile, console, True)

        #Calcul du besoin énergétique d'une personne
        case 3:
            pass

        case 4:
            exit()
        
        case _:
            pass

def run_process(user_menu, food_datafile, console, week):
    #Initialisation des variables pour gestion jour/semaine
    json_file = JSON_FILE_WEEK if week else JSON_FILE_DAY

    match user_menu:
        #Encodage d'un aliment
        case 1:
            #L'utilisateur encode la période souhaitée
            period_index = get_period(console)

            loop = True
            while loop:
                add_food_item(food_datafile, PERIODS[period_index], console, json_file, week)
                loop = get_continue_or_change_period(console)
            
            return True
        
        #Affichage du tableau récapitulatif
        case 2:
            datas = load_json(json_file)
            if datas:
                show_summary_table(datas, console, week)
            else: 
                recap_error(console)
            
            enter_to_exit()
            return True

        #Quitter vers le menu principal
        case 3:
            return False

def add_food_item(food_datafile, period, console, json_file, week):

    #L'utilisateur encode l'aliment souhaité
    search_list = food_name_process(food_datafile, console)

    #L'utilisater choisit parmi la liste de correspondance
    display_foods(search_list)
    list_index = select_from_food_list(search_list, console)
    selected_food = search_list[list_index]

    #L'utilisateur encode la quantité de l'aliment sélectionné
    food_quantity = get_quantity(console)

    #L'utilisateur encode la fréquence de consommation sur une semaine (si week = True)
    if week:
        frequency = get_frequency(console)
    else:
        frequency = 7
    
    #Calcul du résultat des macro-nutriment pour l'aliment sélectionné
    macro_value_dict = calculate_macro(food_datafile[selected_food], food_quantity, period, frequency)
    
    #Enregistrement du record
    save_to_json(selected_food, macro_value_dict, json_file)

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