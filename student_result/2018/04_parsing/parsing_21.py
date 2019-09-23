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


def get_userinfo():
    LOGIN_INFO['id'] = input('user id >> ')
    LOGIN_INFO['passwd'] = input('user passwd >> ')


def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


print('''
2018.10.25. Coded

이 프로그램은 Go Sasa에서 제출가능한 과제를 읽어옵니다.
각 과제를 표시하면 후에 당신의 과제를 날짜 오름차순으로 출력해줍니다.
''')

print('Access to Go Sasa to extract your schedule...')

get_userinfo()

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
        print('Login Failed')
        sys.exit(0)
    else:
        print('Login Success\n')

    boards = soup.select('ul.treeview-menu li a')

    # print(boards)

    board_list = []
    for i in boards:
        if 'board' == i.get('href').split('/')[1]:
            board_list.append(i.get('href').split('/')[3])

    # print(board_list)

    schedule = {}

    for board_id in board_list:
        new_board = bs(s.get('https://go.sasa.hs.kr/board/lists/' +
                             board_id + '/page/1').text, 'html.parser')
        notices = new_board.select('div.box-body tr.info')
        for i in notices:
            try:
                if i.select('span.text-info')[0].getText() == '[제출가능]':
                    link = i.select('a.boardList_item')[0].get('href')

                    extract = bs(s.get('https://go.sasa.hs.kr' +
                                       link).text, 'html.parser')
                    due_date = extract.select(
                        'small.text-info')[0].getText().split(' ')[3]
                    date = float(due_date.split(
                        '-')[1]+'.'+due_date.split('-')[2])
                    print('Due Date : '+due_date)

                    name = i.select('span.hidden-xs')[0].getText()
                    print(name)

                    choice = input('일정에 추가하시겠습니까? (y/n)  ')

                    if choice == 'y':
                        schedule[name] = date

                    print('\n')

            except IndexError:
                continue

    schedule = sorted(schedule.items(), key=lambda kv: kv[1])
    print("My Schedule::\n")
    for i in schedule:
        print("%s :: %.2f 제출" % i)

    # boards = bs(s.get('https://go.sasa.hs.kr/main').text, 'html.parser')
    # print(boards.select('ul treeview-menu li a'))
    # for i in soup.select('ul.treeview-menu li')[0]:
     #   print()
      #  print(type(i))
       # print('\n')
