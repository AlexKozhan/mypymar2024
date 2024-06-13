"""Напишите программу - инженерный калькулятор.
Передусмотрите возможные ошибки и обработайте их.
 ~ - это предложение ввода.

Базовые требования:

Программа считает простые математические выражения:
~ 5 + 4 9

Программа ожидает от пользователя ввода
математического выражения и правильно его трактует:
~ 10 - 3 + 1 8 ~ 2 ** 3 - 1 7"""


import re
import sys


def calculate_expression(expression):
    tokens = re.findall(r'[+-]?\d*\.\d+|\d+|[+-/*//**]', expression)

    result = float(tokens[0])

    i = 1
    while i < len(tokens):
        operator = tokens[i]
        i += 1
        if operator == '+':
            result += float(tokens[i])
        elif operator == '-':
            result -= float(tokens[i])
        elif operator == '*':
            result *= float(tokens[i])
        elif operator == '/':
            if float(tokens[i]) == 0:
                print("Ошибка: деление на ноль")
                sys.exit(1)
            result /= float(tokens[i])
        elif operator == '//':
            if float(tokens[i]) == 0:
                print("Ошибка: деление на ноль")
                sys.exit(1)
            result //= float(tokens[i])
        elif operator == '**':
            result **= float(tokens[i])
        else:
            print("Ошибка: недопустимый оператор")
            sys.exit(1)
        i += 1

    return result


def main():
    print("Введите математическое выражение (например, '10 - 3 + 18'): ")
    user_input = input("~ ")

    try:
        result = calculate_expression(user_input)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
