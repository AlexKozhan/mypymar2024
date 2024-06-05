"""Напишите декоратор, который проверял бы тип
параметров функции, конвертировал их если надо и складывал:

@typed(type=str)
def add(a, b):
    return a + b

add("3", 5) -> "8"
add(5, 5) -> "55"
add('a', 'b') -> 'ab’

@typed(type=int)
def add(a, b, с):
    return a + b + с

add(5, 6, 7) -> 18

@typed(type=float)
def add(a, b, с):
    return a + b + с

add(0.1, 0.2, 0.4) -> 0.7000000000000001"""


def typed(data_type):
    def inner(func):
        def wrapper(*args):
            converted_args = map(data_type, args)
            return func(*converted_args)
        return wrapper
    return inner


@typed(data_type=str)
def add(a, b):
    return a + b


@typed(data_type=int)
def add_int(a, b, c):
    return a + b + c


@typed(data_type=float)
def add_float(a, b, c):
    return a + b + c


assert add("3", 5) == "35", "An error occured"
assert add(5, 5) == "55", "An error occured"
assert add('a', 'b') == "ab", "An error occured"
assert add_int(5, 6, 7) == 18, "An error occured"
assert add_float(0.1, 0.2, 0.4) == 0.7000000000000001, "An error occured"
