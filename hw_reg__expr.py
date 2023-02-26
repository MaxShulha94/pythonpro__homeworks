import re

"""
Task 1
Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R,
за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр."""

# text = input('enter text: ')
# pattern = r'Rb+r'
# res = re.findall(pattern, text)
# print(res)

"""
Task 2
Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999)."""


# def validation(card_num):
#
#     pattern = r'^(9{4}-9{4}-9{4}-9{4})$'
#     res = re.findall(pattern, card_num)
#
#     if res:
#         print(True)
#     else:
#         print(False)
# validation(card_num = input('enter your card number: '))

"""
Task 3
Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
Вимоги:
-Цифри (0-9).
-лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
-у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
-Символ "-" не може повторюватися."""

# def valid_mail(text: str):
#     pattern = r'^[^_-]\[w\d]{0-9}\S+_\S-{1}'
#     result = re.search(pattern, text)
#     if result:
#         print(True)
#     else:
#         print(False)
# valid_mail(text=input('Enter your email: '))

"""
Task 4
Напишіть функцію, яка перевіряє правильність логіну. 
Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри."""

def checking_log(login):
    pattern = r'[A-Za-z0-9]{2-10}'
    result = re.findall(pattern, login)
    if result:
        print(True)
    else:
        print(False)
checking_log(login=input('Enter your login: '))