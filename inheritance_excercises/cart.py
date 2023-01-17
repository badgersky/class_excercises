class Cart:

    def __init__(self):
        self.products = []

    def add(self, price, name):
        if price < 0:
            raise ValueError(f'Invalid price: {price}')
        self.products.append((price, name))

    def summary(self):
        price = 0
        for product in self.products:
            price += product[0]
        return price

    