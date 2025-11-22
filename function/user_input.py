from rich.markdown import Markdown
from rich import print

def get_menu_choice(console, sub):
    #Menu principal je passe 4 à sub, sinon je passe 3 pour les menu secondaires

    while True:
        result_answer = console.input(f"Votre choix (1 à {sub}) : ")
        try:
            result_answer = int(result_answer)
        except ValueError:
            print(f"[red]Encoder un chiffre de 1 à {sub} inclus\n[/red]")
            continue

        if result_answer >= 1 and result_answer <= sub:
            return result_answer
        else:
            print(f"[red]Encoder un chiffre de 1 à {sub} inclus\n[/red]")

def get_period(console):
    console.clear()
    period_md = """
### Choisissez la période à encoder.

1. Petit déjeuner
2. Collation du matin
3. Diner
4. Collation de l'après-midi
5. Souper
6. Collation du soir 
"""

    md = Markdown(period_md)
    console.print(md)

    while True:
        result_answer = console.input("Votre choix (1 à 6) : ")
        try:
            result_answer = int(result_answer)
        except ValueError:
            print("[red]Encoder un chiffre de 1 à 6 inclus\n[/red]")
            continue

        if result_answer >= 1 and result_answer <= 6:
            return result_answer-1
        else:
            print("[red]Encoder un chiffre de 1 à 6 inclus\n[/red]")
            
def get_food_name(console):
    return console.input("\nQuel aliment souhaitez-vous : ")

def select_from_food_list(food_list, console):
    while True:
        result_answer = console.input(f"\nVotre choix (1 à {len(food_list)}) : ")

        try:
            result_answer = int(result_answer)
        except ValueError:
            print(f"[red]Encoder un nombre de 1 à {len(food_list)} inclus\n[/red]")
            continue

        if result_answer >= 1 and result_answer <= len(food_list):
            return result_answer-1
        else:
            print(f"[red]Encoder un nombre de 1 à {len(food_list)} inclus\n[/red]")

def get_quantity(console):
    while True:
        food_quantity = console.input("\nEncoder la proportion en gramme ou ml : ")

        try:
            food_quantity = float(food_quantity)
        except ValueError:
            print(f"[red]Erreur! {food_quantity} Encoder un nombre valide\n[/red]")
            continue

        return food_quantity
        
def get_frequency(console):
    while True:
        frequency = console.input("\nEncoder la fréquence de consommation en jour (pour une semaine) : ")

        try:
            frequency = int(frequency)
        except ValueError:
            print("[red]Encoder un chiffre de 1 à 7 inclus\n[/red]")
            continue
        
        if frequency >= 1 and frequency <= 7:
            return frequency
        else:
            print("[red]Encoder un chiffre de 1 à 7 inclus\n[/red]")

def get_continue_or_change_period(console):
    while True:
        result_answer = console.input("\nVoulez-vous encoder un nouvel aliment pour cette période (O/N) : ")

        if result_answer not in ("O", "o", "N", "n"):
            print("[red]Encoder la lettre correspondante O: oui ou N: non \n[/red]")
            continue

        if result_answer in ("O", "o"):
            return True
        else:
            return False
            
def enter_to_exit():
    input("\n\nAppuyer sur entrée pour quitter le récapitulatif...")