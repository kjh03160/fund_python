class HTML:
    def __init__(self):
        self.head_html ="""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400);
    @font-face { font-family: 'silgothic'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_eight@1.0/silgothic.woff') format('woff'); font-weight: normal; font-style: normal; }
    @font-face { font-family: 'DungGeunMo'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/DungGeunMo.woff') format('woff'); font-weight: normal; font-style: normal; }
    
    html,
    body,
    .background {
      height : 110%;
      margin: 0;
    }

    html {
      background: #fff;

    }

    body {
      padding: 10px;

      background: #eee;
      background: linear-gradient(0deg, rgba(0, 0, 200, 0.2), rgba(0, 0, 200, 0));

      -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
    }

    .background {
      /* width: 130%; */

    /* height: 120% !important; */
      background: #eee;
      background: linear-gradient(120deg, rgba(50, 150, 100, 0.2), rgba(0, 0, 100, 0));
    }

    *,
    *:before,
    *:after {
      margin: 0;
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
      margin-top: 10px;
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
  padding: 25px;
  border: 2px solid #fff;
  border-radius: 40px/50px;
  background-clip: padding-box;
  text-align: center;
  opacity: 50%;
  font-family: 'silgothic';
    font-size: 1em;
    color: black;
    font-weight: 1000;
    white-space: nowrap;
    }
  </style>
          <title>Time Table</title>
        </head>
        
        """


        self.main_html = """
        
        
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


        self.bottom = """    
       </table>
      <!-- </div> -->
      <div id='container'>
        <p>강의계획서 - 강의명 클릭!</p>
        <p>강의평 - 강의명에 마우스 올리기!</p>
        
      </div>
    </body>
    
    </html>
    """

    def make_result_html(self, user, dict):
        print('웹페이지 제작중...')
        tds_list = []
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
        time = 1
        while time < 4:
            html_list = []
            stars_list = []

            Mon = dict['Mon'][time - 1]
            Tue = dict['Tue'][time - 1]
            Wed = dict['Wed'][time - 1]
            Thu = dict['Thu'][time - 1]
            Fri = dict['Fri'][time - 1]
            def day_table(day):
                temp_stars = []
                insert_html = ""
                # print(day)
                for i in day:
                    sub = i['name'].split(' / ')[0]
                    prof = i['prof']
                    insert_html += '<a href=' + i['syllabus'] + '>' + sub + '<br>' + ' (' + prof + ')' +'</a>' + '<br><br>\n'
                    temp_stars.append(i['stars'])
                stars_list.append(" / ".join(temp_stars))
                html_list.append(insert_html[:-9] + '\n')
                return html_list

            day_table(Mon)
            day_table(Tue)
            day_table(Wed)
            day_table(Thu)
            day_table(Fri)
            print(html_list[3])
            for i in range(5):
                if len(stars_list[i]) == 0:
                    stars_list[i] = ''
                else:
                    stars_list[i] = 'data-tooltip=' + "'" + stars_list[i] + "'"
            # print(time)
            # print(html_list[3])
            td_html = td_html.format(time=str(time), Mon=html_list[0], Tue=html_list[1], Wed=html_list[2],
                                     Thu=html_list[3], Fri=html_list[4], stars1=stars_list[0],
                                     stars2=stars_list[1], stars3=stars_list[2], stars4=stars_list[3],
                                     stars5=stars_list[4])
            # print(html_list[0])
            # print()
            # print()
            # print(td_html)
            # print()
            tds_list.append(td_html)
            time += 1
            print(tds_list)

        return tds_list



    def make(self, dict):
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
                            print(i)
                            i = i.split('::')
                            print(i)
                            i = i[1:]
                            print(i)
                            if len(i) == 0:
                                continue
                            subject = i[0].split(' / ')
                            print(subject)
                            print(i[1])

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

