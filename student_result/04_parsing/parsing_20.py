# pip install -U requests
# pip3 install -U beautifulsoup4

import datetime  # 날짜 관련 라이브러리

import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library

# 로그인이 필요한 사이트 파싱을 위한 정보 저장
LOGIN_INFO = {
    'id': '아이디 입력',
    'passwd': '암호 입력'
}

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

    # 음악을 올린 시간
    section_board_list_data = bs(s.get('https://go.sasa.hs.kr/RcmndMusic/musicView').text, 'html.parser')
    notice_board_data = bs(s.get('https://go.sasa.hs.kr/RcmndMusic/musicView').text, 'html.parser')

    # 이름 추출
    notice_board_title = notice_board_data.find('td').getText()

    # 한 줄을 의미하는 <tr> tag 를 모두 검색해 list 로 반환한다.
    notice_list = notice_board_data.select('tr')
    del notice_list[0] # 인덱스 제거
        # 게시물의 한줄씩 가져와서 분석하기 시작

    breakrule=dict()

    #print('-----------------all list------------------') # 임시 출력(전체 리스트)
    for sub_tr in notice_list:
        sub_tr_data = sub_tr.select('td')
        if len(sub_tr_data) == 0:
            continue
        #분석
        name = sub_tr_data[4].getText().strip()[0:8] # 이름 받아오기
        time = sub_tr_data[5].getText().strip()[0:8] #
        # print("이름 : %s || 등록 시간 : %s" % (name[3:8],time)) # 임시 출력(전체 리스트)
        if int(time[0:2])<4:
            breakrule.setdefault(name,time[0:5])

    breakrule=list(breakrule.items())
    print("------------12시 ~ 4시 업로더-------------")
    for i in breakrule:
        print("이름 : %s || 등록 시간 : %s시 %s분" % (i[0], i[1][0:2], i[1][3:5]))
