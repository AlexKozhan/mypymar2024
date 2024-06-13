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
    Represents a bank that performs currency exchange.
    """

    def __init__(self):
        self.currency_converter = Currency()

    def exchange_currency(self, from_currency: str,
                          amount: float, to_currency: str = 'BYN') -> tuple:
        """
        Converts the specified amount from one currency to another.

        Args:
            from_currency (str): The currency code to convert from.
            amount (float): The amount to convert.
            to_currency (str, optional): The currency code to
            convert to. Defaults to 'BYN'.

        Returns:
            tuple: A tuple containing the converted amount
            and the currency code.

        Raises:
            ValueError: If invalid currency codes are provided.
        """
        converted_amount = (self.currency_converter.convert
                            (from_currency, to_currency, amount))
        return converted_amount, to_currency


class Currency:
    """
    Represents a currency converter based on predefined exchange rates.
    """

    def __init__(self):
        # Example exchange rates
        self.rates = {
            'USD': {'BYN': 3.269, 'EUR': 0.929},
            'EUR': {'BYN': 3.52, 'USD': 1.076},
            'BYN': {'USD': 0.306, 'EUR': 0.284}
        }

    def convert(self, from_currency: str, to_currency:
    str, amount: float) -> float:
        """
        Converts the specified amount from one currency to another.

        Args:
            from_currency (str): The currency code to convert from.
            to_currency (str): The currency code to convert to.
            amount (float): The amount to convert.

        Returns:
            float: The converted amount.

        Raises:
            ValueError: If invalid currency codes are provided.
        """
        if from_currency not in self.rates or to_currency not in self.rates[from_currency]:
            raise ValueError("Invalid currency codes")

        rate = self.rates[from_currency][to_currency]
        return round(amount * rate, 2)

    def get_supported_currencies(self):
        """
        Returns a list of all supported currency codes.

        Returns:
            list: List of supported currency codes.
        """
        return list(self.rates.keys())

    def update_exchange_rate(self, from_currency: str, to_currency: str, new_rate: float):
        """
        Updates the exchange rate between two currencies.

        Args:
            from_currency (str): The currency code to convert from.
            to_currency (str): The currency code to convert to.
            new_rate (float): The new exchange rate.

        Raises:
            ValueError: If invalid currency codes are provided.
        """
        if from_currency not in self.rates:
            raise ValueError("Invalid from_currency code")
        if to_currency not in self.rates[from_currency]:
            raise ValueError("Invalid to_currency code")

        self.rates[from_currency][to_currency] = new_rate

    def add_currency(self, currency_code: str, exchange_rates: dict):
        """
        Adds a new currency and its exchange rates to the converter.

        Args:
            currency_code (str): The new currency code to add.
            exchange_rates (dict): A dictionary of exchange rates for
            the new currency.

        Raises:
            ValueError: If the currency code already exists.
        """
        if currency_code in self.rates:
            raise ValueError("Currency code already exists")

        self.rates[currency_code] = exchange_rates


class Person:
    """
    Represents a person with a specific currency and amount.
    """

    def __init__(self, currency: str, amount: float):
        """
        Initializes a Person object with given currency and amount.

        Args:
            currency (str): The currency code.
            amount (float): The amount of money.
        """
        self.currency = currency
        self.amount = amount

    def add_amount(self, additional_amount: float):
        """
        Adds the specified amount to the current amount.

        Args:
            additional_amount (float): The amount to add.
        """
        self.amount += additional_amount

    def withdraw_amount(self, withdrawal_amount: float):
        """
        Withdraws the specified amount from the current amount.

        Args:
            withdrawal_amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount exceeds the current amount.
        """
        if withdrawal_amount > self.amount:
            raise ValueError("Withdrawal amount exceeds current amount")
        self.amount -= withdrawal_amount

    def check_balance(self):
        """
        Returns the current amount balance.
        """
        return self.amount


# Example usage and testing
if __name__ == "__main__":
    bank = Bank()

    vasya = Person('USD', 10)
    petya = Person('EUR', 5)

    # Testing conversion to default currency 'BYN'
    assert (bank.exchange_currency(vasya.currency, vasya.amount)
            == (32.69, "BYN")), "Error converting from USD to BYN"
    assert (bank.exchange_currency(petya.currency, petya.amount)
            == (17.6, "BYN")), "Error converting from EUR to BYN"

    # Testing conversion to specified currency
    assert bank.exchange_currency(vasya.currency, vasya.amount, 'EUR') == (
    9.29, "EUR"), "Error converting from USD to EUR"
    assert bank.exchange_currency(petya.currency, petya.amount, 'USD') == (
    5.38, "USD"), "Error converting from EUR to USD"

    # Testing Person class methods
    vasya.add_amount(20)
    assert vasya.check_balance() == 30, "Error in adding amount to vasya"

    petya.withdraw_amount(3)
    assert petya.check_balance() == 2, "Error in withdrawing amount from petya"

    currency = Currency()
    currency.update_exchange_rate('USD', 'EUR', 0.93)
    assert (currency.convert('USD', 'EUR', 10)
            == 9.3), "Error in updating exchange rate"

    currency.add_currency('GBP', {'USD': 1.25, 'EUR': 1.15})
    assert (currency.convert('GBP', 'USD', 10)
            == 12.5), "Error in adding new currency"
