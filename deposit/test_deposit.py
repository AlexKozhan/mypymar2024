"""
This module contains test functions for the deposit
functionality
of the Bank class, which handles deposit calculations
with monthly
capitalization of interest.
"""


from deposit_2 import Bank


def test_deposit_positive():
    """
    Test the deposit function with a positive amount
    and a valid duration.

    Returns:
        float: The final amount on the deposit after
        the specified duration.
    """
    bank = Bank()
    result = bank.deposit(125, 7)
    return result


def test_deposit_zero_money():
    """
    Test the deposit function with a zero amount
    and a valid duration.

    Returns:
        float: The final amount on the deposit
        after the specified duration.
    """
    bank = Bank()
    result = bank.deposit(0, 7)
    return result


def test_deposit_zero_duration():
    """
    Test the deposit function with a positive
    amount and a zero duration.

    Returns:
        float: The final amount on the deposit
        after the specified duration.
    """
    bank = Bank()
    result = bank.deposit(125, 0)
    return result


def test_deposit_negative_money():
    """
    Test the deposit function with a negative
    amount and a valid duration.

    Returns:
        float: The final amount on the deposit
        after the specified duration.
    """
    bank = Bank()
    result = bank.deposit(-125, 7)
    return result


def test_deposit_negative_duration():
    """
    Test the deposit function with a positive
    amount and a negative duration.

    Returns:
        float: The final amount on the deposit
        after the specified duration.
    """
    bank = Bank()
    result = bank.deposit(125, -7)
    return result
