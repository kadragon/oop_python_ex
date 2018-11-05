"""
네이버 스포츠 홈페이지에서 오늘의 해외축구 주요 영상 중 가장 최근에 올라온 15개를 조회순으로 출력한다.
"""
import requests  # 웹 접속 관련 라이브러리
import bs4 # parsing 라이브러리
from operator import itemgetter # 리스트의 특정 요소를 통한 정렬 관련 라이브러리

def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: 데이터를 읽어올 인터넷 url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text

html = get_html('https://sports.news.naver.com/wfootball/vod/index.nhn')
soup = bs4.BeautifulSoup(html, 'html.parser')

# <div class='video_list'> 안에 있는 <ul> 안에 있는 <li>를 모두 검색하여 리스트 형식으로 반환한다.
video_list_data = soup.select('div.video_list > ul li')
# <div class='video_list'> 안에 있는 <ul> 안에 있는 <li> 안에 있는 <a>를 모두 검색하여 리스트 형식으로 반환한다.
video_list_data2 = soup.select('div.video_list > ul li a')

def get_infor(i):
    video_tag = i.find('span', {'class': 'tag'}).getText() # 영상의 태그
    video_title = i.find('span', {'class': 'title'}).getText() # 영상의 제목
    video_date = i.find('span', {'class': 'time'}).getText().replace('재생시간','') # 영상 재생시간
    video_play = int(i.find('span', {'class': 'play'}).getText().replace('재생 ','').replace(',','')) # 영상 재생횟수
    return video_tag, video_title, video_date , video_play

#print(video_list_data[0])
#print(video_list_data[0].find('span', {'class': 'title'}).getText())

print(" < 오늘의 해외축구 조회순 영상 > ")

infor_list = [] # 영상 태그, 제목, 재생시간, 조회수가 담긴 리스트를 저장할 리스트
url_list = [] # 영상 주소를 저장할 리스트

# 영상 태그, 제목, 재생시간, 조회수가 담긴 리스트를 infor_list에 저장
for i in video_list_data:
    video_tag, video_title, video_date , video_play = get_infor(i)
    infor_list.append([video_tag, video_title, video_date , video_play])
    #print("[%s] %s (%s) | %s "%(video_tag, video_title, video_date, video_play))

# 영상 주소가 담긴 리스트를 url_list에 저장
for i in video_list_data2:
    news_title = i.getText().strip()  # <a> 에 담겨있는 text 를 가져온다.
    news_url = i.get('href')  # <a> 에 설정되어 있는 href 값을 가져온다.
    url_list.append([news_url])

# 영상을 조회수가 높은 순서대로 정렬
infor_list.sort(key=itemgetter(3), reverse= True)

for i in range(len(infor_list)):
    print('[%s] %s(%s) | 조회수 : %s |' %(infor_list[i][0],infor_list[i][1],infor_list[i][2],infor_list[i][3]), end=' ')
    print('https://sports.news.naver.com'+url_list[i][0])

