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
    """
    Evaluates a mathematical expression given as a string.
    Returns:
    float: The result of the expression evaluation.
    Raises:
    ValueError: If the expression contains invalid characters.
    ZeroDivisionError: If the expression involves division by zero.
    """
    tokens = re.findall(r'[+-]?\d*\.\d+|\d+|[+\-*///**]', expression)

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
                raise ZeroDivisionError("Error: division by zero")
            result /= float(tokens[i])
        elif operator == '//':
            if float(tokens[i]) == 0:
                raise ZeroDivisionError("Error: division by zero")
            result //= float(tokens[i])
        elif operator == '**':
            result **= float(tokens[i])
        else:
            raise ValueError("Error: invalid operator")
        i += 1

    return result


def main():
    """
    Main function of the program. Prompts the user for a
    mathematical expression and prints the result of its
    evaluation.
    """
    print("Enter a mathematical expression (e.g., '10 - 3 + 18'): ")
    user_input = input("~ ")

    try:
        result = calculate_expression(user_input)
        print(f"Result: {result}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")


if __name__ == "__main__":
    main()
