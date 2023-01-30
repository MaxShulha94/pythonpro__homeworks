import math
from math import gcd


class Fraction:

    def __init__(self, numerator: int, denumerator: int):
        if not isinstance(numerator, int):
            raise TypeError('Numerator must be int number.')
        if not isinstance(denumerator, int):
            raise TypeError('Denominator must be int number.')
        if denumerator == 0:
            raise ZeroDivisionError()

        self.numerator = numerator
        self.denumerator = denumerator

    def __gt__(self, other):
        tmp = math.gcd(self.numerator, self.denumerator)
        self.numerator //= tmp
        self.denumerator //= tmp

        tmp = math.gcd(other.numerator, other.denumerator)
        other.numerator //= tmp
        other.denumerator //= tmp

        return (self.numerator, self.denumerator) > (other.numerator, other.denumerator)

    def __ge__(self, other):
        tmp = math.gcd(self.numerator, self.denumerator)
        self.numerator //= tmp
        self.denumerator //= tmp

        tmp = math.gcd(other.numerator, other.denumerator)
        other.numerator //= tmp
        other.denumerator //= tmp

        return (self.numerator, self.denumerator) >= (other.numerator, other.denumerator)

    def __lt__(self, other):
        tmp = math.gcd(self.numerator, self.denumerator)
        self.numerator //= tmp
        self.denumerator //= tmp

        tmp = math.gcd(other.numerator, other.denumerator)
        other.numerator //= tmp
        other.denumerator //= tmp

        return (self.numerator, self.denumerator) < (other.numerator, other.denumerator)

    def __le__(self, other):
        tmp = math.gcd(self.numerator, self.denumerator)
        self.numerator //= tmp
        self.denumerator //= tmp

        tmp = math.gcd(other.numerator, other.denumerator)
        other.numerator //= tmp
        other.denumerator //= tmp

        return (self.numerator, self.denumerator) <= (other.numerator, other.denumerator)

    def __eq__(self, other):
        tmp = math.gcd(self.numerator, self.denumerator)
        self.numerator //= tmp
        self.denumerator //= tmp

        tmp = math.gcd(other.numerator, other.denumerator)
        other.numerator //= tmp
        other.denumerator //= tmp

        return (self.numerator, self.denumerator) == (other.numerator, other.denumerator)

    def __ne__(self, other):
        tmp = math.gcd(self.numerator, self.denumerator)
        self.numerator //= tmp
        self.denumerator //= tmp

        tmp = math.gcd(other.numerator, other.denumerator)
        other.numerator //= tmp
        other.denumerator //= tmp

        return (self.numerator, self.denumerator) != (other.numerator, other.denumerator)

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

a = Fraction(1, 4)
b = Fraction(2, 20)

