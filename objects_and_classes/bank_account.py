class BankAccount:

    def __init__(self, number):
        if type(number) != int:
            raise ValueError(f'Invalid number: {number}')
        else:
            self.number = number
            self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0.0:
            self.cash += amount
        else:
            raise ValueError(f'Invalid amount: {amount}')

    def withdraw_cash(self, amount):
        if amount > 0.0:
            return min(self.cash - amount, amount)
        else:
            raise ValueError(f'Invalid amount: {amount}')
