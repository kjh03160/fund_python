from Class_Define import User_Table
from Crwal_Table import Crwal_Table
from html_making import HTML
import os
from sys import exit

def main():
    while True:
        year, semester = input('학기를 입력해주세요 (Ex 20-1 or 20-여름) : ').split('-')
        majors = input('1전공, 2전공을 입력해주세요 (띄어쓰기로 구분), 종료(q 입력) : ').split()
        if majors[0] == 'q':
            exit()
        grade = input('듣고 싶은 수업의 학년을 입력해주세요 (띄어쓰기로 구분) : ').split()
        course_evl = input('강의 평가를 추가하시겠습니까? (에브리타임 로그인 필요, y/n) : ')

        try:
            crawling = Crwal_Table()

            if len(majors) > 1:
                first_major, second_major = majors
            else:
                first_major = majors[0]
                second_major = None

            first_major_obj = crawling.make_timetable(first_major, year, semester)
            second_major_obj = crawling.make_timetable(second_major, year, semester)

            user1 = User_Table(False, grade, first_major, second_major)

            if course_evl == 'y':
                user1.course_evl = True
                crawling.get_avg_stars(first_major_obj, second_major_obj, grade)
            if crawling.browser:
                crawling.browser.close()

            user1.make_txt(first_major_obj, second_major_obj)

            user1.make_time_dict()

            html = HTML()
            html.make_result_html(user1)
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
        finally:
            os.system('cls')

if __name__ == "__main__":
    main()
    input()