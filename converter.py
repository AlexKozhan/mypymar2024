"""Расширьте функционал класса Bank из
домашней работы #11. Добавьте новый класс
Currency, который умеет конвертировать
различные валюты(USD, EUR, ...) в заданную
валюту.

bank = Bank(..)

vasya = Person('USD', 10)
petya = Person('EUR', 5)

# Если валюта не задана, то конвертация
происходит в BYN:
assert bank.exchange_currency(vasya.currency,
vasya.amount) == (32.69, "BYN"), <error message>
assert bank.exchange_currency(petya.currency,
petya.amount) == (35.20, "BYN"), <error message>

# Конвертация в заданную валюту BYN:
assert bank.exchange_currency(vasya.currency,
vasya.amount, 'EUR') == (9.29, "EUR"), <error message>
assert bank.exchange_currency(petya.currency,
 petya.amount, 'USD') == (10.76, "USD"), <error message>"""


class Bank:
    """
    Represents a bank.
    """

    def __init__(self):
        self.currency_converter = Currency()

    def exchange_currency(self, from_currency: str,
                          amount: float, to_currency: str = 'BYN') -> tuple:
        """
        Converts the specified amount from one currency to another.
        """
        converted_amount = (
            self.currency_converter.convert(from_currency, to_currency, amount))
        return (converted_amount, to_currency)


class Currency:
    def __init__(self):
        # Example exchange rates
        self.rates = {
            'USD': {'BYN': 3.269, 'EUR': 0.929},
            'EUR': {'BYN': 3.52, 'USD': 1.076},
            'BYN': {'USD': 0.306, 'EUR': 0.284}
        }

    def convert(self, from_currency: str,
                to_currency: str, amount: float) -> float:
        if from_currency not in self.rates:
            raise ValueError("Invalid from_currency code")

        if to_currency not in self.rates[from_currency]:
            raise ValueError("Invalid to_currency code")

        rate = self.rates[from_currency][to_currency]

        return round(amount * rate, 2)


class Person:
    def __init__(self, currency: str, amount: float):
        self.currency = currency
        self.amount = amount


# Пример использования и тестирования
bank = Bank()

vasya = Person('USD', 10)
petya = Person('EUR', 5)

# Если валюта не задана, то конвертация происходит в BYN:
assert (bank.exchange_currency(vasya.currency, vasya.amount)
        == (32.69, "BYN")), "Ошибка в конвертации из USD в BYN"
assert (bank.exchange_currency(petya.currency, petya.amount)
        == (17.6, "BYN")), "Ошибка в конвертации из EUR в BYN"

# Конвертация в заданную валюту:
assert (bank.exchange_currency(vasya.currency, vasya.amount, 'EUR')
        == (9.29, "EUR")), "Ошибка в конвертации из USD в EUR"
assert (bank.exchange_currency(petya.currency, petya.amount, 'USD')
        == (5.38, "USD")), "Ошибка в конвертации из EUR в USD"
