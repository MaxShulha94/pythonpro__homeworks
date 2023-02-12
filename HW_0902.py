"""4. Створіть декоратор із параметрами для проведення хронометражу роботи тієї чи іншої функції.
   Параметрами повинні виступати те, скільки разів потрібно запустити функцію, що декорується,
   і в який файл зберегти результати хронометражу."""
# import time
#
#
# class Time_decor:
#
#     def __init__(self, func):
#         self.func = func
#         self.start = 0
#         self.stop = 0
#
#     def __call__(self, *args, **kwargs):
#         with open('time_file.txt', 'w') as time_file:
#             self.start = time.time()
#             res = self.func(*args, **kwargs)
#             self.end = time.time()
#             time_file.write(f'Start = {self.start}\n')
#             time_file.write(f'End = {self.end}\n')
#
#             return res
#
#
# @Time_decor
# def factorial_num(num=1000):
#     tmp = 1
#     while num > 1:
#         tmp *= num
#         num -= 1
#     return int(tmp)
#
#
# exempl = factorial_num
#
# print(exempl())
# print(exempl.start)
# print(exempl.end)
