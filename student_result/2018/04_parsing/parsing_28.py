from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import sys

# 로그인한 사람의 정보
LOGIN_INFO = {
    'id': 'user_id',
    'passwd': 'user_passward'
}

# 로그인한 상태 유지
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

    # 현재날짜를 통해 1학기인지 2학기인지 판별
    now = datetime.now()
    if now.month >= 3 and now.month <= 7:
        smst = 1
    else:
        smst = 2

    # 1년동안 기숙사 벌점을 확인하기위해, 벌점 페이지에 접속한다
    section_board_list_data = bs(
        s.get('https://go.sasa.hs.kr/rating/rating_student_view').text, 'html.parser')

    # 기숙사 벌점을 가져오는 함수
    penalty_board = section_board_list_data.select('table.table tbody tr td ')

    # k가 홀수일 경우 본관 벌점, 짝수일 경우 기숙사이므로, 기숙사 벌점만 사용하기 위해 k가 2일때 first_penalty_board, 2일때는 second_penalty_board에 내용을 추가한다
    k = 1
    first_penalty_data = []
    second_penalty_data = []
    for i in penalty_board:
        for j in i:
            if k == 2:
                first_penalty_data.append(str(j).strip())
            elif k == 4:
                second_penalty_data.append(str(j).strip())
            if '현재까지' in j:
                k += 1
    # 위에서 판별한대로 1학기 일때와 2학기 일때 나눠 벌점을 출력한다.
    if smst == 1:
        # 만약 리스트의 2번째에 1번 벌점 목록을 표시하는 '1'이 없을 경우 벌점이 아예없는 경우이므로 종료시킨다
        if first_penalty_data[2] != '1':
            print("벌점이 없습니다.")
            sys.exit()
        first_board = []
        now = []
        index = 2
        # 하나의 표로 되어있기 때문에 2~7, 8~13...처럼 한 줄로 출력한다
        while index < len(first_penalty_data):
            now.append(first_penalty_data[index])
            index += 1
            if index % 6 == 2 and index > 2:
                first_board.append(now)
                now_score = int(now[4])
                now = []

        print("=" * 30, "1학기 기숙사 벌점", '=' * 30)
        for i in first_board:
            for j in i:
                print(j, end='||')
            print(' ')
        # 누계가 0보다 클경우 누계만 출력, 벌점이 더 많을 경우 퇴사까지 남은 벌점을 출력해준다.
        if now_score >= 0:
            print("현재 %d점입니다." % now_score)
        else:
            now_score = abs(now_score)
            left_score = 15 - now_score
            print("현재 벌점 %d점입니다" % abs(now_score))
            print("퇴사까지 %d점 남았습니다" % left_score)
    else:
        # 2학기도 1학기와 동일하게 처리해 출력한다
        if second_penalty_data[2] != '1':
            print("벌점이 없습니다.")
            sys.exit()
        second_board = []
        now = []
        index = 2
        while index < len(second_penalty_data):
            now.append(second_penalty_data[index])
            index += 1
            if index % 6 == 2 and index > 2:
                second_board.append(now)
                now_score = int(now[4])
                now = []
        print("=" * 40, "2학기 기숙사 벌점", '=' * 40)
        for i in second_board:
            print("||", end=' ')
            for j in i:
                print(j, end=' || ')
            print(' ')
        if now_score >= 0:
            print("현재 %d점입니다." % now_score)
        else:
            now_score = abs(now_score)
            left_score = 15 - now_score
            print("현재 벌점 %d점입니다" % abs(now_score))
            print("퇴사까지 %d점 남았습니다" % left_score)
