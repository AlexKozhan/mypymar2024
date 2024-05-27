"""Рассмотрим целые числа от 0 до n-1, записанные
по окружности так, чтобы расстояние между любыми
двумя соседними числами было одинаковым (обратите внимание,
 что 0 и n-1 тоже являются соседними).

Учитывая n и first_number, найдите число, которое
написано в радиально противоположной позиции от first_number

Примеры
Для n = 10 и first_number = 2 вывод должен быть (n, first_number) = 7."""


def searching_number(n, first_number):
    """Method to find opposite number"""
    final_number = (first_number + n // 2) % n
    return final_number


Max_Number1 = 10
First_Number1 = 3
print('(n, first_number) = ', searching_number(Max_Number1, First_Number1))
