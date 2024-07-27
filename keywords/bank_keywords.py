from bank import Bank


class BankKeywords:
    def create_bank(self):
        return Bank()

    def deposit_money(self, bank, money, duration):
        return bank.deposit(money, duration)
