from rich.table import Table
from rich.markdown import Markdown
from rich import print
from function.calculator import sum_macros
from constants import PERIODS

def show_main_menu(console):
    console.clear()

    menu_md = """
# DietLab

Choisissez une action parmi les suivantes.

1. Anamnèse journalière
2. Anamnèse hebdomadaire
3. Calcul besoin énergétique
4. Quitter
"""
    md = Markdown(menu_md)
    console.print(md)

def show_sub_menu(console, week):
    console.clear()

    if week:
        text = "hebdomadaire"
    else:
        text = "journalière"

    menu_md = f"""
Anamnèse {text}.\n
Choisissez une action parmi les suivantes.

1. Encoder un nouvel aliment
2. Afficher le tableau récapitulatif
3. Menu principal
"""

    md = Markdown(menu_md)
    console.print(md)

def display_foods(matching_food_name):
    print("\nChoisissez parmis les élements suivants..")
    for i in range(len(matching_food_name)):
        print(f"[bold yellow]{i+1}.[/bold yellow] {matching_food_name[i]}")

def food_error():
    print("[red]\nAucun aliment correspondant, réessayez.[/red]")

def recap_error(console):
    console.clear()
    print("[red]\nAucun aliment encodé, les tableaux ne peuvent pas être générés.[/red]")

def show_summary_table(food_data, console, week):
    console.clear()

    #Liste des tableaux
    table_list = []
    tables = {
        PERIODS[0] : "Petit déjeuner",
        PERIODS[1] : "Collation du matin",
        PERIODS[2] : "Diner",
        PERIODS[3] : "Goûter",
        PERIODS[4] : "Souper",
        PERIODS[5] : "Collation du soir"
    }

    #Appel de la création des tableaux pour chaque période
    for period, name in tables.items():
        table_list.append(generate_table(period, name, food_data, week))

    #Calcul du total pour la journée complète
    table_list.append(generate_total_table(food_data, week))

    for table in table_list:
        console.print(table)

def generate_table(period, period_name, food_data, week):
    table = base_table(period_name, week)

    #food_data = Liste de dictionnaires contenant chaque aliment
    #food = Dictionnaire : clé1 = nom de l'aliment , clé2 = sous-dictionnaire avec les caractéristiques
    for food in food_data:
        name = food["name"]
        details = food["details"]

        if details["period"] == period:
            rows = [
                fmt(name),
                fmt(details["quantity"]),
                fmt(details["calories"]),
                fmt(details["proteins"]),
                fmt(details["carbs"]),
                fmt(details["fat"]),
                fmt(details["calcium"]),
                fmt(details["iron"]),
                fmt(details["vitamin_c"])
            ]

            if week:
                rows.insert(1, fmt(details["frequency"]))
    
            table.add_row(*rows)

    #Calcul du total pour une période d'une journée
    calories, proteins, carbs, fat, calcium, iron, vitamin_c = sum_macros(food_data, period)
    rows = [
        "Total", 
        "", 
        fmt(calories), 
        fmt(proteins),
        fmt(carbs),
        fmt(fat), 
        fmt(calcium), 
        fmt(iron),
        fmt(vitamin_c)
    ]

    if week:
        rows.insert(1, "")

    table.add_section()
    table.add_row(*rows)

    return table

def generate_total_table(food_data, week):
    table = base_table("Total pour la journée", week)
    
    calories, proteins, carbs, fat, calcium, iron, vitamin_c = sum_macros(food_data)
    rows = [
        "Total", 
        "", 
        fmt(calories), 
        fmt(proteins),
        fmt(carbs),
        fmt(fat), 
        fmt(calcium), 
        fmt(iron),
        fmt(vitamin_c)
    ]

    if week:
        rows.insert(1, "")

    table.add_row(*rows)
    
    return table

def base_table(title, week):
    #Création de la structure de base pour toutes les tables
    table = Table(title=title)
    
    #Ajout des colonnes de la table
    table.add_column("Nom", justify="center")
    if week:
        table.add_column("Fréquence (jours/sem)")
    table.add_column("Quantité (g ou ml)")
    table.add_column("Calories (kcal)")
    table.add_column("Protéines (g)")
    table.add_column("Glucides (g)")
    table.add_column("Lipides (g)")
    table.add_column("Calcium (mg)")
    table.add_column("Fer (mg)")
    table.add_column("Vitamin-C (mg)")

    return table

def fmt(x):
    if isinstance(x, float):
        return f"{x:.2f}"   
    return str(x)