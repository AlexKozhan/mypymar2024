# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
a = "Robin Singh"
print(list(a.split(" ")))


# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
b = "I love arrays they are my favorite"
print(list(b.split(" ")))


# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
c = ["Ivan", "Ivanov"]
d = "Minsk"
e = "Belarus"
print(f"Привет, {' '.join(c)}! "
      f"Добро пожаловать в {d} {e}")


# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
f = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(f))


# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
u = [
    "I", "love", "arrays", "they", "are",
    "my", "favorite", "python", "learning", "instrument"
    ]
u[2] = "tuples"
del u[6]
print(u)
