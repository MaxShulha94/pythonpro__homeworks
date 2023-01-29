class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __square(self):
        return self.height * self.width

    def __add__(self, other):
        return self.__square() + other.__square()

    def mul_n(self, n):
        return self.__square() * n

    def __eq__(self, other):
        return self.__square() == other.__sqare()

    def __ne__(self, other):
        return self.__square() != other.__sqare

    def __lt__(self, other):
        return self.__square() < other.__sqare()

    def __le__(self, other):
        return self.__square() <= other.__sqare()

    def __gt__(self, other):
        return self.__square() > other.__sqare()

    def __ge__(self, other):
        return self.__square() >= other.__sqare

    def __str__(self):
        return f'{self.width} * {self.height} = {self.__square()}'

a = Rectangle(5, 5)
b = Rectangle(4, 4)
