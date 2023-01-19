class NegativePriceError(Exception):
    def __int__(self, message):
        self.message = message

    # def __str__(self):
    #     return f'{self.message}'



class Product:

    def __init__(self, title: str, price: int | float):

        self.title = title
        self.price = price

    #def price_test(self):
        if self.price <= 0:
            raise NegativePriceError('Price can not be zero or less!')

    def __str__(self):
        return f'{self.title}: {self.price} UAH'


class Customer:

    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}.; {self.phone}'


class Cart:

    MAX_LIMIT = 40

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__products = []
        self.__quantities = []

    def get_weight(self):
        return sum(self.__quantities)

    def add_product(self, product: Product, quantity: int | float = 1):
        if self.get_weight() + quantity <= Cart.MAX_LIMIT:
            self.__products.append(product)
            self.__quantities.append(quantity)

    def total(self):
        result = 0
        for product, quantity in zip(self.__products, self.__quantities):
            result += product.price * quantity

        return result

    def __str__(self):
        result = f'{self.customer}\n'
        result += '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
                      zip(self.__products, self.__quantities)))
        result += f'\nTotal: {self.total()} UAH'
        return result

try:
    x_1 = Product('banana', 0)
    x_2 = Product('apple', 25)
    x_3 = Product('orange', 35)
except NegativePriceError as error:
    print(error)

customer_1 = Customer('Ivanov', 'Ivan', '123456789')
customer_2 = Customer('Ivanov', 'Petro', '123456799')

order_1 = Cart(customer_1)
order_1.add_product(x_1)
order_1.add_product(x_2, 2)
order_1.add_product(x_3, 35)

print(order_1)


order_2 = Cart(customer_2)
order_2.add_product(x_2, 10)
print(order_2)

