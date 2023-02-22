"""3. Для класу Box напишіть статичний метод, який підраховуватиме сумарний обсяг двох ящиків, які
      будуть його параметрами."""


class Box:

    @staticmethod
    def vol(box_1, box_2):
        print(f'Sum volume = {box_1 + box_2}')


Box.vol(5, 5)

"""4. Створіть дескриптор, який робитиме поля доступними лише для читання."""


class Descriptor:

    def __init__(self, some_inst):
        self.some_inst = some_inst

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

    var = property()

    @var.getter
    def var(self):
        if isinstance(self.var, int | float):
            return self.var
        raise TypeError('instance must be int')

    @var.setter
    def var(self, new_var):
        if isinstance(new_var, int | float):
            self.var = new_var
        raise TypeError('instance must be int')

    @var.deleter
    def var(self):
        del self.var


num_1 = Num(123)

print(num_1.var)
