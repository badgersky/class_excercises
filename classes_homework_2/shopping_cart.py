available_ids = list(range(1, 1000))
available_ids = available_ids[::-1]


class Product:

    def __init__(self, name, price):
        self.id = available_ids.pop()
        self.price = price
        self.name = name


class ShoppingCart:

    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        if product not in self.products:
            self.products[product.id] = product
            self.quantities[product.id] = 1
        else:
            self.quantities[product.id] += 1

    def change_product_quantity(self, product, new_quantity):
        if new_quantity < 0:
            raise ValueError(f'Invalid quantity: {new_quantity}')
        if new_quantity == 0:
            del self.products[product.id]
            del self.quantities[product.id]
        else:
            self.quantities[product.id] = new_quantity

    def remove_product(self, product):
        del self.products[product.id]
        del self.quantities[product.id]

    def get_receipt(self):
        output = ''
        total = 0
        for idnum, p in self.products.items():
            output += f'\n{p.name.title()} - amount: {self.quantities[idnum]},' \
                      f' price: {p.price}zł,' \
                      f' total: {self.quantities[idnum] * p.price}zł'
            total += self.quantities[idnum] * p.price

        return output + '\nTotal: ' + str(total) + 'zł'
