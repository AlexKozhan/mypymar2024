"""Создайте класс вклад. Который содержит необходимые
 поля и методы, например сумма вклада и его срок.
 Пользователь делает вклад в размере N рублей сроком
 на R лет под 10% годовых (вклад с возможностью ежемесячной
  капитализации - это означает, что проценты прибавляются
   к сумме вклада ежемесячно). Написать класс Bank,
   метод deposit принимает аргументы N и R, и
   возвращает сумму, которая будет на счету
   пользователя."""


import logging


class Bank:
    def __init__(self):
        self.balance = 0
        self.logger = logging.getLogger(__name__)

    def deposit(self, money: float):
        if money <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += money
        self.logger.info(f"Deposited {money}. New "
                         f"balance is {self.balance}.")

    def withdraw(self, money: float):
        if money <= 0:
            raise ValueError("Withdrawal amount must "
                             "be positive.")
        if money > self.balance:
            self.logger.error("Insufficient funds for "
                              "withdrawal.")
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= money
        self.logger.info(f"Withdrew {money}. New balance "
                         f"is {self.balance}.")


INITIAL_MONEY = 125
DURATION = 7

bank = Bank()
bank.deposit(INITIAL_MONEY)

final_money_amount = bank.balance
print(f"Сумма на счету пользователя после "
      f"внесения вклада: {final_money_amount:.2f} рублей")
