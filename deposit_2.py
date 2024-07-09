"""Создайте класс вклад. Который содержит необходимые
 поля и методы, например сумма вклада и его срок.
 Пользователь делает вклад в размере N рублей сроком
 на R лет под 10% годовых (вклад с возможностью ежемесячной
  капитализации - это означает, что проценты прибавляются
   к сумме вклада ежемесячно). Написать класс Bank,
   метод deposit принимает аргументы N и R, и
   возвращает сумму, которая будет на счету пользователя."""


class Deposit:
    """
    Represents a deposit.
    """

    @staticmethod
    def calculate_final_money(money: float, duration: int,
                              annual_rate: float = 0.25) -> float:
        """
        Calculates the total deposit amount taking
        into account the monthly capitalization of interest.
        """
        n = 12  # Monthly capitalization
        return money * (1 + annual_rate / n) ** (n * duration)

    def __str__(self):
        """
        Returns information about the deposit.
        """
        return "This class represents a deposit."


class Bank:
    """
    Represents a bank.
    """

    def __init__(self):
        pass

    def deposit(self, money: float, duration: int) -> float:
        """
        Accepts the deposit amount and term, returns the total
        amount to the user's account.
        """
        deposit_instance = Deposit()
        final_money_result = (deposit_instance.calculate_final_money
                              (money, duration))
        return final_money_result

    def __str__(self):
        """
        Returns information about the bank.
        """
        return "This class represents a bank."


INITIAL_MONEY = 125
DURATION = 7

bank = Bank()
final_money_amount = bank.deposit(INITIAL_MONEY, DURATION)
print(f"Сумма на счету пользователя "
      f"через {DURATION} лет: {final_money_amount:.2f} рублей")
