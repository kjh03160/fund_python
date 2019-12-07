from Class_Define import User_Table
from Crwal_Table import Crwal_Table
from html_making import HTML
import os

while True:
    majors = input('1전공, 2전공을 입력해주세요 (띄어쓰기로 구분) : ').split()
    grade = input('듣고 싶은 수업의 학년을 입력해주세요 (띄어쓰기로 구분) : ').split()
    course_evl = input('강의 평가를 추가하시겠습니까? (에브리타임 로그인 필요, y/n) : ')

    try:
        crawling = Crwal_Table()

        if len(majors) > 1:
            first_major, second_major = majors
        else:
            first_major = majors[0]
            second_major = None

        first_major_obj = crawling.make_timetable(first_major)
        second_major_obj = crawling.make_timetable(second_major)

        user1 = User_Table(False, grade, first_major, second_major)

        if course_evl == 'y':
            user1.course_evl = True
            crawling.get_avg_stars(first_major_obj, second_major_obj, grade)

        credit = user1.make_txt(first_major_obj, second_major_obj)

        time_table_dict = user1.make_time_dict()

        # data = pd.DataFrame(time_table_dict, index = [i + 1 for i in range(12)])
        # data_html = data.to_html()
        # with open('temp.html', 'w', encoding='UTF-8') as file:
        #     file.write(data_html)

        html = HTML()
        # td_html = "\n".join(html.make_by_pandas(time_table_dict))
        html.make_result_html(time_table_dict, credit)
        html.make_list_html(user1)

        with open('Result.html', 'w', encoding='UTF-8') as file:
            file.write(html.main_head_html + html.main_body_html + html.main_bottom_html)

        with open('Course_List.html', 'w', encoding='UTF-8') as file:
            file.write(html.list_head_html + html.list_body_html +html.list_bottom_html)
        print('완료!')
        os.startfile('Result.html')
    except Exception as e:
        print(e)
        print('다시 시도해주세요')
        print()

input()