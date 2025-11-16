from rich.table import Table
from rich.markdown import Markdown
from rich import print

def show_menu(console):
    console.clear()

    menu_md = """
# DietLab

Choisissez une action parmi les suivantes.

1. Encoder un nouvel aliment
2. Afficher le tableau récapitulatif
3. Quitter
"""
    md = Markdown(menu_md)
    console.print(md)

def display_foods(matching_food_name):
    print("\nChoisissez parmis les élements suivants..")
    for i in range(len(matching_food_name)):
        print(f"[bold yellow]{i+1}.[/bold yellow] {matching_food_name[i]}")

def food_error():
    print("[red]\nAucun aliment correspondant, réessayez.[/red]")

def show_summary_table(food_data, console):
    console.clear()

    #Liste des tableaux
    table_list = []

    #Appel de la création des tableaux pour chaque période
    table_list.append(generate_table("breakfast", "Petit déjeuner", food_data))
    table_list.append(generate_table("morning-snack", "Collation du matin", food_data))
    table_list.append(generate_table("lunch", "Diner", food_data))
    table_list.append(generate_table("snack", "Goûter", food_data))
    table_list.append(generate_table("diner", "Souper", food_data))
    table_list.append(generate_table("night-snack", "Collation du soir", food_data))

    for table in table_list:
        console.print(table)

def generate_table(period, period_name, food_data):

    table = Table(title=period_name)

    #Ajout des colonnes de la table
    table.add_column("Nom", justify="center")
    table.add_column("Quantité (g ou ml)")
    table.add_column("Calories (kcal)")
    table.add_column("Protéines (g)")
    table.add_column("Glucides (g)")
    table.add_column("Lipides (g)")
    table.add_column("Calcium (mg)")
    table.add_column("Fer (mg)")
    table.add_column("Vitamin-C (mg)")

    #food_data = Liste de dictionnaires contenant chaque aliment
    #food = Dictionnaire : clé = nom de l'aliment , valeur = sous-dictionnaire avec les caractéristiques
    for food in food_data:
        name, details = next(iter(food.items()))
        if details["period"] == period:
            table.add_row(
                fmt(name),
                fmt(details["quantity"]),
                fmt(details["calories"]),
                fmt(details["proteins"]),
                fmt(details["carbs"]),
                fmt(details["fat"]),
                fmt(details["calcium"]),
                fmt(details["iron"]),
                fmt(details["vitamin_c"])
            )

    return table

def fmt(x):
    if isinstance(x, float):
        return f"{x:.2f}"   
    return str(x)