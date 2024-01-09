from process_game import process_game
from level_games import level_animals, level_nature, level_music


def select_categories():
    response_categories = input("""Выбор категории: 
1. Животные
2. Природа
3. Музыка
""")
    match response_categories:
        case "1":
            return process_game(level_animals)
        case "2":
            return process_game(level_nature)
        case "3":
            return process_game(level_music)
