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


if __name__ == '__main__':
    bread = Product('bread', 2.70)
    ham = Product('ham', 8.40)
    cheese = Product('cheese', 4.40)
    chive = Product('chive', 1.50)
    pepper = Product('pepper', 2.35)

    print(bread.id)
    print(pepper.id)
    print(pepper.name)
    print(pepper.price)

    cart = ShoppingCart()
    print(cart.products)
    print(cart.quantities)
    print(cart.get_receipt())

    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(pepper)
    cart.add_product(chive)
    print(cart.products)
    print(cart.quantities)
    cart.change_product_quantity(pepper, 2)
    print(cart.products)
    print(cart.quantities)
    cart.remove_product(bread)
    print(cart.products)
    print(cart.quantities)
    print(cart.get_receipt())
    