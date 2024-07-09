"""Создайте декоратор, который проверяет, является
ли результат функции числом и выводит сообщение об
ошибке, если это не так. Вот некоторые подсказки:

Внутри декоратора, после вызова функции, проверьте
тип результата с помощью функции isinstance().
Если тип не является числом, выведите сообщение
об ошибке с помощью функции print()."""


def validate_type(func):
    """Decorator that checks the type of a function's result."""
    def wrapper(*args):
        inner_result = func(*args)
        if not isinstance(inner_result, (int, float)):
            print(f"Result of function is "
                  f"not a number, instead it's {type(inner_result)}")
            return False
        return inner_result
    return wrapper


@validate_type
def plus_two_value(a, b):
    """Function for concatenating two values"""
    return a + b


assert plus_two_value(100, 1) == 101, ("plus_two_value(100, 1) "
                                       "should return 101")

RESULT = plus_two_value("1", "werrere")
assert RESULT is None, ("plus_two_value('1', 'werrere') should "
                        "return None due to type error")
