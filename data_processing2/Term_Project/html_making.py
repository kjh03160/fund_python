from Quick_sort import quick_sort_by_stars, quick_sort_by_time

class HTML:
    def __init__(self):
        self.main_head_html ="""
        <!DOCTYPE html>
        <html lang="ko">
                <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">

          <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">



                                                <style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400);
    @font-face { font-family: 'silgothic'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_eight@1.0/silgothic.woff') format('woff'); font-weight: normal; font-style: normal; }
    @font-face { font-family: 'DungGeunMo'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/DungGeunMo.woff') format('woff'); font-weight: normal; font-style: normal; }
    @font-face { font-family: 'KCC-eunyoung'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/KCC-eunyoung-Regular.woff') format('woff'); font-weight: normal; font-style: normal; }

    body {
      padding: 10px;

      background: #eee;
      background: linear-gradient(0deg, rgba(0, 0, 200, 0.2), rgba(0, 0, 200, 0));
      background-attachment: fixed;	
	background-size: cover;
    }

    .background {
      background: #eee;
      background: linear-gradient(120deg, rgba(50, 150, 100, 0.2), rgba(0, 0, 100, 0));
    }

    *,
    *:before,
    *:after {
      margin-bottom: 10px;
      padding: 0;
      /* border: 0; */
      outline: 0;
      -moz-box-sizing: border-box;
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
    }

    table {
      width: 78% !important;
      font-family: 'Open Sans', Helvetica;
      color: #efefef;
      text-align: center;
      /* margin: auto; */
      padding: auto;
      /* margin-top: 10px; */
      /* margin-bottom: 10px; */
      position: relative;
      float: left;

    }

    a {
      color: #2f3b72;
      text-decoration: none
    }

    table tr:nth-child(2n) {
      background: #eff0f1;
    }

    table tr:nth-child(2n+3) {
      background: #fff;
    }

    td {
      color: #2f3b72;
      font-weight: 1000;

      font-family: 'DungGeunMo';
      font-size: 12px !important;
    }

    table th,
    table td {
      padding: 0.7em;
      width: 10em;
    }

    .days,
    .time {
      background: #34495e;
      text-transform: uppercase;
      font-size: 0.8em;
      text-align: center;
    }

    #left_side {
      width: 3em !important;
      background: #34495e;
      font-size: 0.6em;
      text-align: center;
    }

    /* Add this attribute to the element that needs a tooltip */
    [data-tooltip] {
      position: relative;
      z-index: 2;
      cursor: pointer;
    }

    /* Hide the tooltip content by default */
    [data-tooltip]:before,
    [data-tooltip]:after {
      visibility: hidden;
      filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=0);
      opacity: 0;
      pointer-events: none;
      -moz-transition: ease 0.5s all;
      -o-transition: ease 0.5s all;
      -webkit-transition: ease 0.5s all;
      transition: ease 0.5s all;
    }

    /* Position tooltip above the element */
    [data-tooltip]:before {
      position: absolute;
      bottom: 110%;
      left: 50%;
      margin-bottom: 5px;
      margin-left: -80px;
      padding: 7px;
      width: 160px;
      -moz-border-radius: 6px;
      -webkit-border-radius: 6px;
      border-radius: 6px;
      background-color: black;
      color: #fff;
      content: attr(data-tooltip);
      text-align: center;
      font-size: 14px;
      line-height: 1.2;
    }

    /* Triangle hack to make tooltip look like a speech bubble */
    [data-tooltip]:after {
      position: absolute;
      bottom: 110%;
      left: 50%;
      margin-left: -5px;
      width: 0;
      border-top: 5px solid black;
      border-right: 5px solid transparent;
      border-left: 5px solid transparent;
      content: " ";
      font-size: 0;
      line-height: 0;
    }

    /* Show tooltip content on hover */
    [data-tooltip]:hover:before,
    [data-tooltip]:hover:after {
      visibility: visible;
      bottom: 90%;
      filter: progid:DXImageTransform.Microsoft.Alpha(enabled=false);
      opacity: 1;
    }
    #container{
      position: relative;
      float: left;
      margin-left: 10px;
  width: 20%;
  background: rgba(0, 0, 200, 0.2);
  padding: 15px;
  border: 2px solid #fff;
  border-radius: 5px;
  background-clip: padding-box;
  text-align: center;
  font-family: 'silgothic';
    font-size: 1em;
    color: black;
    font-weight: 1000;
    white-space: nowrap;
    box-shadow: 0 15px 30px 1px rgba(128, 128, 128, 0.31);
    height: 120px;
    }
    #container1{
      position: relative;
      float: left;
      margin-left: 10px;
  width: 20%;
  /* background: rgba(0, 0, 200, 0.2); */
  padding: 15px;
  border: 2px solid #fff;
  border-radius: 5px;
  background-clip: padding-box;
  text-align: center;
  font-family: 'silgothic';
    font-size: 1em;
    color: black;
    font-weight: 1000;
    white-space: nowrap;
    box-shadow: 0 15px 30px 1px rgba(128, 128, 128, 0.31);
    height: 100px;
    }
    h2{
      margin-top: 0px;
    }
    p {
      margin-top: auto;
    }
    .explore{
      float:left;
      font-size: 20px;
      
      margin-top: 10px;
      margin-left: 30px;
      padding-top: 10px;
    }
    i  {
      float:right;
      font-size: 40px;
      margin: auto;
      padding: 10px;
    }
    .created{
      position: relative;
      float: left;
      display: table;
      vertical-align: middle;
      font-size: 20px;
      width: 320px;
      height: 150px;
      margin-top: 30px;
    }
    img{
      float: left;
      margin-left: 10px;
      /* position: relative; */
      border-radius: 10px;
      margin-right: 10px;
    }
    #made{
      float: left;
      display: table-cell;
      vertical-align: middle;
      text-align: center;;
      margin-top: 20px !important;
      margin-left: 30px;
      font-family: 'KCC-eunyoung';
      font-size: 1.5em;
      font-weight: 600;
    }
  </style>
          <title>Time Table</title>
        </head>
        """


        self.main_body_html = """
        
        
        <body>
          <!-- <div class='tab'> -->
          <table border='0' cellpadding='0' cellspacing='0'>
            <tr class='days'>
              <th id='left_side'>#</th>
        
              <th>Mon</th>
              <th>Tue</th>
              <th>Wed</th>
              <th>Thu</th>
              <th>Fri</th>
        
        
            </tr>
        """


        self.main_bottom_html = """    
       </table>
      <!-- </div> -->
 <div id='container'>
        <h2>총 <a href="Course_List.html"><U><b>{credit}</b>학점</a></U></h2>

        <p>강의계획서 - 강의명 클릭!</p>
        <p>강의평 - 강의명에 마우스 올리기!</p>
        
               
      </div>
      <div id='container1'>
        <div class='explore'>E x p l o r e !</div>
        <a href="https://www.instagram.com/juna_km/" target="_blank"><i class="fab fa-instagram"></i> </a>
        <a href="https://github.com/kjh03160" target="_blank"><i class="fab fa-github"></i></a>
        
      </div>
      <div class='created'>   <a href="https://likelion.net/" target="_blank"><img src="https://scontent-gmp1-1.xx.fbcdn.net/v/t1.0-9/53319997_2288407134771022_3834362680915787776_n.png?_ncat=103&_nc_ohc=PuEJDAR0sc0AQmKZ_9qb_PhpWTQPncx2wW-F3ePXw-AAqw0j5lX1Ww4dQ&_nc_ht=scontent-gmp1-1.xx&oh=89450d424bcb98be2bcc177b7e8cc2f7&oe=5E7CF0A6" width="140px" height="150px">
      </a><div id='made'>Made<br> by<br> juna_km</div>
        </div>
    </body>
    
    </html>
    """

        self.list_head_html = """
        
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Time List</title>




    <style>

html{
    height: 100%;
    overflow:hidden;
}
h1{
    margin-top:-10px;
  font-size: 30px;
  color: rgb(25, 83, 34);
  text-transform: uppercase;
  font-weight: 1000;
  text-align: center;
  margin-bottom: 15px;
}
table{
  width:100%;
  table-layout: fixed;
}
.tbl-header{
  background-color: rgba(231, 203, 247, 0.377);
 }
.tbl-content{
  height:500px;
  overflow-x:auto;
  margin-top: 0px;
  border: 1px solid rgba(121, 120, 120, 0.3);
}
th{
  padding: 20px 15px;
  text-align: center;
  font-weight: 500;
  font-size: 12px;
  font-weight: 1000;
  color: rgb(233, 87, 51);
  text-transform: uppercase;
}
td{
  padding: 15px;
  text-align: center;
  vertical-align:middle;
  font-weight: 300;
  font-size: 15px;
  color: rgba(32, 26, 25, 0.993);
  border-bottom: solid 1px rgba(128, 126, 126, 0.212);
  word-break: keep-all;
}
a {
      color: #c2306d;
      text-decoration: none
    }

/* demo styles */

@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);
body{

  background: linear-gradient(0deg, rgba(0, 0, 200, 0.2), rgba(0, 0, 200, 0));
  font-family: 'Roboto', sans-serif;
  background-attachment: fixed;	
	background-size: cover;
    height: 100%;
}
section{
  margin: 50px;
  height: 80%;
}


/* follow me template */
.made-with-love {
  margin-top: 30px;
  padding: 5px;
  /* clear: left; */
  text-align: center;
  font-size: 20px;
  font-family: arial;
  color: rgb(85, 66, 66);
position: relative;
left:-73px;
}
.made-with-love i {
  font-style: normal;
  color: rgb(168, 51, 92);
  font-size: 24px;
  position: relative;
  top: 0px;
}
.made-with-love a {
  color: rgb(53, 43, 43);
  text-decoration: none;
}
.made-with-love a:hover {
  text-decoration: underline;
}


/* for custom scrollbar for webkit browser*/

::-webkit-scrollbar {
    width: 6px;
} 
::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
} 
::-webkit-scrollbar-thumb {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
}

.buttons-con{
    z-index: 3;
  position: relative;
  float: left;
}

.buttons-con .action-link-wrap {
  margin-top: 8px;
  margin-left: 50px;
}
.buttons-con .action-link-wrap a {
  background: #c47ace;
  padding: 8px 25px;
  border-radius: 4px;
  color: #FFF;
  font-weight: bold;
  font-size: 14px;
  transition: all 0.3s linear;
  cursor: pointer;
  text-decoration: none;
  margin-right: 10px
}
.buttons-con .action-link-wrap a:hover {
  background: rgb(112, 17, 190);
  color: #fff;
}






</style>
</head>
<body>
        <section>
                <!--for demo wrap-->
                <h1>HUFS User Time Table</h1>
                <div class="tbl-header">
                  <table cellpadding="0" cellspacing="0" border="0">
                    <thead>
                      <tr>
                        <th width="30px">Area</th>
                        <th width="350px">Subject Name</th>
                        <th width="60px">전필</th>
                        <th width="60px">온라인</th>
                        <th width="60px">원어</th>
                        <th width="60px">팀티칭</th>
                        <th width="80px">담당교수</th>
                        <th width="30px">학점</th>
                        <th width="50px">강의시간</th>
                        <th width="50px">제한인원</th>
                        <th>비고</th>
                        <th width="50px">강의평가</th>

                      </tr>
                    </thead>
                  </table>
                </div>
                <div class="tbl-content">
                  <table cellpadding="0" cellspacing="0" border="0">
                    <tbody>
        """

        self.list_body_html = """
        
        """

        self.list_bottom_html = """
                            </tbody>
                  </table>
                </div>
              </section>
              <div class="buttons-con">
                  <div class="action-link-wrap">
                    <a href="Result.html" class="link-button link-back-button">Go Back</a>
                  </div>
                </div>
              <!-- follow me template -->
              <div class="made-with-love">
                Made 
                <i>★</i> by
                <a target="_blank" href="https://www.instagram.com/juna_km/">Junha Kim</a>
              </div>
</body>
</html>
        """

    def make_result_html(self, dict, credit):
        print('웹페이지 제작중...')
        time = 1
        while time < 13:
            td_html = '''
                    <tr>
                      <th id='left_side'>{time}</th>
                      <td {stars1}>{Mon}</td>
                      <td {stars2}>{Tue}</td>
                      <td {stars3}>{Wed}</td>
                      <td {stars4}>{Thu}</td>
                      <td {stars5}>{Fri}</td>
                    </tr>
                        '''
            html_list = []
            stars_list = []

            Mon = dict['Mon'][time - 1]
            Tue = dict['Tue'][time - 1]
            Wed = dict['Wed'][time - 1]
            Thu = dict['Thu'][time - 1]
            Fri = dict['Fri'][time - 1]
            def day_table(day, html_list):
                temp_stars = []
                insert_html = ""
                for i in day:
                    sub = i['sub'].split(' / ')[0]
                    syllabus = i['syllabus']
                    prof = i['prof']
                    stars = i['stars']
                    sub = sub + '<br>' + '(' + prof + ')'
                    insert_html += '<a href="' + syllabus + '" target="_blank">' + sub + '</a>' + '<br><br>\n'
                    temp_stars.append(stars)
                html_list.append(insert_html[:-9])
                stars_list.append(" / ".join(temp_stars))

            day_table(Mon, html_list)
            day_table(Tue, html_list)
            day_table(Wed, html_list)
            day_table(Thu, html_list)
            day_table(Fri, html_list)
            for i in range(5):
                if len(stars_list[i]) == 0:
                    stars_list[i] = ''
                else:
                    stars_list[i] = 'data-tooltip=' + "'" + stars_list[i] + "'"

            self.main_body_html += td_html.format(time=str(time), Mon=html_list[0], Tue=html_list[1], Wed=html_list[2],
                                     Thu=html_list[3], Fri=html_list[4], stars1=stars_list[0],
                                     stars2=stars_list[1], stars3=stars_list[2], stars4=stars_list[3],
                                     stars5=stars_list[4])

            time += 1
        self.main_bottom_html = self.main_bottom_html.format(credit=credit)



    def make_list_html(self, user):
        courses = user.courses
        if user.course_evl:
            quick_sort_by_stars(courses, 0, len(courses) - 1)
        else:
            quick_sort_by_time(courses, 0, len(courses) - 1)

        inserted_html = """
                              <tr>
                        <td width="30px">{area}</td>
                        <td width="350px">{subject}</td>
                        <td width="60px">{required}</td>
                        <td width="60px">{online}</td>
                        <td width="60px">{foreign}</td>
                        <td width="60px">{team_teaching}</td>
                        <td width="80px">{prof}</td>
                        <td width="30px">{credit}</td>
                        <td width="50px">{class_time}</td>
                        <td width="50px">{restrict_num}</td>
                        <td >{note}</td>
                        <td width="50px">{stars}</td>
                      </tr>
        """
        for i in courses:
            area = i.area
            name = i.subject.split(' / ')
            if len(name) > 1:
                name = name[0] + '<br>' + name[1]
            else:
                name = name[0]
            subject = '<a href="' + i.syllabus + '" target="_blank">' + name + '</a>'
            required = i.required
            online = i.online
            foreign = i.foreign
            team_teaching = i.team_teaching
            prof = i.prof
            credit = i.credit
            class_time = i.class_time
            restrict_num = i.restrict_num
            note = i.note
            stars = i.stars
            self.list_body_html += inserted_html.format(area = area, subject = subject, required = required, online = online,
                                                             foreign = foreign, team_teaching = team_teaching, prof = prof,
                                                             credit = credit, class_time = class_time, restrict_num = restrict_num,
                                                             note = note, stars = stars)


    def make_by_pandas(self, dict):
        tds_list = []
        # with open(user.first_major + '1.txt', 'r', encoding='UTF-8') as first:
        #     with open(user.second_major + '1.txt', 'r', encoding='UTF-8') as second:
        with open('temp.html', 'r', encoding='UTF-8') as file:
            a = file.readline()
            time = 1
            while a != "":
                a = file.readline()
                if '<td>' in a:
                    td_html = '''
                            <tr>
              <th id='left_side'>{time}</th>
              <td {stars1}>{Mon}</td>
              <td {stars2}>{Tue}</td>
              <td {stars3}>{Wed}</td>
              <td {stars4}>{Thu}</td>
              <td {stars5}>{Fri}</td>
            </tr>
            '''
                    k = 0
                    html_list = []
                    stars = []

                    def table_make(line):
                        print(line)
                        line = line.strip()[5:-7:1].split(',,')  # <td>[ , ]</td> 제거후 2 과목 이상 있으면 분리
                        insert_html = ""
                        if len(line) == 0:
                            html_list.append(insert_html)
                        temp_stars =[]
                        for i in line:
                            i = i.split('::')
                            i = i[1:]
                            if len(i) == 0:
                                continue
                            subject = i[0].split(' / ')

                            temp_stars.append(i[1])
                            if len(i) > 1:
                                insert_html += '<a href=' + i[2] + '>' + '<br>'.join(subject) +'</a>' + '<br><br>\n'
                            else:
                                insert_html += ('<a href=' + i[2] + '>' + subject[0] + '</a>' + '<br>' + '\n')
                        stars.append(' / '.join(temp_stars))
                        html_list.append(insert_html[:-9] + '\n')

                    for i in range(5):
                        table_make(a)
                        k += 1
                        a = file.readline()

                    for i in range(5):
                        if len(stars[i]) == 0:
                            stars[i] = ''
                        else:
                            stars[i] = 'data-tooltip=' + "'" + stars[i] + "'"
                    td_html = td_html.format(time = time, Mon = html_list[0], Tue = html_list[1], Wed = html_list[2],
                                             Thu = html_list[3], Fri = html_list[4], stars1 = stars[0],
                                             stars2 = stars[1], stars3 = stars[2], stars4 = stars[3],
                                             stars5 = stars[4])
                    tds_list.append(td_html)
                    time += 1

        return tds_list

