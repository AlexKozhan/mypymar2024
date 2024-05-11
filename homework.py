"""Homework6"""


# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
FIRST_LINE = "Robin Singh"
"""printing the list out of string"""
print(list(FIRST_LINE.split()))


# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
SECOND_LINE = "I love arrays they are my favorite"
"""printing the list out of string"""
print(list(SECOND_LINE.split()))


# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: 'Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus'
THIRD_LINE = ["Ivan", "Ivanov"]
CITY_LINE = "Minsk"
STRANA_LINE = "Belarus"
"""printing the text out of string and list"""
print(f"Привет, {' '.join(THIRD_LINE)}! "
      f"Добро пожаловать в {CITY_LINE} {STRANA_LINE}")


# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => '"'I love arrays they are my favorite'
NEW_SPISOK = ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""printing the string out of list"""
print(" ".join(NEW_SPISOK))


# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
OLD_SPISOK = [
    "I", "love", "arrays", "they", "are",
    "my", "favorite", "python", "learning", "instrument"
    ]
OLD_SPISOK[2] = "tuples"
del OLD_SPISOK[6]
"""printing list with another 3rd element and deleted 6th"""
print(OLD_SPISOK)
