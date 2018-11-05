# pip3 install -U requests
# pip3 install -U beautifulsoup4
# pip3 install datetime
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def conv_url(url):  # 입력된 url에서 html 파일을 얻어온다.
    header = {'User-Agent': ''}  # 그냥 하면 뜨는 IndexError 방지용
    req = requests.get(url, headers=header)  # header를 사용
    html = req.text  # text 형식으로 변환
    return BeautifulSoup(html, 'html.parser')  # 파싱

soup = conv_url("https://www.melon.com/chart/index.htm")  # 멜론차트의 html 파일

def get_first_albums_number(soup):  # 멜론 차트 1등의 앨범 고유번호를 얻어온다.
    tag_list = soup.select('#lst50')
    abcd = tag_list[0]
    first_album = abcd.select('div.wrap_song_info a')[3].get('href')
    return first_album[37:45]

first_album_url = "https://www.melon.com/album/detail.htm?albumId=" + get_first_albums_number(soup)  # 1등 앨범의 url
new_soup = conv_url(first_album_url)  # 1등 앨범의 url에서의 html 파일

def find_youtube_url(song_name):  # 멜론의 1등 앨범의 url 링크를 얻어옴
    youtube_url = "https://www.youtube.com/results?search_query=" + song_name
    you_soup = conv_url(youtube_url)
    song_list_href = you_soup.select('div.yt-lockup-content a')[0].get('href')
    idx = 0
    while 'google' in song_list_href or 'channel' in song_list_href:  # 예외 처리 : 광고나 채널이 맨 위에 나타날 경우
        idx += 2
        song_list_href = you_soup.select('div.yt-lockup-content a')[idx].get('href')
    return "https://www.youtube.com" + song_list_href


def get_album_info(soup_prime):  # 앨범의 정보를 얻어옴
    song_name = soup_prime.select('div.entry div.song_name')[0].getText().split()[1]  # 앨범 이름
    artist = soup_prime.select('div.entry div.artist a')[0].getText().strip()  # 앨범 아티스트
    soup_list = soup_prime.find_all('dd')
    date = soup_list[0].getText()  # 발매일
    genre = soup_list[1].getText()  # 장르
    publisher = soup_list[2].getText()  # 발매사
    agency = soup_list[3].getText()  # 기획사
    return [song_name, artist, date, genre, publisher, agency]

album_info = get_album_info(new_soup)  # 앨범의 정보를 담고 있는 리스트
album_info.append(find_youtube_url(album_info[0]))  # 앨범 정보 리스트에 url을 추가

now = datetime.now()  # 시간 출력을 위함
(year, month, day, hour) = (now.year, now.month, now.day, now.hour)

print("[ {}년 {}월 {}일 {}시의 멜론 차트 1등 앨범은? ]\n"
      "♬ {} - {} ♬\n"
      "■ 발매일 : {}  |  장르 : {}\n"
      "■ 발매사 : {}\n"
      "■ 기획사 : {}\n"
      "( YouTube 링크 : {} )".format(year, month, day, hour, album_info[0], album_info[1], album_info[2], album_info[3], album_info[4], album_info[5], album_info[6]))