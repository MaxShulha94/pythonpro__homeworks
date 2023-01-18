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
        self.finded_st = []

    def add_st(self, student):
        if len(self.list_group) <= 9:
            self.list_group.append(student)

    def plus_st(self):
        new_student = {'inform': input('Enter surname, name and age: ')}
        self.list_group.append(new_student.get('inform'))

    def del_st(self):
        del_student = input('Enter surname, name, age: ')
        if del_student in self.list_group:
            self.list_group.remove(del_student)

    def search_st(self):
        search_student = input('Enter surname, name, age: ')
        if search_student in self.list_group:
            self.finded_st.append(search_student)

    def __str__(self):
        return f'{self.specialize}:\n' + '\n'.join(map(str, self.list_group)) + {self.finded_st}


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
st11 = Student('Borko', 'Ivan', '35')

gr.add_st(st1)
gr.add_st(st2)
gr.add_st(st3)
gr.add_st(st4)
gr.add_st(st5)
gr.add_st(st6)
gr.add_st(st7)
gr.add_st(st8)
gr.add_st(st9)
# gr.add_st(st10)
# gr.add_st(st11)

# gr.plus_st()
#gr.del_st()
gr.search_st()
print(gr)
