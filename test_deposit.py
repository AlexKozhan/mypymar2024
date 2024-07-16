"""
Unit tests for the Bank class in deposit_2 module.
"""

import unittest
from deposit_2 import Bank, Deposit


class TestBankDeposit(unittest.TestCase):
    """
    Test cases for the Bank class deposit method.
    """

    def setUp(self):
        self.bank = Bank()

    def test_negative_scenario(self):
        """
        Test case to check handling of negative
        scenarios.
        """
        zero_money = 0
        duration = 7

        with self.assertRaises(ValueError):
            self.bank.deposit(zero_money, duration)

    def test_positive_scenario(self):
        """
        Test case to check handling of positive
        scenarios.
        """
        initial_money = 1000
        duration = 1
        expected_amount = 1280.731560657122

        final_money_amount = self.bank.deposit(initial_money,
                                               duration)

        self.assertEqual(final_money_amount, expected_amount)

    def test_calculate_final_money(self):
        """
        Test case to check the calculate_final_money
        method.
        """
        initial_money = 1000
        duration = 1
        expected_amount = 1280.731560657122
        actual_amount = (Deposit.calculate_final_money
                         (initial_money,
                          duration, 0.25))

        self.assertAlmostEqual(actual_amount,
                               expected_amount, places=2,
                               msg=f"Expected "
                                   f"{expected_amount:.2f} "
                                   f"but "
                                   f"got {actual_amount:.2f}")

    def test_negative_deposit_money(self):
        """
        Test case to check handling of negative
        deposit amount.
        """
        negative_money = -1000
        duration = 1

        with self.assertRaises(ValueError):
            self.bank.deposit(negative_money,
                              duration)

    def test_zero_duration(self):
        """
        Test case to check handling of
        zero duration.
        """
        initial_money = 1000
        zero_duration = 0

        with self.assertRaises(ValueError):
            self.bank.deposit(initial_money,
                              zero_duration)


if __name__ == '__main__':
    unittest.main()
