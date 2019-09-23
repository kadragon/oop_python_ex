# 달빛학사에서, 입력한 기간 이내에 존재하는 제출가능/신청가능/중요 공지를 확인하는 프로그램
# 그다지 실용성은 안 높은데 활용성도 안 높음

from os import system
import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # 파싱 라이브러리


class post:
    """
    게시물의 태그를 받아 저장하는 클래스입니다...
    """

    def __init__(self, tag, post_type):
        """
        문자열로 형변환된 html 태그를 받습니다.
        :parameter tag: 문자열로 형 변환된 html 태그
        :parameter type: 해당 게시물의 타입(0: 중요, 1: 제출가능, 2: 신청가능)
        """

        tag = tag.split("\n")  # 항상 21줄이다. (0~20)
        tag = (tag[7], tag[8], tag[14], tag[18])  # 각각 링크, 제목, 작성자, 날짜
        self.type = post_type  # 인자로 넘어온 것 그대로 대입

        # 이후는 각각의 형식에 맞추어 수정(문자열 메소드 이용)
        self.url = tag[0].replace('" target="_self">', "").replace(
            '<a class="boardList_item" href="', "").strip()
        self.name = tag[1].replace(
            '<span class="hidden-xs">', "").replace('</span>', "").strip()
        self.poster = tag[2].replace("</td>", "").strip()
        self.date = tag[3][tag[3].find(">") + 1:tag[3].find("<", 2)]

    def __str__(self):
        return (self.name + " by " + self.poster + " | " + self.date + " | " + "https://go.sasa.hs.kr" + self.url)


def get_html_with_session(s, url):
    """
    인자로 넘겨진 세션 s로 url의 html을 읽어들여 반환한다. 
    :parameter s: 세션
    :parameter url: html을 읽고 싶은 주소
    :return: url의 html tag
    """

    response = s.get(url)
    response.raise_for_status()

    return response.text


def parse_html(html):
    """
    주어진 html을 파싱한다. (BeautifulSoup 이용)
    :parameter html: 파싱할 html(get_html_with_session 결과 권장)
    :return: 파싱된 html
    """

    return bs(html, "html.parser")


def with_file(tag):
    """
    주어진 태그에 해당하는 게시물에 첨부 파일이 있는지 확인한다.
    :parameter tag: bs4.element.tag
    :return: 판단한 결과(True/False)
    """
    raise NotImplementedError


def empty(k):
    """
    주어진 iterable 객체가 비어 있는지 확인한다.
    :parameter k: iterable 객체
    :return: 비어 있으면 True, 아니면 False
    """

    return (len(k) == 0)


# 달빛학사 로그인에 필요한 정보 Dictionary
LOGIN_INFO = {
    'id': 'ID',
    'passwd': 'PW'
}

print("이 프로그램은 달빛학사에 올라온 중요 공지, 파일 제출 공지, 신청 공지를 표시해주는 프로그램입니다.")
print("아이디와 비밀번호를 입력해주세요.")
LOGIN_INFO["id"] = input("id > ")
LOGIN_INFO["passwd"] = input("pw > ")
system("cls")
print("로딩중입니다. 잠시만 기다려주세요...")

result_list = list()  # 최종적으로 얻고 싶은 결과 리스트
with requests.Session() as s:
    # 세션을 통해 실행한다...
    # 로그인 페이지의 html을 가져온다.
    login_page_html = get_html_with_session(s, "https://go.sasa.hs.kr")
    parsed_login_page = parse_html(login_page_html)  # 파싱(문법 해부)

    # csrf 코드를 찾는다.
    csrf = parsed_login_page.find('input', {"name": "csrf_test_name"})
    LOGIN_INFO.update({"csrf_test_name": csrf['value']})  # 로그인 정보를 업데이트한다.

    # 로그인 정보를 가지고 접속을 시도한다.
    login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)
    if login_req.status_code != 200:  # 만일 성공적으로 로그인하지 못했다면(200: 성공적으로 불러옴을 의미)
        raise Exception("로그인에 실패하였습니다.")  # 에러를 발생시키고 프로그램 종료.

    main_page_html = get_html_with_session(
        s, "https://go.sasa.hs.kr/main")  # 메인 페이지의 html 코드를 가져와
    parsed_main_page = parse_html(main_page_html)  # 파싱한다

    board_menu = parsed_main_page.select('ul.sidebar-menu li')  # 해당 태그를 검색
    board_id_list = list()  # 게시판, 기타 게시판 각 메뉴의 링크를 저장할 리스트

    not_yet = True  # 조건을 체크하기 위한 변수(원하는 부분이 나왔는지 안 나왔는지...)
    for i in board_menu:  # 각 줄에 대해 검색
        string_tag = str(i)  # 문자열화
        if ("게시판" in string_tag):  # 원하는 부분(게시판 이후)이 나오면
            not_yet = False  # 탐색 시작
        # 찾으려는 부분이 아니면(아직 안 나왔거나 분실물/설명서)
        if (not_yet or "분실물" in string_tag or "설명서" in string_tag):
            continue  # 계속 탐색
        if ("부서별" in string_tag):  # 탐색이 끝났으면(부서별 탭 -> 게시판, 기타 게시판 바로 아래)
            break  # 탈출

        # 이 조건문은 해당 탭이 링크를 포함하고 있는지를 확인한다.
        if string_tag.split("/")[1] == "board":
            board_id_list.append(string_tag.split(
                "/")[3])  # 보드 id만 얻어와 리스트에 추가

    for i in board_id_list:  # 게시판 종류별로 탐색
        board_url_without_page_num = (
            "https://go.sasa.hs.kr/board/lists/" + str(i) + "/page/")  # 페이지 번호 제외 주소
        page_num = 0  # 0에서 시작하여, 1, 2, ...

        while (True):  # 페이지 번호의 한계를 모르므로 무한 루프 + break문 이용
            page_num += 1  # 페이지 번호 1 증가
            board_url = board_url_without_page_num + \
                str(page_num)  # 해당 페이지로 이동
            board_html = get_html_with_session(s, board_url)  # html 불러오기
            board_html = parse_html(board_html)  # 파싱(그대로 대입됨에 주의)

            post_list = board_html.select("div.box-body tbody tr")  # 목록 받아오기
            if (empty(post_list)):  # 페이지 번호가 한계를 넘어, 아무런 게시물도 없다면
                break  # 무의미한 링크에 접속하는 것을 중단한다

            for j in post_list:  # 각 게시물에 대해...
                string_tag = str(j)  # 문자열화
                if ('tr class="warning"' in string_tag):  # 중요 공지라면?
                    result_list.append(post(string_tag, 0))  # 결과 리스트에 추가
                elif ('tr class="info"' in string_tag):  # 제출가능이라면?
                    result_list.append(post(string_tag, 1))  # 결과 리스트에 추가
                elif ('tr class="success"' in string_tag):  # 신청가능이라면?
                    result_list.append(post(string_tag, 2))  # 결과 리스트에 추가

print("로딩이 완료되었습니다.\n만일 비어 있다면, 진짜 없거나 아이디/비밀번호가 잘못된 것입니다.")

cnt = 0  # 순서
for i in result_list:  # 하나씩 출력함
    cnt += 1
    # __str__이 post 클래스에 구현되어 있음
    print("[" + str(cnt) + "] " + str(i), end=" ")
    # 종류에 따른 구분
    if (i.type == 0):
        print("(중요)")
    elif (i.type == 1):
        print("(제출가능)")
    else:
        print("(신청가능)")
