"""Homework6"""


""" This is a docstring which describes the module:
Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]"""
FIRST_LINE = "Robin Singh"
print(list(FIRST_LINE.split()))


""" This is a docstring which describes the module:
"I love arrays they are my favorite" =>
["I", "love", "arrays", "they", "are", "my", "favorite"]"""
SECOND_LINE = "I love arrays they are my favorite"
print(list(SECOND_LINE.split()))


"""This is a docstring which describes the module:
Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
Напечатайте текст: 'Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus'"""
THIRD_LINE = ["Ivan", "Ivanov"]
CITY_LINE = "Minsk"
STRANA_LINE = "Belarus"
print(f"Привет, {' '.join(THIRD_LINE)}! "
      f"Добро пожаловать в {CITY_LINE} {STRANA_LINE}")


"""This is a docstring which describes the module:
Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
сделайте из него строку => '"'I love arrays they are my favorite'"""
NEW_SPISOK = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(NEW_SPISOK))


"""This is a docstring which describes the module:
Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
удалите элемент из списка под индексом 6"""
OLD_SPISOK = [
    "I", "love", "arrays", "they", "are",
    "my", "favorite", "python", "learning", "instrument"
    ]
OLD_SPISOK[2] = "tuples"
del OLD_SPISOK[6]
print(OLD_SPISOK)
