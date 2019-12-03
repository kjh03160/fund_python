from Class_Define import Department, Class, User, User_Table, Stack
from Crwal_Table import Crwal_Table
import pandas as pd

# first_major, second_major = input('1전공, 2전공을 입력해주세요 (띄어쓰기로 구분) : ').split()
# grade = input('듣고 싶은 수업의 학년을 입력해주세요 (띄어쓰기로 구분) : ')
first_major =  'ELLT학과'
second_major ='융복합소프트웨어전공'
grade = '2 3'.split()
# course_evl = input('강의 평가를 추가하시겠습니까? (에브리타임 로그인 필요, y/n) : ')
course_evl = 'y'

crawling = Crwal_Table()
first_major_obj = crawling.make_timetable(first_major)
second_major_obj = crawling.make_timetable(second_major)

if course_evl == 'y':
    crawling.get_avg_stars(first_major_obj, second_major_obj, grade)

user1 = User_Table(grade, first_major, second_major)

user1.make_txt(first_major_obj, second_major_obj)

crawling.browser.close()

time_table_dict = {
    'Mon' : [[] for i in range(12)],
    'Tue' : [[] for i in range(12)],
    'Wed' : [[] for i in range(12)],
    'Thu' : [[] for i in range(12)],
    'Fri' : [[] for i in range(12)],
}

course_list = user1.courses
for i in course_list:
    s = Stack()
    time = i.class_time.split('(')[2].strip().split()
    digit_list = []
    for j in time:
        if j.isalpha():
            if not s.isEmpty():
                s.pop()
            s.push(j)
        else:
            time_table_dict[s.peek()][int(j) - 1].append(i.subject + '\n')
    while not s.isEmpty:
        s.pop()



data = pd.DataFrame(time_table_dict, index = [i + 1 for i in range(12)])
# data_styler = data.style
# data_styler.set_table_styles(
#     [dict(selector="table", props=[("text-align", "center")])]
# )
# data_html = data.style.set_properties({'text-align': 'right'}).render()
data_html = data.to_html()
with open('1.txt', 'w', encoding='UTF-8') as file:
    file.write(data_html)
with open('1.html', 'w', encoding='UTF-8') as file:
    file.write(data_html)