"""Напишите декоратор @validate_arguments, который
проверяет, что все аргументы функции являются
положительными числами. Если встречается аргумент,
не соответствующий этому условию, функция должна вывести
сообщение об ошибке. Вот некоторые подсказки:

Внутри декоратора, используйте цикл for для перебора
аргументов функции.
Используйте оператор if для проверки, является ли
аргумент положительным числом.
Если аргумент не соответствует условию, используйте
оператор raise для вызова исключения ValueError."""


def validate_arguments(func):
    """Decorator that checks that all
    function arguments are positive numbers."""
    def wrapper(*args):
        for i in args:
            if i < 0:
                raise ValueError('Числа должны быть положительными')
        return func(*args)
    return wrapper


@validate_arguments
def numbers(*args):
    """Function that prints positive numbers"""
    return f'Введенные числа - положительные: {", ".join(map(str, args))}'


print(numbers(40, 50, 20, 10, 1))
