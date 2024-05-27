"""Рассмотрим целые числа от 0 до n-1, записанные
по окружности так, чтобы расстояние между любыми
двумя соседними числами было одинаковым (обратите внимание,
 что 0 и n-1 тоже являются соседними).

Учитывая n и first_number, найдите число, которое
написано в радиально противоположной позиции от first_number

Примеры
Для n = 10 и first_number = 2 вывод должен быть (n, first_number) = 7."""


def searching_number(max_number, first_number):
    """Method to find opposite number"""
    final_number = (first_number + max_number // 2) % max_number
    return final_number


max_number1 = 10
first_number1 = 3
print('(n, first_number) = ', searching_number(max_number1, first_number1))

max_number2 = 9
first_number2 = 2
print('(n, first_number) = ', searching_number(max_number2, first_number2))
