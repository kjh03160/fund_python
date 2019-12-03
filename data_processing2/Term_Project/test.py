head_html ="""
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400);

    .blue {
      background: #3498db;
    }

    .purple {
      background: #9b59b6;
    }

    .navy {
      background: #34495e;
    }

    .green {
      background: #2ecc71;
    }

    .red {
      background: #e74c3c;
    }

    .orange {
      background: #f39c12;
    }

    .cs335,
    .cs426,
    .md303,
    .md352,
    .md313,
    .cs240 {
      font-weight: 300;
      cursor: pointer;
    }

    body {
      background: #e74c3c;
      padding: 20px;
    }

    *,
    *:before,
    *:after {
      margin: 0;
      padding: 0;
      border: 0;
      outline: 0;
      -moz-box-sizing: border-box;
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
    }

    table {
      font-family: 'Open Sans', Helvetica;
      color: #efefef;
      /* direction:rtl; */
    }

    table tr:nth-child(2n) {
      background: #eff0f1;
    }

    table tr:nth-child(2n+3) {
      background: #fff;
    }

    table th,
    table td {
      padding: 1em;
      width: 10em;
    }

    .days,
    .time {
      background: #34495e;
      text-transform: uppercase;
      font-size: 0.6em;
      text-align: center;
    }

    .time {
      width: 3em !important;
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
  </style>
  <title>Time Table</title>
</head>

"""


main_html = """
<!DOCTYPE html>
<html lang="ko">

<body>
  <!-- <div class='tab'> -->
  <table border='0' cellpadding='0' cellspacing='0'>
    <tr class='days'>
      <th>#</th>

      <th>Mon</th>
      <th>Tue</th>
      <th>Wed</th>
      <th>Thu</th>
      <th>Fri</th>


    </tr>
    <tr>
      <td class='time'>1</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon1}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue1}</td>
      <td>{Wed1}</td>
      <td>{Thu1}</td>
      <td>{Fri1}</td>


    </tr>
    <tr>
      <td class='time'>2</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon2}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue2}</td>
      <td>{Wed2}</td>
      <td>{Thu2}</td>
      <td>{Fri2}</td>

    </tr>
    <tr>
      <td class='time'>3</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon3}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue3}</td>
      <td>{Wed3}</td>
      <td>{Thu3}</td>
      <td>{Fri3}</td>

    </tr>
    <tr>
      <td class='time'>4</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon4}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue4}</td>
      <td>{Wed4}</td>
      <td>{Thu4}</td>
      <td>{Fri4}</td>

    </tr>
    <tr>
      <td class='time'>5</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon5}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue5}</td>
      <td>{Wed5}</td>
      <td>{Thu5}</td>
      <td>{Fri5}</td>

    </tr>
    <tr>
      <td class='time'>6</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon6}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue6}</td>
      <td>{Wed6}</td>
      <td>{Thu6}</td>
      <td>{Fri6}</td>

    </tr>
    <tr>
      <td class='time'>7</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon7}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue7}</td>
      <td>{Wed7}</td>
      <td>{Thu7}</td>
      <td>{Fri7}</td>

    </tr>
    <tr>
      <td class='time'>8</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon8}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue8}</td>
      <td>{Wed8}</td>
      <td>{Thu8}</td>
      <td>{Fri8}</td>

    </tr>
    <tr>
      <td class='time'>9</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon9}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue9}</td>
      <td>{Wed9}</td>
      <td>{Thu9}</td>
      <td>{Fri9}</td>

    </tr>
    <tr>
      <td class='time'>10</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon10}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue10}</td>
      <td>{Wed10}</td>
      <td>{Thu10}</td>
      <td>{Fri10}</td>

    </tr>
    <tr>
      <td class='time'>11</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon11}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue1}</td>
      <td>{Wed11}</td>
      <td>{Thu11}</td>
      <td>{Fri11}</td>


    </tr>
    <tr>
      <td class='time'>12</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>{Mon12}</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>{Tue12}</td>
      <td>{Wed12}</td>
      <td>{Thu12}</td>
      <td>{Fri12}</td>

    </tr>
  </table>
  <!-- </div> -->
</body>

</html>
"""