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
    def calculate_final_money(self, money: float, duration: int,
                              annual_rate: float = 0.25) -> float:
        """
        Calculates the total deposit amount taking
        into account the monthly capitalization of interest.
        """
        m = money
        n = 12
        y = duration
        r = annual_rate
        a = m * (1 + r / n) ** (n * y)
        return a


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
        final_money = deposit_instance.calculate_final_money(money, duration)
        return final_money


INITIAL_MONEY = 125
DURATION = 7

bank = Bank()
final_money = bank.deposit(INITIAL_MONEY, DURATION)
print(f"Сумма на счету пользователя через {DURATION} "
      f"лет: {final_money:.2f} рублей")
