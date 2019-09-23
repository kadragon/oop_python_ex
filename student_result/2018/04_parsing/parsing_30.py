from bs4 import BeautifulSoup as bs
import requests
import datetime
import webbrowser


LOGIN_INFO = {
    'id': '',
    'passwd': ''
}

reqlist = []

with requests.Session() as s:
    pagelogin = s.get('https://go.sasa.hs.kr')
    html = pagelogin.text
    soup = bs(html, 'html.parser')

    csrf = soup.find('input', {'name': 'csrf_test_name'})

    LOGIN_INFO['csrf_test_name'] = csrf['value']

    login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)

    if login_req.status_code != 200:
        raise Exception('로그인에 실패하였습니다.')

    board_sohak = bs(
        s.get('https://go.sasa.hs.kr/night_Control/user').text, 'html.parser')

    table = board_sohak.select('div.box-body table tbody tr td.text-center')
    tablename = board_sohak.select('div.box-body table thead tr.warning th')

    insertdict = {}
    names = []

    for i in tablename:
        name = i.getText().strip()
        insertdict[name] = ''
        names.append(name)

    index = 0
    for i in table:
        things = i.getText().strip()
        insertdict[names[index % 7]] = things
        index += 1

        if index % 7 == 0:
            reqlist.append(insertdict)
            insertdict = {}

today = datetime.date.today()


requestavail = False
for reqs in reqlist:
    if reqs['지도일'] == str(today):
        requestavail = True
        if reqs['승인'] == '승인':
            print('소학습실 신청이 승인되었습니다!')
        else:
            print('{} 선생님께 한 {}시 소학습실 신청이 승인되지 않았습니다.'.format(
                reqs['지도교사'], reqs['지도시간']))

if not requestavail:
    browse = input('오늘 소학습실 사용을 신청하지 않았습니다. 지금 하시겠습니까?(y/n)')
    if browse.lower() == 'y':
        webbrowser.open('https://go.sasa.hs.kr/night_Control/user')
