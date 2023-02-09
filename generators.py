""" 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним
       множником. Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при
       передачі команди на завершення. """


def gen_progression(first_num, last_num, mult):
    while first_num < last_num:
        yield first_num
        first_num *= mult


for item in gen_progression(3, 1000, 4):
    print(item)

"""2. Реалізуйте свій аналог генераторної функції range()."""


def range_analog(start, stop, step):
    while start < stop:
        yield start
        start += step


for item in range_analog(0, 20, 2):
    print(item)

"""3. Напишіть функцію-генератор, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана параметром 
      цієї функції."""


def simple_num(n):
    for numb in range(2, n + 1):
        for i in range(2, numb):
            if numb % i == 0:
                break
            else:
                yield numb


for item in simple_num(20):
    print(item)

"""4. Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел від 2 до вказаної 
      вами величини."""


n = input('enter the number: ')
x = (i ** 3 for i in range(2, n))

print(list(x))
