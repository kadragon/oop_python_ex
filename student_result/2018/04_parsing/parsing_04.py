# pip install -U beautifulsoup4
# pip install -U requests

from bs4 import BeautifulSoup as bs
import requests

# 한중일 문자 포맷팅 해결 함수
# http://gnoownow10.cafe24.com/cjk-formatting.html
# 여기부터
import unicodedata


def preformat_cjk(string, width, align='<', fill=' '):
    count = (width - sum(1 + (unicodedata.east_asian_width(c) in "WF")
                         for c in string))
    return {
        '>': lambda s: fill * count + s,
        '<': lambda s: s + fill * count,
        '^': lambda s: fill * (count / 2) + s + fill * (count / 2 + count % 2)
    }[align](string)
# 여기까지


LOGIN_INFO = {
    'id': 'USER_ID',
    'passwd': 'USER_PASSWORD'
}

with requests.Session() as sess:
    login_soup = bs(sess.get('https://go.sasa.hs.kr').text, 'html.parser')
    login_csrf = login_soup.find('input', {'name': 'csrf_test_name'})
    LOGIN_INFO.update({'csrf_test_name': login_csrf['value']})
    login_req = sess.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)
    if login_req.status_code != 200:
        raise Exception('로그인되지 않았습니다!')

    refresh = True
    while refresh:
        music_soup = bs(
            sess.get('https://go.sasa.hs.kr/RcmndMusic/musicView').text, 'html.parser')
        table = music_soup.select('table tbody tr')
        print('| 순위 | 좋아요 | '+' '*22+' 곡명 '+' '*22+' | '+' ' *
              19+' 링크 '+' '*18+' |   추천자   | 추천시간 | 좋아요 여부 |')
        idx_list = []
        for i in table:
            rank = i.select('th')[0].getText()
            temp = i.select('td')
            button = temp[0].find('button')
            button_clicked = True if button.getText().strip() == '취소' else False
            idx_list.append([button.get('id'), button_clicked])
            like_number = temp[1].getText().strip()
            title = temp[2].getText().strip()
            link = temp[3].find('a').get('href')
            person = temp[4].getText().strip()
            if person == '삭제':
                person = '   USER   '
            time = temp[5].getText().strip()
            print('| %4s | %6s | %s | %s | %-6s | %s |      %s      |' % (rank, like_number,
                                                                          preformat_cjk(title, 50), link, person, time, 'O' if button_clicked else 'X'))

        print()
        print('좋아요, 혹은 좋아요를 취소하고 싶은 곡의 순위를 입력하세요.')
        print('종료하려면 0을 입력하세요.')
        while True:
            n = input()
            if (not n.isdigit()) or (int(n) > len(idx_list)):
                print('형식에 맞게 입력하세요.')
                continue
            if int(n) == 0:
                refresh = False
                break
            else:
                n = int(n)
                idx = idx_list[n-1][0][6:] if idx_list[n -
                                                       1][1] else idx_list[n-1][0][4:]
                action = 'delete' if idx_list[n-1][1] else 'insert'
                print(idx, action)
                res = sess.post('https://go.sasa.hs.kr/RcmndMusic/likeControl',
                                data={'musicIdx': int(idx), 'action': action})
                if res.status_code != 200:
                    raise Exception('오류가 발생했습니다.')
                break
