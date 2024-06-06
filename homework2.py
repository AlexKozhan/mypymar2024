"""Создайте класс вклад. Который содержит необходимые
 поля и методы, например сумма вклада и его срок.
 Пользователь делает вклад в размере N рублей сроком
 на R лет под 10% годовых (вклад с возможностью ежемесячной
  капитализации - это означает, что проценты прибавляются
   к сумме вклада ежемесячно). Написать класс Bank,
   метод deposit принимает аргументы N и R, и
   возвращает сумму, которая будет на счету пользователя."""


class Deposit:
    def calculate_final_money(self, money: float, years: int,
                              annual_rate: float = 0.25):
        """
        Calculates the total deposit amount taking
        into account the monthly capitalization of interest.
        """
        m = money
        n = 12
        y = years
        r = annual_rate
        a = m * (1 + r / n) ** (n * y)
        return a


class Bank:
    def deposit(self, money: float, years: int):
        """
        Accepts the deposit amount and term, returns the total
        amount to the user's account.
        """
        deposit = Deposit()
        final_money = deposit.calculate_final_money(money, years)
        return final_money


initial_money = 125
years = 7

bank = Bank()
final_money = bank.deposit(initial_money, years)
print(f"Сумма на счету пользователя через {years} лет: {final_money:.2f} рублей")
