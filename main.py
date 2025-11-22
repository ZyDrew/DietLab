from function.data_manager import read_food_datafile
from function.user_input import get_menu_choice
from function.display import show_main_menu
from function.session import run_menu_loop
from rich.console import Console

def main():
    #Définition de la console d'affichage global au programme
    console = Console()

    #Initialisation des données
    #Lecture du fichier des données csv
    food_datafile = read_food_datafile()

    while True:
        #Affichage du menu principal
        show_main_menu(console)

        #Boucle principale du programme
        run_menu_loop(get_menu_choice(console, 4), food_datafile, console)
         
main()