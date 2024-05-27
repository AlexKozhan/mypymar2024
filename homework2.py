"""Рассмотрим целые числа от 0 до n-1, записанные
по окружности так, чтобы расстояние между любыми
двумя соседними числами было одинаковым (обратите внимание,
 что 0 и n-1 тоже являются соседними).

Учитывая n и first_number, найдите число, которое
написано в радиально противоположной позиции от first_number

Примеры
Для n = 10 и first_number = 2 вывод должен быть (n, first_number) = 7."""


def searching_number(MAX_NUMBER, FIRST_NUMBER):
    """Method to find opposite number"""
    final_number = (FIRST_NUMBER + MAX_NUMBER // 2) % MAX_NUMBER
    return final_number


MAX_NUMBER1 = 10
FIRST_NUMBER1 = 3
print('(n, first_number) = ', searching_number(MAX_NUMBER1, FIRST_NUMBER1))

MAX_NUMBER2 = 9
FIRST_NUMBER2 = 2
print('(n, first_number) = ', searching_number(MAX_NUMBER2, FIRST_NUMBER2))
