# 달빛학사 로그인
# 게시판 선택
# 'N'이 붙은 것만 조회

import requests
import sys
import bs4

# 달빛학사 아이디와 비밀번호를 입력하고 사용
LOGIN_INFO = {
    'id': '',
    'passwd': ''
}


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어들여 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text


with requests.Session() as s:
    first_page = s.get('https://go.sasa.hs.kr')
    html = first_page.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

# 달빛학사 계정 로그인
csrf = soup.find('input', {'name': 'csrf_test_name'})
LOGIN_INFO.update({'csrf_test_name': csrf['value']})
login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)


if login_req.status_code != 200:
    raise Exception('로그인 안됨')


print(LOGIN_INFO['id'] + " 로그인하였습니다.")
print("========================================================")
print("1. 달빛학사에서 새로 올라온(N 표시가 있는) 게시글 목록을 검색합니다.")
print("2. 원하는 게시판 번호를 선택하세요.")
print("3. 1: 일반 공지, 2: 교과 공지, 3: 대회 및 캠프, 4: 분실물")
print("4. 프로그램을 종료하고 싶으면 'exit'를 쳐주시면 됩니다.")
print("========================================================")


i = True
while i:
    print('--------------------------------------------------------')
    target_page = input('번호를 선택하세요.')   # 보고 싶은 게시판 선택
    target_url = ''
    if target_page == '1':
        target_url = 'https://go.sasa.hs.kr/board/lists/22/page/1'
        print("------------------일반 공지 새글--------------------")
    elif target_page == '2':
        target_url = 'https://go.sasa.hs.kr/board/lists/23/page/1'
        print("------------------교과 공지 새글--------------------")
    elif target_page == '3':
        target_url = 'https://go.sasa.hs.kr/board/lists/16/page/1'
        print("------------------대회 및 캠프 새글--------------------")
    elif target_page == '4':
        target_url = 'https://go.sasa.hs.kr/board/lists/2/page/1'
        print("------------------분실물 새글--------------------")
    elif target_page == 'exit':
        print("------------------프로그램 종료------------------------")
        break
    else:   # 올바른 입력 유도
        print('1~4 숫자 입력')
        continue

    # print(target_url)

    html = s.get(target_url).text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    all_news = soup.select('div.box tbody a.boardList_item')    # 모든 글을 가져온다

    a = []
    a.append(all_news)
    # print(a)

    for i in all_news:
        news_text = i.getText().strip()
        news_info = news_text.split('\n')
        news_title = news_info[0]
        if len(news_info) == 4:     # 'N'자가 html 텍스트 중에 포함된 경우에만 split 결과의 리스트 원소 개수가 4
            news_url = i.get('href')
            print('')
            print('* %s | https://go.sasa.hs.kr%s' %
                  (news_title, news_url))  # 글의 제목과 url 출력
