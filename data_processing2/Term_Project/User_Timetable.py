from Class_Define import Department, Class, User, User_Table, Stack
from Crwal_Table import Crwal_Table
import pandas as pd
from html_making import HTML
import os
def make_time_dict(dict, user):
    print('시간표 만드는 중입니다.')
    course_list = user.courses
    for i in course_list:
        s = Stack()
        time = i.class_time.split('(')[2].strip().split()
        for j in time:
            if not j.isdigit():
                if not s.isEmpty():
                    s.pop()
                s.push(j)
            else:
                # subject_information = {'name' :i.subject, 'syllabus' : i.syllabus, 'prof' : i.prof, 'stars' : i.stars }
                # dict[s.peek()][int(j) - 1].append(subject_information)
                dict[s.peek()][int(j) - 1].append('subject::' + i.subject + '::' + i.stars + '::' + i.syllabus + ',')
        while not s.isEmpty:
            s.pop()
    return dict


# first_major, second_major = input('1전공, 2전공을 입력해주세요 (띄어쓰기로 구분) : ').split()
first_major, second_major = ('ELLT학과 융복합소프트웨어전공').split()
# grade = input('듣고 싶은 수업의 학년을 입력해주세요 (띄어쓰기로 구분) : ').split()
# course_evl = input('강의 평가를 추가하시겠습니까? (에브리타임 로그인 필요, y/n) : ')
grade = str(2)
course_evl = 'y'
crawling = Crwal_Table()
first_major_obj = crawling.make_timetable(first_major)
second_major_obj = crawling.make_timetable(second_major)

user1 = User_Table(True, grade, first_major, second_major)

if course_evl == 'y':
    user1.course_evl = True
    crawling.get_avg_stars(first_major_obj, second_major_obj, grade)



user1.make_txt(first_major_obj, second_major_obj)


time_table_dict = {
    'Mon' : [[] for i in range(12)],
    'Tue' : [[] for i in range(12)],
    'Wed' : [[] for i in range(12)],
    'Thu' : [[] for i in range(12)],
    'Fri' : [[] for i in range(12)],
}

time_table_dict = make_time_dict(time_table_dict, user1)

data = pd.DataFrame(time_table_dict, index = [i + 1 for i in range(12)])
data_html = data.to_html()
with open('temp.html', 'w', encoding='UTF-8') as file:
    file.write(data_html)

html = HTML()
td_html = "\n".join(html.make(time_table_dict))

with open('Result.html', 'w', encoding='UTF-8') as file:
    file.write(html.head_html + html.main_html + td_html + html.bottom)
print('완료!')
os.startfile('Result.html')