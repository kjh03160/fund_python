class Student:
    def __init__(self, name, univ, dept, grade):
        self.name = name
        self.univ = univ
        self.dept= dept
        self.grade = grade

    def __call__(self):
        print("이름 : %s/학교 : %s/학과 : %s, 학년 : %s" % (self.name, self.univ, self.dept, self.grade))


with open('input.txt', 'r', encoding='utf-8') as file:
    a = file.readlines()
    student = []

    for i in a:
        temp = (i.strip().split(','))
        st1 = Student(temp[0], temp[1], temp[2], temp[3])
        student.append(st1)

    for i in student:
        i()
