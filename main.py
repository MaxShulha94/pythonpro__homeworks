class Product:
    def __init__(self, description, price, size):
        self.description = description
        self.price = int(price)
        self.size = size
        self.type = 'product'

    def __str__(self):
        return f'{self.description} - {self.price}UAH, {self.size} kilogramm'


class Buyer:
    def __init__(self, surname, name, tel_number):
        self.surname = surname
        self.name = name
        self.tel_number = tel_number
        self.type = 'buyer'

    def __str__(self):
        return f'{self.surname}, {self.name}, {self.tel_number}'


class Order:
    def __init__(self, buyer, title):
        self.buyer = buyer
        self.title = title
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        self

    def total_sum(self):
        res = 0
        for self.price, self.size in self.products:
            res += self.price * self



    def __str__(self):
        return f'{self.total_sum}{self.title} : {self.buyer}\n' + '\n'.join(map(str, self.products))


buyer = Buyer('Gump', 'Forrest', '+38098888888')
product1 = Product('Fresh apple', '20', '1')
product2 = Product('Fresh orange', '50', '1')
product3 = Product('Cow\'s milk', '45', '1')
product4 = Product('Goat\'s milk', '55', '1')

products = Order(buyer, 'Purchases')
products.add_product(product2)
products.add_product(product3)
print(products)
