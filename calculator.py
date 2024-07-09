"""Напишите программу - инженерный калькулятор.
Передусмотрите возможные ошибки и обработайте
их. ~ - это предложение ввода.

Базовые требования:

Программа считает простые математические выражения:
~ 5 + 4 9

Программа ожидает от пользователя ввода
математического выражения и правильно его трактует:
~ 10 - 3 + 1 8 ~ 2 ** 3 - 1 7"""


import re
from collections import deque


def tokenize(expression):
    """
    Tokenizes a mathematical expression string into tokens.

    Args:
    expression (str): The mathematical expression to tokenize.

    Returns:
    deque: A deque containing tokens extracted from the expression.
    """
    return deque(re.findall(r'\d+\.\d+|\d+|\*\*|[+\-*/()]', expression))


def parse_expression(tokens):
    """
    Parses a mathematical expression represented by tokens,
    respecting operator precedence.

    Args:
    tokens (deque): Tokens representing the mathematical expression.

    Returns:
    float: The result of evaluating the expression.

    Raises:
    ValueError: If a token cannot be converted to float.
    ZeroDivisionError: If division by zero is encountered.
    """
    term = parse_term(tokens)
    while tokens and tokens[0] in ('+', '-'):
        op = tokens.popleft()
        right = parse_term(tokens)
        term = term + right if op == '+' else term - right
    return term


def parse_term(tokens):
    """
    Parses terms (multiplication, division, floor division) in the expression.

    Args:
    tokens (deque): Tokens representing the mathematical expression.

    Returns:
    float: The result of evaluating the term.
    """
    term = parse_factor(tokens)
    while tokens and tokens[0] in ('*', '/', '//'):
        op = tokens.popleft()
        right = parse_factor(tokens)
        if op == '*':
            term *= right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Error: division by zero")
            term /= right
        elif op == '//':
            if right == 0:
                raise ZeroDivisionError("Error: division by zero")
            term //= right
    return term


def parse_factor(tokens):
    """
    Parses factors (exponentiation) in the expression.

    Args:
    tokens (deque): Tokens representing the mathematical expression.

    Returns:
    float: The result of evaluating the factor.
    """
    factor = parse_primary(tokens)
    while tokens and tokens[0] == '**':
        tokens.popleft()
        exponent = parse_primary(tokens)
        factor **= exponent
    return factor


def parse_primary(tokens):
    """
    Parses primary expressions (numbers or sub-expressions in parentheses).

    Args:
    tokens (deque): Tokens representing the mathematical expression.

    Returns:
    float: The result of evaluating the primary expression.

    Raises:
    ValueError: If a token inside the primary expression
    cannot be converted to float.
    """
    token = tokens.popleft()
    if token == '(':
        expr = parse_expression(tokens)
        tokens.popleft()  # Remove the closing parenthesis ')'
        return expr
    try:
        return float(token)
    except ValueError:
        raise ValueError(f"Error: could not convert "
                         f"token '{token}' to float") from None


def calculate_expression(expression):
    """
    Evaluates a mathematical expression provided as a string.

    Args:
    expression (str): The mathematical expression to evaluate.

    Returns:
    float: The result of evaluating the expression.

    Raises:
    ValueError: If the expression contains invalid characters or tokens.
    ZeroDivisionError: If division by zero is encountered.
    """
    if not re.match(r'^[0-9+\-*/.()//** ]*$', expression):
        raise ValueError("Error: invalid characters in expression")

    try:
        tokens = tokenize(expression)
        result = parse_expression(tokens)
        return result
    except ZeroDivisionError as zde:
        raise ZeroDivisionError(f"Error: {zde}") from zde
    except ValueError as ve:
        raise ValueError(f"Error: {ve}") from ve
    except Exception as e:
        raise ValueError(f"Error: {e}") from e


def main():
    """
    Main function of the program. Prompts the
    user for a mathematical expression
    and prints the result of its evaluation.
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
