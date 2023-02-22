"""3. Для класу Box напишіть статичний метод, який підраховуватиме сумарний обсяг двох ящиків, які
      будуть його параметрами."""


class Box:

    @staticmethod
    def vol(box_1, box_2):
        return f'Sum volume = {box_1 + box_2}'


Box.vol(5, 5)

"""4. Створіть дескриптор, який робитиме поля доступними лише для читання."""


class Descriptor:

    def __get__(self, instance, owner):
        return self.some_inst

    def __set__(self, instance, value):
        raise AttributeError('Can not set')

    def __del__(self):
        raise AttributeError('Can not delete')



"""5. Реалізуйте функціонал, який заборонятиме встановлення полів класу будь-якими значеннями, крім цілих чисел."""


class Num:


    def __init__(self, var: int | float):
        self.var = var


    def __get__(self, instance, owner):
        if isinstance(instance, int | float):
            return instance.__dict__[self._var]
        else:
            raise TypeError('instance must be int')


    def __set__(self, instance, value):
        if isinstance(instance, int | float):
            instance.__dict__[self._var] = value
        raise TypeError('instance must be int')




num_1 = Num('1')

print(num_1.var)
