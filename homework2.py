"""Создайте декоратор, который проверяет, является
ли результат функции числом и выводит сообщение об
ошибке, если это не так. Вот некоторые подсказки:

Внутри декоратора, после вызова функции, проверьте
тип результата с помощью функции isinstance().
Если тип не является числом, выведите сообщение
об ошибке с помощью функции print()."""


def validate_type(func):
    def wrapper(*args):
        inner_result = func(*args)
        if not isinstance(inner_result, (int, float)):
            print(f"Result of function is not a number, instead it's {type(inner_result)}")
            return None
        return inner_result
    return wrapper


@validate_type
def plus_numbers(a, b):
    return a + b


@validate_type
def plus_strings(a, b):
    return a + b


assert plus_numbers(100, 1) == 101, "plus_numbers(100, 1) should return 101"

result = plus_strings("1", "werrere")
assert result is None, "plus_strings('1', 'werrere') should return None due to type error"
