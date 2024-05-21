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
    Chislo_Igroka = input("Введите 4-значное число с неповторяющимися цифрами: ")
    """Checking input number to have 4 unique digits"""
    if len(Chislo_Igroka)!=4 or not Chislo_Igroka.isdigit() or len(set(Chislo_Igroka))!=4:
        print('Вы ввели некорректное число, читайте внимательнее и попробуйте еще раз')
        continue

    Byki = 0
    Korovi = 0
    """Cheking how many Byki and Korovi we guessed right"""
    for i in range(4):
        if Chislo_Igroka[i] == Chislo_PK[i]:
            Byki+=1
        elif Chislo_Igroka[i] in Chislo_PK:
            Korovi+=1
    print(F"{Korovi} коров(ы), {Byki} бык(а)")

    if Byki==4:
        """Finishin the game"""
        print('Вы выиграли!')
        break
