class Department:
    def __init__(self, name):
        self.name = name
        self.classes = []

    def __str__(self):
        return self.name

    def insert_class(self, class_obj):
        self.classes.append(class_obj)


class Class:
    def __init__(self, area, year, subject, syllabus, required, online, foreign, team_teaching, prof,
                 credit, class_time, restrict_num, note = '-', avg_stars = ' - '):
        self.area = area
        self.year = year
        self.subject = subject
        self.syllabus = syllabus
        self.required = required
        self.online = online
        self.foreign = foreign
        self.team_teaching = team_teaching
        self.prof = prof
        self.credit = credit
        self.class_time = class_time
        self.restrict_num = restrict_num
        self.stars = avg_stars
        self.note = note

    def __str__(self):
        return self.subject

    def __call__(self):
        return (self.area, self.year, self.subject, self.syllabus, self.required, self.online, self.foreign,
                self.team_teaching, self.prof, self.credit, self.class_time, self.restrict_num, self.note, self.stars)


class User:
    def __init__(self, course_evl, grade, first_major, second_major = None):
        self.first_major = first_major
        self.second_major = second_major
        self.grade = grade
        self.courses = []
        self.course_evl = course_evl



class User_Table(User):
    def __init__(self, course_evl, grade, first_major, second_major = None):
        self.credits = 0

        self.time_table = {
                'Mon' : [[] for i in range(13)],
                'Tue' : [[] for i in range(13)],
                'Wed' : [[] for i in range(13)],
                'Thu' : [[] for i in range(13)],
                'Fri' : [[] for i in range(13)],
            }
        super().__init__(course_evl, grade, first_major, second_major)

    def insert_course(self, course_obj):
        self.courses.append(course_obj)
        self.credits += int(course_obj.credit)

    def make_txt(self, fst_obj, sec_obj):
        first_major_obj = fst_obj
        with open(first_major_obj.name + '_classified.txt', 'w', encoding="UTF-8") as file:
            for course in first_major_obj.classes:
                if (self.course_evl == True and ' - ' in course.stars) or not course.year in self.grade or '이중' in course.area:
                    continue
                file.write(" # ".join(course()) + '\n')
                self.insert_course(course)
        print('1전공 조건 추출 완료')

        if sec_obj:
            second_major_obj = sec_obj
            with open(second_major_obj.name + '_classified.txt', 'w', encoding="UTF-8") as file:
                for course in second_major_obj.classes:
                    if (self.course_evl == True and ' - ' in course.stars) or not course.year in self.grade or '1전공자 전용' in course.note:
                        continue
                    file.write(" # ".join(course()) + '\n')
                    self.insert_course(course)
            print('2전공 조건 추출 완료')


        return self.credits

    def make_time_dict(self):
        print('시간표 만드는 중입니다.')
        course_list = self.courses
        for i in course_list:
            s = Stack()
            if len(i.class_time) > 3:
                time = i.class_time.split('(')[2].strip().split()
            else:
                continue
            for j in time:
                if not j.isdigit():
                    if not s.isEmpty():
                        s.pop()
                    s.push(j)
                else:
                    subject_information = {'sub': i.subject, 'syllabus': i.syllabus, 'prof': i.prof, 'stars': i.stars, 'credit' :  i.credit}
                    self.time_table[s.peek()][int(j) - 1].append(subject_information)
                    # dict[s.peek()][int(j) - 1].append('subject::' + i.subject + '::' + i.stars + '::' + i.syllabus + ',')
            while not s.isEmpty:
                s.pop()
        return self.time_table

class Stack:
    def __init__(self):
        self.item = []
        self.size = 0

    def push(self, value):
        self.item.append(value)
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.item.pop()
        return print("Stack is Empty")

    def peek(self):
        if self.size != 0:
            return self.item[-1]
        return print("Stack is Empty")

    def __len__(self):
        return len(self.item)

    def isEmpty(self):
        return self.__len__() == 0