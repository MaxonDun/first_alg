import random

def gener_kolod():
    mast=('Cherv','Bubi','Krest','Piki') # C-chervi, B-bubi, K-kresti
    value=('6 ','7 ','8 ','9 ','10 ','B ','D ','K ','T ')
    return  [x+y for x in value for y in mast]

def sum(a):
    summa=0
    for i in a:
        summa+=int(i)
    return summa


def kard_in_int(a):
    znach={'B':2,'D':3,'K':4,'T':11,'1':10,'6':6,'7':7,'8':8,'9':9}
    new=[]
    for i in a:
        if str(i[0]) in znach.keys():
            new = new + [znach[i[0]]]
        else:
            new = new + [i[0]]
    return new

name = input('Как вас зовут? Начнем игру!')

while True:
    while True:
        komp = []
        igrok = []
        koloda = gener_kolod()
        while len(komp) < 2:
            komp = komp + kard_in_int([koloda.pop(random.randint(1, len(koloda) - 1))])
        while sum(komp) < 15:
            komp = komp + kard_in_int([koloda.pop(random.randint(1, len(koloda) - 1))])
        if sum(komp) <= 18:
            if random.randint(0, 1):
                komp = komp + kard_in_int([koloda.pop(random.randint(1, len(koloda) - 1))])
            else:
                break
        break


    while True:
        while len(igrok) < 2:
            igrok = igrok + kard_in_int([koloda.pop(random.randint(1,len(koloda) - 1))])
        try:
            while True:
                inp = int(input(f'Ваши очки: {igrok} Берем еще? [1-Да , 0-Нет]'))
                if inp==1:
                    igrok = igrok + kard_in_int([koloda.pop(random.randint(1, len(koloda) - 1))])
                else:
                    print('Раскроем карты!')
                    inp=0
                    break
        except ValueError:
            print("Вы должны ввести 0 или 1!")
        if sum(igrok)<22 and sum(komp)<22:
            if sum(igrok) > sum(komp):
                inp = input(f'{name}! ВЫ ПОБЕДИЛИ! Результат: Игрок:{sum(igrok)} Компьютер:{sum(komp)} \n'
                        f'Будем играть еще? [1-Да , 0-Нет] ')
                break
            elif sum(igrok) < sum(komp):
                inp = input(f'{name}! ВЫ ПРОИГРАЛИ! Результат: Игрок:{sum(igrok)} Компьютер:{sum(komp)} \n'
                          f'Будем играть еще? [1-Да , 0-Нет]')
                break
        elif sum(igrok)>=22 and sum(komp)>=22:
            inp = input(f'{name}! Ничья! Результат: Игрок:{sum(igrok)} Компьютер:{sum(komp)}\n'
                      f'Будем играть еще? [1-Да , 0-Нет]')
            break
        if sum(igrok)>=22 and sum (komp)<22:
            inp = input(f'{name}! Вы проиграли! Результат: Игрок:{sum(igrok)} Компьютер:{sum(komp)}  \n'
                        f'Будем играть еще? [1-Да , 0-Нет]')
            break
        elif sum(igrok)<22 and sum (komp)>=22:
            inp = input(f'{name}! Вы выирали! Результат: Игрок:{sum(igrok)} Компьютер:{sum(komp)}  \n'
                        f'Будем играть еще? [1-Да , 0-Нет]')
            break
    if int(inp)==1:
        print('Поехали!')
    else:
        print("Досвидания!")
        break
