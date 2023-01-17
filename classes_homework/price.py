class Price:

    def __init__(self, amount):
        try:
            self.amount = float(amount)
        except ValueError:
            raise ValueError(f'Invalid amount: {amount}')

    @classmethod
    def from_usd(cls, amount):
        return Price(amount * 3.8)

    @classmethod
    def from_eur(cls, amount):
        return Price(amount * 4.5)

    def __str__(self):
        return f'{self.amount:.2f}'
