from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

from Class_Define import Department, Class, User

class Crwal_Table:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/61.0.3163.100 Safari/537.36")

        self.browser = webdriver.Chrome('chromedriver.exe', options=self.options)

        self.dept_list = []
        self.dept_eles = None

    def lecture_home(self):
        self.browser.get("https://wis.hufs.ac.kr/src08/jsp/lecture/LECTURE2020L.jsp")

        dept_eles = self.browser.find_element_by_name('ag_crs_strct_cd')

        if len(self.dept_list) == 0:
            for i in dept_eles.find_elements_by_tag_name('option'):
                self.dept_list.append(i.text.strip()[6:].split('(')[0].strip())

        self.dept_eles = Select(dept_eles)

        return self.dept_eles

    def make_timetable(self, major):
        print(major, '데이터 수집 중')
        try:
            with open(major + '_all.txt', 'r', encoding="UTF-8") as file:
                class_list = file.readlines()
                depart = Department(major)
                for i in class_list:
                    i = i.split(" # ")
                    area, year, subject, syllabus, required, online, foreign, team_teaching, prof, credit, class_time, restrict_num, note, stars = i
                    depart.insert_class(Class(area, year, subject, syllabus, required, online, foreign,
                                              team_teaching, prof, credit, class_time, restrict_num, note, stars))
            print("데이터 수집 완료")

            return depart
        except:

            dept_eles = self.lecture_home()
            major_index = self.dept_list.index(major)
            depart = Department(major)
            dept_eles.select_by_index(major_index)

            time.sleep(0.5)
            html = bs(self.browser.page_source, 'html.parser')

            tbody = html.findAll('tbody')
            trs = tbody[-1].findAll('tr')[1:]

            for i in trs:
                tds = i.findAll('td')
                area = tds[1].get_text().strip()
                year = tds[2].get_text().strip()
                subject = tds[4].get_text().strip().splitlines()
                subject = " / ".join(subject)
                try:
                    syllabus = tds[5].find('a').get('href').split('\'')
                    ag_1 = syllabus[1]
                    ag_2 = syllabus[3]
                    ag_3 = syllabus[5]
                    ag_4 = syllabus[7]
                    syllabus = "https://wis.hufs.ac.kr/src08/jsp/lecture/syllabus.jsp?mode=print&ledg_year=" \
                               +str(ag_1)+"&ledg_sessn="+str(ag_2)+"&org_sect="+str(ag_3)+"&lssn_cd="+str(ag_4)
                except:
                    syllabus = 'None'

                required = tds[6]
                if required.find('img'):
                    required = '필수'
                else:
                    required = required.get_text()

                online = tds[7]
                if online.find('img'):
                    online = '온라인'
                else:
                    online = online.get_text()

                foreign = tds[8]
                if foreign.find('img'):
                    foreign = '원어'
                else:
                    foreign = foreign.get_text()

                team_teaching = tds[10]
                if team_teaching.find('img'):
                    team_teaching = '팀티칭'
                else:
                    team_teaching = team_teaching.get_text()

                prof = tds[11].get_text().strip().split('(')[0].strip()
                credit = tds[12].get_text().strip()
                class_time = tds[14].get_text().strip()
                restrict_num = tds[15].get_text().strip()
                note = tds[16].get_text().strip()

                if len(note) == 0:
                    depart.insert_class(Class(area, year, subject, syllabus, required, online, foreign,
                                              team_teaching, prof, credit, class_time, restrict_num))
                else:
                    depart.insert_class(Class(area, year, subject, syllabus, required, online, foreign,
                                              team_teaching, prof, credit, class_time, restrict_num, note))

            self.all_courses(depart)
        print("데이터 수집 완료")
        return depart


    def get_avg_stars(self, dept_obj1, dept_obj2, grade):
        browser = self.browser
        browser.get("https://everytime.kr/lecture")
        try:
            print('로그인 시도')
            id = browser.find_element_by_name("userid")
            id_input = input('아이디 입력 : ')
            id.send_keys(id_input)

            pw = browser.find_element_by_name("password")
            pw_input = input('비밀번호 입력 : ')
            pw.send_keys(pw_input)

            login = browser.find_element_by_class_name('submit')
            login.click()
            print('에브리타임 로그인 성공')
        except:
            print('로그인 실패')
            return

        fst_class_list = dept_obj1.classes
        scd_class_list = dept_obj2.classes

        def course_insert(class_list):
            for course in class_list:
                if course.year not in grade:
                    continue
                else:
                    if (dept_obj1.classes == class_list and '이중' in course.area) \
                            or (dept_obj2.classes == class_list and '1전공자 전용' in course.note):
                        continue

                while True:
                    try:
                        input_box = browser.find_element_by_name('keyword')
                        submit_btn = browser.find_element_by_class_name('submit')
                        input_box.send_keys(' ')
                        input_box.send_keys(course.subject.split(' / ')[0])
                        browser.execute_script("arguments[0].click();", submit_btn)
                        time.sleep(0.5)
                        profs= browser.find_element_by_xpath("//*[contains(text(), '" + course.prof + "')]")

                        browser.execute_script("arguments[0].click();", profs)
                        time.sleep(0.5)
                        stars = browser.find_element_by_class_name('value').text
                        if stars == '0':
                            stars = '없음'
                        course.stars = stars
                        browser.back()
                        browser.back()

                        break

                    except:
                        pass
                    try:
                        popup = browser.find_element_by_class_name('close')
                        browser.execute_script("arguments[0].click();", popup)
                    except:
                        continue
        print('강의평 가져오는중...')
        course_insert(fst_class_list)
        print('1전공 완료')
        course_insert(scd_class_list)
        print('2전공 완료')
        browser.close()


    def all_courses(self, dept_obj):
        with open(dept_obj.name + '_all.txt', 'w', encoding="UTF-8") as file:
            for course in dept_obj.classes:
                file.write(" # ".join(course()) + "\n")