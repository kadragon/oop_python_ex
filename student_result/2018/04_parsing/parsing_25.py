from bs4 import BeautifulSoup as bs
import requests
import datetime
"""
Project     과제3|Web Site Parsing
Auth        2513 지명금
Date        2018.10.28
"""
# pip install beautifulsoup4
# pip install requests

import datetime  # 날짜 관련 라이브러리

import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # 웹파싱 관련 라이브러리 및 함수

# 달빛학사 : http://go.sasa.hs.kr/

# 해당하는 사이트의 로그인을 위한 정보
LOGIN_INFO = {
    'id': 'USER_ID',
    'passwd': 'USER_PASSWORD'
}

"""
Project     과제3|Web Site Parsing
Auth        2513 지명금
Date        2018.10.28
"""
# pip install beautifulsoup4
# pip install requests


# 로그인을 위해 필요한 정보 id, password
LOGIN_INFO = {
    'id': 'ID',
    'passwd': 'PASSWD'
}


def get_DayNum():
    """
    며칠전까지의 데이터를 보고싶은지를 사용자가 입력하는 함수
    :return day_num: 데이터를 볼 기한을 담은 변수
    """
    day_num = int(input('>> 며칠 전까지의 게시물을 확인하시겠습니까? '))  # 며칠 전까지의 데이터를 받고싶은지 입력
    return day_num


def get_Category():
    """
    사용자가 보고 싶은 카테고리를 받는 함수
    :return notice: 일반 공지 = 22 or 교과 공지 = 23 or 대회 및 캠프 = 16 or 분실물 = 2
    """
    print("="*11 + " 달빛학사 응용 프로그램 " + "="*11)  # 프로그램의 이름 출력
    print("일반 공지 | 교과 공지 | 대회 및 캠프 | 분실물")  # 검색 가능한 카테고리

    notice = -1
    while notice == -1:
        notice = input(">> 어떤 공지를 확인하시겠습니까? ")
        if notice == "일반 공지":  # 달빛학사에서 일반 공지의 번호 22
            notice = 22  # example : go.sasa.hs.kr/board/lists/22/
        elif notice == "교과 공지":  # 달빛학사에서 교과 공지의 번호 23
            notice = 23
        elif notice == "대회 및 캠프":  # 달빛학사에서 대회 및 캠프의 번호 16
            notice = 16
        elif notice == "분실물":  # 달빛학사에서 분실물의 번호 2
            notice = 2
        else:
            notice = -1
    return notice  # 카테고리의 번호를 반환한다


with requests.Session() as s:
    first_page = s.get('https://go.sasa.hs.kr')
    html = first_page.text
    soup = bs(html, 'html.parser')

    csrf = soup.find('input', {'name': 'csrf_test_name'})

    LOGIN_INFO.update({'csrf_test_name': csrf['value']})

    login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)
    if login_req.status_code != 200:
        raise Exception('로그인 되지 않았습니다!')

    # 일반 공지 : 22 (1 ~ 15)
    CATEGORY_NUM = get_Category()
    day_num = get_DayNum()
    # 각 공지별로 페이지 수를 저장한 dictionary
    PAGE_TOTAL = {"22": 16, "23": 7, "16": 13, "2": 26}

    # 게시물이 올라온 날짜 별로 기록해서 저장하는 이중 리스트
    board_list = [[] for i in range(day_num+1)]

    # 사용자가 선택한 CATEGORY_NUM의 PAGE를 가져와서 그만큼 탐색
    for page_num in range(1, PAGE_TOTAL[str(CATEGORY_NUM)]):
        # url 주소 예시 : 일반 공지 첫 번째 페이지 https://go.sasa.hs.kr/board/lists/22/page/1
        section_board_list_data = bs(s.get('https://go.sasa.hs.kr/board/lists/'+str(
            CATEGORY_NUM)+'/page/'+str(page_num)).text, 'html.parser')
        board_list_data = section_board_list_data.select(
            'div.box-body tbody span.hidden-xs')  # 게시물의 제목 가져오기
        url_list_data = section_board_list_data.select(
            'div.box-body tbody a')  # 게시물의 url 주소 가져오기
        time_list_data = section_board_list_data.select(
            'div.box-body tbody time')  # 게시물이 올라온 날짜 가져오기

        url_list = []  # url 주소를 저장해두는 list
        for data in url_list_data:
            # 예시로 /board/lists/page/2의 형식을 가진 데이터만 골라서 저장하기
            if 'board' == data.get('href').split('/')[1]:
                # https://go.sasa.hs.kr/를 포함한 주소를 담은 변수
                url = "https://go.sasa.hs.kr" + \
                    '/'.join(data.get('href').split('/'))
                url_list.append(url)  # url_list에 추가해준다

        # 데이터들은 게시물이 올라온 순서대로 저장되므로 3개의 list에 있는 요소는 동일한 것을 가리킨다
        for i in range(len(time_list_data)):
            data = time_list_data[i].text
            list_time = datetime.datetime.now()
            months = int(data[3])*10 + int(data[4])
            days = int(data[6])*10 + int(data[7])
            list_time = list_time.replace(month=months, day=days)
            # 오늘로부터 며칠 전에 올라온 게시물인지 확인하기 위한 과정
            index = -(list_time - datetime.datetime.now()).days

            if index <= day_num:  # 사용자가 보려고 하는 기한 안에 들어와있는 게시물이라면
                # (제목, url주소)를 묶어서 저장하는 tuple 변수
                dataset = (board_list_data[i].text, url_list[i])
                # 위의 dataset을 board_list[며칠 전의 게시물인지]에 추가해준다 예시로 2일전의 게시물이면 board_list[2]에 저장
                board_list[index].append(dataset)

    daysago = 0
    for board in board_list:
        cnt_idx = 0
        print(("="*11+" %02d days ago " + "="*11) %
              daysago)  # 며칠 전의 게시물인지 제목을 출력
        for data in board:
            # [출력순서] 제목:제목 url:url 의 형식으로 출력
            print("[%d] 제목:%s url:%s" % (cnt_idx, data[0], data[1]))
        if len(board) == 0:
            print("NONE")  # 해당하는 날짜에 게시물이 올라온게 없으면 NONE을 출력

        daysago += 1
