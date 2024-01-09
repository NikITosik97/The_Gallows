from rules import rules_game
from select_categories import select_categories


def menu():
    response = input("""  Меню: 
1. Старт
2. Правила
""")
    match response:
        case "1":
            return select_categories()
        case "2":
            print(rules_game)
            menu()
