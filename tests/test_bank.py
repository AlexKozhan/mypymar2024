"""
This module contains tests for the Bank class.
It uses pytest for testing and
logging to capture log messages.
"""

import logging
import pytest
from bank import Bank

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def bank_instance():
    """
    Fixture to create a Bank instance for testing.

    Returns:
        Bank: A new Bank instance.
    """
    return Bank()


def test_deposit(bank_instance, caplog):
    """
    Test depositing money into the bank account.

    Args:
        bank_instance (fixture): Fixture to
        create a Bank instance.
        caplog (LogCaptureFixture): Fixture to
        capture log messages.
    """
    with caplog.at_level(logging.INFO):
        bank_instance.deposit(100)
    assert bank_instance.balance == 100
    assert ("Deposited 100. New balance "
            "is 100.") in caplog.text


def test_withdraw(bank_instance, caplog):
    """
    Test withdrawing money from the bank account.

    Args:
        bank_instance (fixture): Fixture
        to create a Bank instance.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    bank_instance.deposit(200)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        bank_instance.withdraw(50)
    assert bank_instance.balance == 150
    assert "Withdrew 50. New balance is 150." in caplog.text


def test_withdraw_insufficient_funds(bank_instance, caplog):
    """
    Test withdrawing money when the balance is insufficient.

    Args:
        bank_instance (fixture): Fixture to
        create a Bank instance.
        caplog (LogCaptureFixture): Fixture
        to capture log messages.
    """
    bank_instance.deposit(50)
    caplog.clear()
    with caplog.at_level(logging.INFO):
        bank_instance.withdraw(100)
    assert bank_instance.balance == 50
    assert "Insufficient funds for withdrawal." in caplog.text
