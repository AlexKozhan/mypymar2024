"""
This module contains tests for the Bank class.
It uses pytest for testing and logging
to capture log messages.
"""
# pylint: disable=E0401,C0411,W0621

import pytest
import logging
from bank import Bank


@pytest.fixture
def bank_instance():
    return Bank()


def test_deposit(bank_instance, caplog):
    bank_instance.deposit(100)
    assert bank_instance.balance == 100
    assert ("Deposited 100. New balance is 100."
            in caplog.text)


def test_withdraw(bank_instance, caplog):
    bank_instance.deposit(200)
    bank_instance.withdraw(50)
    assert bank_instance.balance == 150
    assert ("Withdrew 50. New balance is 150."
            in caplog.text)


def test_withdraw_insufficient_funds(bank_instance,
                                     caplog):
    bank_instance.deposit(50)

    caplog.set_level(logging.INFO)

    with pytest.raises(ValueError, match="Insufficient funds for withdrawal."):
        bank_instance.withdraw(100)
    assert bank_instance.balance == 50
    assert any("Insufficient funds for withdrawal." in record.message
               for record in caplog.records)
