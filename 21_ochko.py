import random


def gener_kolod():
    """
    Создает колоду карт.
    :return: return type list
    """
    new_list = []
    finish_list = []
    mast = ('Cherv', 'Bubi', 'Krest', 'Piki')  # C-chervi, B-bubi, K-kresti
    value = ('6 ', '7 ', '8 ', '9 ', '10 ', 'B ', 'D ', 'K ', 'T ')
    new_list = [x + y for x in value for y in mast]
    while new_list:
        finish_list = finish_list + [new_list.pop(random.randint(0, len(new_list) - 1))]
    return finish_list


def sum_of_el(a):
    """
    Считает сумму карт в руке.
    :param a: list
    :return: Return type int
    """
    amount = 0
    for i in a:
        amount += int(i)
    return amount


def kard_in_int(a):
    """
    Перевод  карты в номинальное значение
    :param a: list
    :return: list
    """
    znach = {'B': 2,
        'D': 3,
        'K': 4,
        'T': 11,
        '1': 10,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9}
    new_list = []
    for elem in a:
        if str(elem[0]) in znach.keys():
            new_list = new_list + [znach[elem[0]]]
        else:
            new = new_list + [elem[0]]
    return new_list


name = input('Как вас зовут? Начнем игру!\n')

while True:
    while True:
        komp = []
        igrok = []
        koloda = gener_kolod()
        while len(komp) < 2:
            komp = komp + kard_in_int([koloda.pop()])
        while sum_of_el(komp) < 15:
            komp = komp + kard_in_int([koloda.pop()])
        if sum_of_el(komp) <= 18:
            if random.randint(0, 1):
                komp = komp + kard_in_int([koloda.pop()])
            else:
                break
        break

    while True:
        while len(igrok) < 2:
            igrok = igrok + kard_in_int([koloda.pop()])
        try:
            while True:
                inp = int(input(f'Ваши очки: {igrok} Берем еще? [1-Да , 0-Нет]'))
                if inp == 1:
                    igrok = igrok + kard_in_int([koloda.pop() ])
                    if sum_of_el(igrok) >= 21:
                        print('Раскроем карты!')
                        break
                else:
                    print('Раскроем карты!')
                    inp = 0
                    break
        except ValueError:
            print("Вы должны ввести 0 или 1!")
        if sum_of_el(igrok) < 22 and sum_of_el(komp) < 22:
            if sum_of_el(igrok) > sum_of_el(komp):
                inp = input(f'{name}! ВЫ ПОБЕДИЛИ! Результат: Игрок:{sum_of_el(igrok)} Компьютер:{sum_of_el(komp)} \n'
                            f'Будем играть еще? [1-Да , 0-Нет] ')
                break
            elif sum_of_el(igrok) < sum_of_el(komp):
                inp = input(f'{name}! ВЫ ПРОИГРАЛИ! Результат: Игрок:{sum_of_el(igrok)} Компьютер:{sum_of_el(komp)} \n'
                            f'Будем играть еще? [1-Да , 0-Нет]')
                break
            else:
                inp = input(f'{name}! Ничья! Результат: Игрок:{sum_of_el(igrok)} Компьютер:{sum_of_el(komp)}\n'
                            f'Будем играть еще? [1-Да , 0-Нет]')
                break
        elif sum_of_el(igrok) >= 22 and sum_of_el(komp) >= 22:
            inp = input(f'{name}! Ничья! Результат: Игрок:{sum_of_el(igrok)} Компьютер:{sum_of_el(komp)}\n'
                        f'Будем играть еще? [1-Да , 0-Нет]')
            break
        if sum_of_el(igrok) >= 22 and sum_of_el(komp) < 22:
            inp = input(f'{name}! Вы проиграли! Результат: Игрок:{sum_of_el(igrok)} Компьютер:{sum_of_el(komp)}  \n'
                        f'Будем играть еще? [1-Да , 0-Нет]')
            break
        elif sum_of_el(igrok) < 22 and sum_of_el(komp) >= 22:
            inp = input(f'{name}! Вы выирали! Результат: Игрок:{sum_of_el(igrok)} Компьютер:{sum_of_el(komp)}  \n'
                        f'Будем играть еще? [1-Да , 0-Нет]')
            break
    if int(inp) == 1:
        print('Поехали!')
    else:
        print("Досвидания!")
        break

