import logging

logger = logging.getLogger('Add_student')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class LimitError(Exception):
    def __int__(self, message):
        self.message = message


class Human:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def info(self):
        return 'Human'

    def __str__(self):
        return f'{self.surname}, {self.name}, {self.age}'


class Student(Human):
    def __int__(self, surname, name, age):
        super().__init__(surname, name, age)

    def info(self):
        return 'Student'


class Group:
    def __init__(self, specialize, limit_st=10):
        self.specialize = specialize
        self.limit_st = limit_st
        self.list_group = []

    def add_st(self, student: Student):
        if len(self.list_group) > 9:
            raise LimitError('You can not add more than 10 students!')
        if student not in self.list_group:
            logger.debug(f'Student {student} was added')
            self.list_group.append(student)

    def del_st(self, student: Student):
        if student in self.list_group:
            self.list_group.remove(student)

    def search_st(self, surname: str):
        res = []
        for i in self.list_group:
            if i.surname == surname:
                res.append(i)
        return res

    def __str__(self):
        return f'{self.specialize}:\n' + '\n'.join(map(str, self.list_group))


gr = Group('Python-pro')

st1 = Student('Kuzmenko', 'Ivan', '19')
st2 = Student('Tkachenko', 'Ivan', '29')
st3 = Student('Levchenko', 'Ivan', '39')
st4 = Student('Shevchenko', 'Ivan', '88')
st5 = Student('Kravchenko', 'Ivan', '18')
st6 = Student('Serhienko', 'Ivan', '28')
st7 = Student('Petrenko', 'Ivan', '48')
st8 = Student('Maksymenko', 'Ivan', '23')
st9 = Student('Ivanenko', 'Ivan', '17')
st10 = Student('Borysenko', 'Ivan', '35')
st11 = Student('Brovko', 'Ivan', '35')
st12 = Student('Rudnko', 'Ivan', '55')

try:
    gr.add_st(st1)
    gr.add_st(st2)
    gr.add_st(st3)
    gr.add_st(st4)
    gr.add_st(st5)
    gr.add_st(st6)
    gr.add_st(st7)
    gr.add_st(st8)
    gr.add_st(st9)
    gr.add_st(st10)
    gr.add_st(st11)
    gr.add_st(st12)
except LimitError as error:
    print(error)

print(gr)
# surname = input('Enter surname: ')
# a = gr.search_st(surname)
# print('*'.join(map(str, a)))
