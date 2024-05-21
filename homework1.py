"""В классическом варианте игра рассчитана
на двух игроков. Каждый из игроков задумывает
и записывает тайное 4-значное число с
неповторяющимися цифрами. Игрок, который начинает
игру по жребию, делает первую попытку отгадать число.
Попытка — это 4-значное число с неповторяющимися цифрами,
сообщаемое противнику. Противник сообщает в ответ, сколько
цифр угадано без совпадения с их позициями в тайном числе
(то есть количество коров) и сколько угадано вплоть до
позиции в тайном числе (то есть количество быков).
При игре против компьютера игрок вводит комбинации одну
за другой, пока не отгадает всю последовательность.
Ваша задача реализовать программу, против которой
можно сыграть в "Быки и коровы"."""

import random

# Пример
# Загадано
# 2310
# Две коровы, один бык
# 3219
# Вы выиграли!

Chislo_PK_List = random.sample('0123456789', 4)
"""Generated list of 4 random unique numbers
and changing type list to type string"""
CHISLO_PK = ''.join(Chislo_PK_List)
print("Загадано")

while True:
    chislo_igroka = input("Введи 4-значное число с неповторяющимися цифрами ")
    """Checking input number to have 4 unique digits"""
    if (len(chislo_igroka) != 4 or not chislo_igroka.isdigit()
            or len(set(chislo_igroka)) != 4):
        print('Вы ввели некорректное число, попробуйте еще раз')
        continue

    kolvo_byki = 0
    KOLVO_KOROVI = 0
    """Cheking how many  kolvo_byki and KOLVO_KOROVI we guessed right"""
    for i in range(4):
        if chislo_igroka[i] == CHISLO_PK[i]:
            kolvo_byki += 1
        elif chislo_igroka[i] in CHISLO_PK:
            KOLVO_KOROVI += 1
    print(F"{KOLVO_KOROVI} коров(ы), {kolvo_byki} бык(а)")

    if kolvo_byki == 4:
        print('Вы выиграли!')
        break
