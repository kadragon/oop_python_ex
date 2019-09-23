import requests
import itertools
from bs4 import BeautifulSoup as bs


# 좋아하는 음식과 싫어하는 음식 입력받기
# 리턴값: 좋아하는 음식과 싫어하는 음식 리스트


def input_favor():
    like = input('공백을 기준으로 좋아하는 음식을 모두 적어주세요: ').split()
    hate = input('공백을 기준으로 알러지가 있거나 싫어하는 음식을 모두 적어주세요: ').split()

    return like, hate


# 웹사이트 크롤링
# 리턴값: 급식 메뉴 및 급식 날짜

def crawl_menu():
    # 로그인 정보
    LOGIN_INFO = {
        'id': 'ID',
        'passwd': 'PASSWD'
    }

    with requests.Session() as s:
        # 달빛학사 로그인
        url = 'https://go.sasa.hs.kr'
        resp = s.get(url)
        html = resp.text
        soup = bs(html, 'html.parser')

        csrf = soup.find('input', {'name': 'csrf_test_name'})
        LOGIN_INFO.update({'csrf_test_name': csrf['value']})
        login_req = s.post(
            'https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)

        # 급식 페이지로 접속
        menu_url = 'https://go.sasa.hs.kr/main/foodList'
        menu = s.get(menu_url)
        html = menu.text
        soup = bs(html, 'html.parser')

        # 급식 데이터 크롤링
        # / 을 기준으로 음식을 구분한다
        all_menu = soup.select('div.timeline-body')
        all_menu = [i.get_text().strip().split('/') for i in all_menu]

        # 급식 날짜 크롤링
        # 공백을 기준으로 날짜를 구분한다
        all_menu_time = soup.select('span.bg-teal')
        all_menu_time = [i.get_text().strip() for i in all_menu_time]

        return all_menu, all_menu_time


like, hate = input_favor()
all_menu, all_menu_time = crawl_menu()

meal = ['아침', '점심', '저녁']

# 좋아하는 음식 찾기
print("[이번 3일 동안 나오는 좋아하는 음식은...]")
for i in range(len(all_menu)):
    for j in all_menu[i]:
        for k in like:
            if k in j:
                print(j.strip(), all_menu_time[i // 3], meal[i % 3])

print()

# 싫어하는 음식 찾기
print("[이번 3일 동안 나오는 싫어하는/못 먹는 음식은...]")
for i in range(len(all_menu)):
    for j in all_menu[i]:
        for k in hate:
            if k in j:
                print(j.strip(), all_menu_time[i // 3], meal[i % 3])
