# pip3 install -U beautifulsoup4
# pip3 install -U requests


import bs4
import sys
import requests
from bs4 import BeautifulSoup as bs  # parsing library

LOGIN_INFO = {
   'id': '',
   'passwd': ''
}


def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

print('''[달빛학사 Tagging 시스템 구현]
사용자가 접근할 수 있는 모든 게시판의 태그된 최근(1페이지)의 모든 게시물을 찾아서 태그한 사람, 게시물 링크를 출력해줍니다.
이름의 경우, 달빛학사 우측 상단의 정보를 자동으로 이용합니다. 
태그 예시 : @권정준 @정영근 @강동욱 ... ''')

print('ACCESSING GO SASA')

LOGIN_INFO['id'] = input('USER ID >> ')
LOGIN_INFO['passwd'] = input('USER PASSWD >> ')

with requests.Session() as s:
    # 로그인 페이지를 가져와서 html 로 만들어 파싱을 시도한다.
    first_page = s.get('https://go.sasa.hs.kr')
    html = first_page.text
    soup = bs(html, 'html.parser')

    # cross-site request forgery 방지용 input value 를 가져온다.
    csrf = soup.find('input', {'name': 'csrf_test_name'})

    # 두개의 dictionary 를 합친다.
    LOGIN_INFO.update({'csrf_test_name': csrf['value']})

    login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)


    main_page = s.get('https://go.sasa.hs.kr')
    html = main_page.text
    soup = bs(html, 'html.parser')

    try:
        soup.select('h4.box-title')[0].getText().strip() == '공지사항'
    except IndexError:
        print('LOGIN FAILED')
        sys.exit(0)
    else:
        print('LOGIN SUCCESS\n')

    print('SEARCHING...')
    #print(soup)

    myname = soup.select('a.dropdown-toggle span')[1].getText().split('(')[0].lstrip()

    boards = soup.select('ul.treeview-menu li a')

    #print(boards)

    board_list = []
    for i in boards:
        if 'board' == i.get('href').split('/')[1]:
            board_list.append(i.get('href').split('/')[3])

    #print(board_list)
    #board_list = ['32']
    for board_id in board_list: #게시판 접근
        new_board = bs(s.get('https://go.sasa.hs.kr/board/lists/' + board_id + '/page/1').text, 'html.parser')

        notices = new_board.select('a.boardList_item')

        #print(notices)
        for i in notices:
            #print('************')
            postlink = i.get('href')
            #print(postlink)
            extract = bs(s.get('https://go.sasa.hs.kr' + postlink).text, 'html.parser')
            try:
                comment = extract.select('div.comment-text small')
                #print(comment)
                for c in comment:
                    if c.getText().find('@'+myname)!=-1:
                        #print(c.getText())
                        print(extract.select('div.user-block span.username')[0].getText().lstrip())
                        print('Contents: '+c.getText())
                        print('Link: '+'https://go.sasa.hs.kr' + postlink)
                        print(' ')

            except IndexError as e:
                continue
