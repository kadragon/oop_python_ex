import datetime  # 날짜 관련 라이브러리

import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library

# 로그인이 필요한 사이트 파싱을 위한 정보 저장
LOGIN_INFO = {
    'id': 'USER_ID',
    'passwd': 'USER_PASSWORD'
}

# 오늘의 날씨는 구하가
now = datetime.date.today()
tmp_date = now + datetime.timedelta(days=-2)  # 2일 전 날짜를 구하기

min_date = "%s-%02d-%02d" % (str(tmp_date.year)[2:4], tmp_date.month, tmp_date.day)  # 2일전 기준으로 18-01-01 과 같은 형태 만들기

# 로그인을 유지하는건 session 이라는 기술 | 이를 활용하기 위해서 with 를 사용한다.
with requests.Session() as s:
    # 로그인 페이지를 가져와서 html 로 만들어 파싱을 시도한다.
    first_page = s.get('https://go.sasa.hs.kr')
    html = first_page.text
    soup = bs(html, 'html.parser')

    # cross-site request forgery 방지용 input value 를 가져온다.
    # https://ko.wikipedia.org/wiki/사이트_간_요청_위조
    csrf = soup.find('input', {'name': 'csrf_test_name'})

    # 두개의 dictionary 를 합친다.
    LOGIN_INFO.update({'csrf_test_name': csrf['value']})

    # 만들어진 로그인 데이터를 이용해서, 로그인을 시도한다.
    login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)

    # 로그인이 성공적으로 이루어졌는지 확인한다.
    if login_req.status_code != 200:
        raise Exception('로그인 되지 않았습니다!')

    # 접근 할 수 있는 모든 게시판을 검색 하기 위해서, 메인페이지에 접속한다.
    section_board_list_data = bs(s.get('https://go.sasa.hs.kr/main').text, 'html.parser')

    # 접속 후, <ul class='treeview-menu'> 안에 있는, <li> 안에 있는, <a> 를 모두 검색한다.
    board_list_data = section_board_list_data.select('ul.treeview-menu li a')

    # 접근 할 수 있는 모든 게시판의 목록을 저장하는 리스트
    auth_board_list = []

    for i in board_list_data:
        # ex) /board/lists/22/page/1
        # '/' 으로 분리하여 [1] 이 board 인 것이 게시판이기에 이 게시판만 저장한다.
        if 'board' == i.get('href').split('/')[1]:
            auth_board_list.append(i.get('href').split('/')[3])

    """
    검색한 board_id 기반으로 각 게시판을 개별적으로 방문하여, 최근 2일간의 게시물들을 모두 가져오는 과정
    """
    for board_id in auth_board_list:
        # 각 게시판에 접속하여 html tag 를 parsing 하기 좋게 bs4 를 적용한다.
        notice_board_data = bs(s.get('https://go.sasa.hs.kr/board/lists/' + board_id + '/page/1').text, 'html.parser')

        # ex) <h3 class="box-title">[18] 공지사항</h3>
        # 위와 같은 형태의 게시판 이름 추출 | <h3> tag 를 찾아, 그 안에 있는 text 를 추출한다.
        notice_board_title = notice_board_data.find('h3').getText()

        # 게시판의 한 줄을 의미하는 <tr> tag 를 모두 검색해 list 로 반환한다.
        notice_list = notice_board_data.select('tr')

        # 게시물의 한줄씩 가져와서 분석하기 시작
        for sub_tr in notice_list:
            # 제목줄을 무시하기 위한 코드 | 제목 줄에는 <td> 대신 <th> 사용된다는 것을 활용
            sub_tr_data = sub_tr.select('td')
            if len(sub_tr_data) == 0:
                continue

            notice_url = 'https://go.sasa.hs.kr/' + (sub_tr_data[1].find('a').get('href'))
            notice_title = sub_tr_data[1].select('span')[0].getText().strip()
            notice_date = sub_tr_data[4].getText().strip()[0:8]

            # 게시된지 2일 이하의 게시물을 필터링
            if notice_date >= min_date:
                print("%s | %s | %s | %s" % (notice_board_title, notice_date, notice_title, notice_url))
