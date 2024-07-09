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
        initial_money = 1000
        duration = 1
        expected_amount = 1280.731560657122

        final_money_amount = self.bank.deposit(initial_money, duration)

        self.assertEqual(final_money_amount, expected_amount)


if __name__ == '__main__':
    unittest.main()
