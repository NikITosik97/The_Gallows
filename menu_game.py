from rules import rules_game
from process_game import process_game

categories = ("Животные", "Природа", "Музыка")


def menu():
    response = input("""   Меню: 
1. Старт
2. Правила
""")
    if response == 'Правила':
        return(print(rules_game))
    elif response == 'Старт':
        response_categories = input("""
Выбор категории:
Животные
Природа
Музыка
""")
        if response_categories == 'Животные':
            return(print("""
            1 уровень
            """), process_game())