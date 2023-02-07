# class Customer:
#
#     def __init__(self, surname, name, phone):
#         self.surname = surname
#         self.name = name
#         self.phone = phone
#
#     def __str__(self):
#         return f'{self.surname} {self.name[0]}.; {self.phone}'
#
#
# class Pizza:
#
#     def __init__(self):
#         self.pizza_dict = {'Monday': 'Cheese Pizza', 'Tuesday': 'Pepperoni Pizza', 'Wednesday': 'Meat Pizza',
#                            'Thursday': 'Margherita Pizza', 'Friday': 'Hawaiian Pizza', 'Saturday': 'The Works Pizza',
#                            'Sunday': 'Sicilian Pizza'}
#         self.price_dict = {'Monday': 100, 'Tuesday': 95, 'Wednesday': 110, 'Thursday': 90, 'Friday': 95, 'Saturday': 90,
#                            'Sunday': 100}
#         self.today = input('What day is it today?')
#         self.pizza_of_the_day = self.pizza_dict[self.today]
#         self.price_of_pizza = self.price_dict[self.today]
#
#     def __str__(self):
#         return f'{self.pizza_of_the_day}: {self.price_of_pizza} UAH'
#
#
# class Order:
#
#     def __init__(self, customer: Customer):
#
#         self.customer = customer
#         self.orders = []
#         self.__quantities = []
#
#     def add_product(self, pizza: Pizza, quantity: int | float = 1):
#         self.orders.append(pizza)
#         self.__quantities.append(quantity)
#
#     def total(self):
#         result = 0
#         for pizza, quantity in zip(self.orders, self.__quantities):
#             result += self.price_of_pizza * quantity
#
#         return result
#
#     def __str__(self):
#         result = f'{self.customer}\n'
#         result += '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price_of_pizza * item[1]} UAH',
#                                 zip(self.orders, self.__quantities)))
#         result += f'\nTotal: {self.total()} UAH'
#         return result
#
#
# human = Customer('Ivan', 'Sirko', 10)
# p = Pizza()
# x = Order(human)
# x.add_product(p, 3)
# print(x)


def fib():
    prev, curr = 0, 1

    def get_next():
        nonlocal prev, curr
        prev, curr = curr, prev + curr
        return curr
    return get_next

x = fib()
while True:
    print(x())