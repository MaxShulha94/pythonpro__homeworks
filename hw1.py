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
        self.type = 'student'

    def info(self):
        return 'Student'


class Group:
    def __init__(self, specialize):
        self.specialize = specialize
        self.list_group = []

    def add_st(self, student):
        self.list_group.append(student)

    def plus_st(self, st_surname, st_name, st_age):
        self.list_group.append(self.plus_st)

    def del_st(self, st_surname, st_name, st):
        self.list_group.remove(self.del_st)

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
st_surname = input('Enter the surname of student: ')
st_name = input('Enter the name of student: ')
st_age = input('Enter the age of student: ')
gr.plus_st(st_surname, st_name, st_age)

print(gr)
