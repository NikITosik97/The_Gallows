from rendering import rendering


def find_index_letter(letter: str, word: str):
    lst_index = []

    for indx, letter_ in enumerate(word):
        if letter_ == letter:
            lst_index.append(indx)

    return lst_index


def set_letter(indx: list, pole: list, letter: str):
    for indx_ in indx:
        pole[indx_] = letter

    return pole


def process_game(categories: tuple):
    try_ = 0
    indx_level = 0

    for level in categories:
        indx_level += 1
        if indx_level > 1:
            print(f"Поздравляем вы перешли на {indx_level} уровень!")
        count_word = 0
        print(f'Уровень {indx_level}')
        print("-" * 10)
        for word in level:
            count_word += 1
            field = ["_" for pole in range(len(word))]
            print(f"Слово {count_word} из {len(word)} букв!")
            print(*field)
            while try_ < len(rendering):
                response = input("Ваша буква: ").lower()
                if response in word and response not in field:
                    lst_indx = find_index_letter(response, word)
                    print("Буква угадана!")
                    field = set_letter(lst_indx, field, response)
                    print("-" * 10)
                    print(*field)
                    print("-" * 10)
                else:
                    print(rendering[try_])
                    try_ += 1
                    print(f"У вас осталось {len(rendering) - try_} попытка!")
                if "".join(field) == word:
                    print("Слово угадано!")
                    break
            if try_ == 7:
                return 'Вы проиграли!'
    return "Вы прошли игру!"
