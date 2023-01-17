class Cart:

    def __init__(self):
        self.products = []

    def add(self, price, name):
        if price < 0:
            raise ValueError(f'Invalid price: {price}')
        self.products.append((price, name))

    def summary(self):
        return sum([product[0] for product in self.products])


class Discount20PercentCart(Cart):

    def __init__(self):
        super().__init__()

    def summary(self):
        return [(product[0] * 0.80, product[1]) for product in self.products]


class Above3ProductsCheapestFreeCart(Cart):

    def __init__(self):
        super().__init__()

    def summary(self):
        prices = [product[0] for product in self.products]
        if len(prices) > 3:
            prices[prices.index(min(prices))] = 0

        return [(price, self.products[i]) for i, price in enumerate(prices)]
