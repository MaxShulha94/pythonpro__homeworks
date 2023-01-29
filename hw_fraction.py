import math
from math import gcd


class Fraction:

    def __init__(self, numerator: int, denumerator: int):
        self.numerator = numerator
        self.denumerator = denumerator

    def __gt__(self, other):
        return Fraction(self.numerator > other.numerator, self.denumerator > other.denumerator)

    def __ge__(self, other):
        return Fraction(self.numerator >= other.numerator, self.denumerator >= other.denumerator)

    def __lt__(self, other):
        return Fraction(self.numerator < other.numerator, self.denumerator < other.denumerator)

    def __le__(self, other):
        return Fraction(self.numerator <= other.numerator, self.denumerator <= other.denumerator)

    def __eq__(self, other):
        return Fraction(self.numerator == other.numerator, self.denumerator == other.denumerator)

    def __ne__(self, other):
        return Fraction(self.numerator != other.numerator, self.denumerator != other.denumerator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denumerator * other.denumerator)

    def __add__(self, other):
        return Fraction((self.numerator * other.denumerator) + (other.numerator * self.denumerator),
                        (self.denumerator * other.denumerator))

    def __sub__(self, other):
        return Fraction((self.numerator * other.denumerator) - (other.numerator * self.denumerator),
                        (self.denumerator * other.denumerator))

    def __floordiv__(self, other):
        return Fraction(self.numerator * other.denumerator, self.denumerator * other.numerator)

    def __str__(self):
        if self.numerator == self.denumerator:
            return f'1'
        if self.numerator < self.denumerator:
            return f'{self.numerator // gcd(self.numerator, self.denumerator)}/{self.denumerator // gcd(self.numerator, self.denumerator)}'
        if self.numerator > self.denumerator:
            self.numerator = self.numerator // gcd(self.numerator, self.denumerator)
            self.denumerator = self.denumerator // gcd(self.numerator, self.denumerator)
            intgr = self.numerator // self.denumerator
            new_numerator = self.numerator - (intgr * self.denumerator)
            return f'{intgr} {new_numerator}/{self.denumerator}'

a = Fraction(1, 6)
b = Fraction(9, 5)

