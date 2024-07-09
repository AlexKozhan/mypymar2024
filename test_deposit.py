"""
Unit tests for the Bank class in deposit_2 module.
"""

import unittest
from deposit_2 import Bank


class TestBankDeposit(unittest.TestCase):
    """
    Test cases for the Bank class deposit method.
    """

    def setUp(self):
        self.bank = Bank()

    def test_negative_scenario(self):
        """
        Test case to check handling of negative scenarios.
        """
        zero_money = 0
        duration = 7

        with self.assertRaises(ValueError):
            self.bank.deposit(zero_money, duration)

    def test_positive_scenario(self):
        """
        Test case to check handling of positive scenarios.
        """
        initial_money = 125
        duration = 7

        final_money_amount = self.bank.deposit(initial_money, duration)

        self.assertGreater(final_money_amount, initial_money)


if __name__ == '__main__':
    unittest.main()
