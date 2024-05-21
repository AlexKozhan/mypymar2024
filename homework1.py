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


# Пример
# Загадано
# 2310
# Две коровы, один бык
# 3219
# Вы выиграли!

"""Generated list of 4 random unique numbers"""
import random
Chislo_PK_List = random.sample('0123456789', 4)
"""Changing type list to type string"""
CHISLO_PK = ''.join(Chislo_PK_List)
print("Загадано")

while True:
    Chislo_Igroka = input("Введи 4-значное число с неповторяющимися цифрами ")
    """Checking input number to have 4 unique digits"""
    if (len(Chislo_Igroka) != 4 or not Chislo_Igroka.isdigit()
            or len(set(Chislo_Igroka)) != 4):
        print('Вы ввели некорректное число, попробуйте еще раз')
        continue

    KOLVO_BYKI = 0
    KOLVO_KOROVI = 0
    """Cheking how many  KOLVO_BYKI and KOLVO_KOROVI we guessed right"""
    for i in range(4):
        if Chislo_Igroka[i] == CHISLO_PK[i]:
            KOLVO_BYKI += 1
        elif Chislo_Igroka[i] in CHISLO_PK:
            KOLVO_KOROVI += 1
    print(F"{KOLVO_KOROVI} коров(ы), {KOLVO_BYKI} бык(а)")

    """When we guessed right game stops"""
    if KOLVO_BYKI == 4:
        print('Вы выиграли!')
        break
