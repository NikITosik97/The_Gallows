import level_games
from rendering import rendering
from random import choice


def process_game():
    word_1 = level_games.level_1_animals[0]
    length_word_1 = len(word_1)
    field = ['_' for i in range(length_word_1)]
    try_ = len(rendering)
    print(f'Угадайте слово из {length_word_1} букв')
    print()
    print(*field)
    print()
    count = 0
    while try_ != 0:
        letter = input("Ваша буква: ")
        for ind, letter_ in enumerate(word_1):
            if letter in word_1:
                word_index = word_1.find(letter)
                field[word_index] = letter
                print(*field)
                print('Буква угадана!')
                break
            else:
                print(rendering[count])
                count += 1
                try_ -= 1
                break
        if "".join(field) == word_1:
            return 'Вы победили!'
    return 'Вы проиграли!'


