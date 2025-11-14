from rich.console import Console
from rich.table import Table

def show_summary_table(food_data):
    console = Console()
    console.clear()

    table = Table(title="Petit déjeuner")

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

    #food_date = Liste de dictionnaires contenant chaque aliment
    #food = Dictionnaire : clé = nom de l'aliment , valeur = sous-dictionnaire avec les caractéristiques
    for food in food_data:
        name, details = next(iter(food.items()))
        if details["period"] == "breakfast":
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
    console.print(table)

def fmt(x):
    if isinstance(x, float):
        return f"{x:.2f}"   
    return str(x)
