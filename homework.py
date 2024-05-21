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

import random
"""Generating list of 4 unique numbers for PK"""
Chislo_PK_List = random.sample('0123456789', 4)
"""Changing type list to type string"""
Chislo_PK = ''.join(Chislo_PK_List)
print("Загадано", Chislo_PK)

while True:
    Chislo_Igroka = input("Введи 4-значное число с неповторяющимися цифрами ")
    """Checking input number to have 4 unique digits"""
    if (len(Chislo_Igroka) != 4 or not Chislo_Igroka.isdigit()
            or len(set(Chislo_Igroka)) != 4):
        print('Вы ввели некорректное число, попробуйте еще раз')
        continue

    Byki = 0
    Korovi = 0
    """Cheking how many Byki and Korovi we guessed right"""
    for i in range(4):
        if Chislo_Igroka[i] == Chislo_PK[i]:
            Byki += 1
        elif Chislo_Igroka[i] in Chislo_PK:
            Korovi += 1
    print(F"{Korovi} коров(ы), {Byki} бык(а)")

    if Byki == 4:
        """Finishin the game"""
        print('Вы выиграли!')
        break


"""Мы можем визуализировать художественную
пирамиду ASCII с N уровнями,
напечатав N рядов звездочек, где верхний ряд
имеет одну звездочку
в центре, а каждый последующий ряд имеет две
дополнительные звездочки с каждой стороны."""

# Вот как это выглядит, когда N равно 3.

#   *
#  ***
# *****
# Вот как это выглядит, когда N равно 5.

#     *
#    ***
#   *****
#  *******
# *********
# Необходимо написать программу, которая
# генерирует такую пирамиду
# со значением N, равным 10

N = 10
"""creating stars and white spaces for piramida"""
for i in range(N):
        stars = 2*i+1
    probeli = N-i-1
    piramida = ' ' * probeli + '*' * stars
    print(piramida)


"""Вы получили в подарок на день рождения статуи
разных размеров, каждая статуя имеет неотрицательный
целочисленный размер. Поскольку Вам нравится доводить
вещи до совершенства, то необходимо расположить их от
меньшего к большему, чтобы каждая статуя была больше
предыдущей ровно на 1. Для этого Вам могут понадобиться
дополнительные статуи. Определите количество отсутствующих
статуй.

Пример Для статуй = [6, 2, 3, 8] результат должен быть = 3.
Иными словами, у Вас отсутствуют статуи размеров 4, 5 и 7."""

Statui_List = [6, 2, 3, 8]
Min_Statuya = min(Statui_List)
Max_Statuya = max(Statui_List)
Missing_Statui = []
"""Finding elements not in Statui_List"""
for i in range(Min_Statuya, Max_Statuya + 1):
    if i not in Statui_List:
        Missing_Statui.append(i)
MISSING_STATUI_STRING = ', '.join(map(str, Missing_Statui))
print(f"Не хватает {len(MISSING_STATUI_STRING)} статуй")
print(f"У вас отсутсвуют статуи размеров {MISSING_STATUI_STRING}")
