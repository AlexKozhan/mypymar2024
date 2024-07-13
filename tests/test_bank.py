"""
Test suite for the Bank class.
"""

import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))

from bank import Bank

@pytest.fixture
def bank_instance():
    """
    Fixture for creating a Bank instance.
    """
    return Bank()

def test_deposit_positive(bank_instance):
    """
    Test that a positive deposit is calculated correctly.
    """
    expected_amount = 125 * (1 + 0.25 / 12) ** (12 * 7)
    final_amount = bank_instance.deposit(125, 7)
    assert final_amount == pytest.approx(expected_amount, rel=1e-2)

def test_deposit_zero_money(bank_instance):
    """
    Test that depositing zero money raises a ValueError.
    """
    with pytest.raises(ValueError, match="Initial money "
                                         "amount must be positive."):
        bank_instance.deposit(0, 7)

def test_deposit_negative_duration(bank_instance):
    """
    Test that a negative duration raises a ValueError.
    """
    with pytest.raises(ValueError, match="Duration must "
                                         "be a positive integer."):
        bank_instance.deposit(125, -7)
