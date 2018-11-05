  # pip3 install -U beautifulsoup4
  # pip3 install -U requests

import bs4
import requests
import datetime  # 내일의 날짜를 알기 위한 library

def get_html(url):  # 웹 사이트 주소를 입력 받아, html tag를 읽어서 반환
    response = requests.get(url)
    response.raise_for_status()

    return response.text

tomorrow = datetime.date.today() + datetime.timedelta(days = 1)  # 내일의 날짜 받아오기
page_url = 'https://movie.naver.com/movie/bi/ti/running.nhn?code=402&sdate=' + str(tomorrow)  # 네이버 영화 - 내일 메가박스 세종의 상영시간표 접속
  # code=402 부분을 바꿔서 네이버 영화가 지원하는 다른 영화관의 시간표에도 접속 가능!
html = get_html(page_url)
soup = bs4.BeautifulSoup(html, 'html.parser')

movie_theater = soup.select('div.title h3')  # 상영시간표 정보 제공 - 영화관 이름 출력
for i in movie_theater:
    print(i.getText().strip())

tomorrow = str(tomorrow).split('-')
print(tomorrow[0] + '년 ' + tomorrow[1] + '월 ' + tomorrow[2] + '일 상영시간표')  # 상영시간표 정보 제공 - 날짜 출력

movie_list = soup.select('div.box_story_8 tr')

for i in movie_list:  # 각 영화 i에 대해서
    movie_name = i.select('th a')
    for j in movie_name:
        print(j.getText().strip(), end = ': ')  # 영화 이름 j를 출력
    movie_time_list = i.select('td a')
    for j in movie_time_list:
        movie_time = j.getText().strip()
        print(movie_time, end = ' ')  # 영화의 모든 상영시간 j를 출력
    print()
