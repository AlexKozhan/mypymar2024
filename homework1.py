"""Дана последовательность целых чисел в виде массива.
 Определите, можно ли получить строго возрастающую последовательность,
  удалив из массива не более одного элемента.

Примечание: последовательность a0, a1, ..., an считается строго возрастающей,
 если a0 < a1 < ... < an. Последовательность, содержащая только один элемент,
 также считается строго возрастающей.

Примеры
Для последовательности = [1, 3, 2, 1], вывод должен быть решение = False.

В этом массиве нет ни одного элемента, который можно было бы удалить,
чтобы получить строго возрастающую последовательность.

Для последовательности = [1, 3, 2] вывод должен быть = True.

Вы можете удалить 3 из массива, чтобы получить строго возрастающую
последовательность [1, 2]. Альтернативно можно убрать 2, чтобы получить
строго возрастающую последовательность [1, 3].

solution([1, 2, 3])
solution([1, 2, 1, 2])
solution([1, 3, 2, 1])
solution([1, 2, 3, 4, 5, 3, 5, 6])
solution([40, 50, 60, 10, 20, 30])"""


def is_increasing(massiv):
    """Cheking if out list is not increasing"""
    for i in range(1, len(massiv)):
        if massiv[i] <= massiv[i - 1]:
            return False
    return True


def strictly_increasing_without_one_element(massiv):
    """If previous function works then we have increasing list"""
    if is_increasing(massiv):
        return True

    for i in range(len(massiv)):
        """A try to delete 1 element in list to have increased list"""
        temp_massiv = massiv[:i] + massiv[i + 1:]
        if is_increasing(temp_massiv):
            return True

    return False


solution1 = [1, 2, 3]
solution2 = [1, 2, 1, 2]
solution3 = [1, 3, 2, 1]
solution4 = [1, 2, 3, 4, 5, 3, 5, 6]
solution5 = [40, 50, 60, 10, 20, 30]

print(strictly_increasing_without_one_element(solution1))
print(strictly_increasing_without_one_element(solution2))
print(strictly_increasing_without_one_element(solution3))
print(strictly_increasing_without_one_element(solution4))
print(strictly_increasing_without_one_element(solution5))
