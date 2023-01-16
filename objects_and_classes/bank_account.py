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
            withdrawn_cash = min(self.cash, amount)
            self.cash -= withdrawn_cash
            return withdrawn_cash
        else:
            raise ValueError(f'Invalid amount: {amount}')

    def show_info(self):
        print(f'Account number: {self.number}\nBalance: {self.cash}')


n = 2183961239786128931233
account1 = BankAccount(n)

# account1.deposit_cash(100)
# account1.show_info()
# account1.deposit_cash(200)
# account1.show_info()
# # account1.deposit_cash(-100)
# print(account1.withdraw_cash(100))
# account1.show_info()
# print(account1.withdraw_cash(1000))
# account1.show_info()
# # print(account1.withdraw_cash(-200))
# # account2 = BankAccount('siema')
# # account3 = BankAccount(1231231232123.12312312312312312)
