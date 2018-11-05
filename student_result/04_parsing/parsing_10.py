#pip install -U beautifulsoup4
#pip install -U requests

import requests
import sys
from bs4 import BeautifulSoup as bs

# 달빛학사 아이디와 비밀번호를 입력하고 사용하세요!!!!!!!!
LOGIN_INFO = {
    'id' : '',
    'passwd' : ''
}

INPUT_INFO = {}

REC_INFO = {}

def get_html(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.text

with requests.Session() as s :
    first_page = s.get('https://go.sasa.hs.kr')
    html=first_page.text
    soup = bs(html,'html.parser')

with requests.Session() as y :
    youtube_page = y.get('https://www.youtube.com')
    yhtml=youtube_page.text
    ysoup=bs(yhtml, 'html.parser')

with requests.Session() as mus :
    music_first_page = mus.get('https://go.sasa.hs.kr/Rcmnd/musicView')
    music_html=music_first_page.text
    music_soup = bs(music_html,'html.parser')

with requests.Session() as mel :
    melon_page = mel.get('http://www.genie.co.kr/chart/top200')
    melon_html = melon_page.text
    melon_soup = bs(melon_html, 'html.parser')

# 지니뮤직 차트 따오기
# 멜론도 하고 싶었으나, 멜론은 크롤링을 막더군요 ㅠㅠㅠㅠ
def JINI() :
    print("<<지니뮤직 1-50 차트입니다>>")
    use_melon_data = melon_soup.select('td.info a')
    ranking_data=[]
    for i in use_melon_data :
        ranking_data.append(i.getText().strip())

    cnt=0
    cnt2=1
    for i in ranking_data :
        cnt+=1

        if cnt==1 :
            print(cnt2, end='')
            print(" ", end='')
            cnt2+=1
        print(i + " | ", end='')
        if cnt==3 :
            print('')
            cnt=0
    print('')
    print('## 지니뮤직 차트 검색은 1회만 가능하니, 다음에는 노래 이름을 검색해주세요.##')

print("현재 사용자 : " + LOGIN_INFO['id'])
print("=========================공지============================")
print("1. 유튜브 채널, 광고 영상은 자동으로 필터링됩니다.(걱정하지 마세요!)")
print("2. 원하는 노래를 자세히 검색해주세요.")
print("3. 지니뮤직 차트를 보고 싶으면 '지니뮤직'을 검색해주세요.")
print("4. 프로그램을 종료하고 싶으면 'exit'를 쳐주시면 됩니다.")
print("5. 추천한 노래는 자동으로 좋아요가 눌립니다.")
print("6. 다만, 추천 후 딜레이가 존재하여 '현재 랭킹'에는 반영되지 않습니다.")
print("========================================================")

music = input("추천하려고 하는 노래의 제목을 써주세요. 가장 위에 뜨는 영상이 추천됩니다. ")

if music=="지니뮤직" :
    JINI()
    music = input("\n추천하려고 하는 노래의 제목을 써주세요. 가장 위에 뜨는 영상이 추천됩니다. ")

if music == "exit" :
    print("종료하겠습니다")
    sys.exit(1)

music.replace(" ", "+")

# 달빛학사 계정 로그인
csrf=soup.find('input', {'name' : 'csrf_test_name'})
LOGIN_INFO.update({'csrf_test_name' :csrf['value']})
login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)

if login_req.status_code != 200 :
    raise Exception('로그인 안됨')

# 유튜브 링크 끌고오기
youtube_data = bs(y.get("https://www.youtube.com/results?search_query="+music).text, 'html.parser')
use_youtube_data = youtube_data.select('div.yt-lockup-content h3 a')

# 추천할 유튜브 링크 완성
link = "https://www.youtube.com" + use_youtube_data[0].get('href')

# 동영상 거르기(광고, 유튜브 채널, 유튜브 계정)
for i in range(1,5):
    if link.find("adservice")!=-1 or link.find("channel")!=-1 or link.find("user")!=-1:
        link = "https://www.youtube.com" + use_youtube_data[i].get('href')
    else : break

# 추천할 유튜브 링크
print(music, "링크의 주소입니다", link)

# 달빛학사의 노래추천 링크 가져오기
# 사실 주소가 정해져있기는 하지만 다른 것에도 활용할 수 있도록 복잡한 과정 거침
section_board_list_data = bs(s.get('https://go.sasa.hs.kr/main').text, 'html.parser')
board_list_data = section_board_list_data.select('ul.sidebar-menu li a')
for i in board_list_data :
    title = i.getText().strip()
    if title == '노래 추천' :
        url = i.get('href')
        break

# 노래추천 페이지 html
use_data = bs(s.get("https://go.sasa.hs.kr"+url).text, 'html.parser')

# 노래 추천 위한 csrf 획득
use_enter_data = use_data.select('div.box-body form')
music_csrf=use_data.find('input', {'name' : 'csrf_test_name'})
INPUT_INFO.update({'youtube' : link})
INPUT_INFO.update({'csrf_test_name' : music_csrf['value']})

music_req = s.post('https://go.sasa.hs.kr/RcmndMusic/musicView', data=INPUT_INFO)

use_data = bs(s.get("https://go.sasa.hs.kr"+url).text, 'html.parser')
use_new_data = use_data.select('div.col-md-12 button')

# 노래 추천 고유 ID 획득
identify=[]
for i in use_new_data :
    identify.append(i.get('id'))

# 노래 좋아요 과정
idx=int(identify.pop()[6:])
REC_INFO.update({'musicIdx' : idx})
REC_INFO.update({'action' : 'insert'})

# 노래 좋아요 누르기
s.post('https://go.sasa.hs.kr/RcmndMusic/likeControl', data=REC_INFO)


# 랭킹 출력
# 흥미로운 점은, 좋아요를 눌렀지만 바로 반영되지 않는다는 것입니다
# 아마도 post로 보내지는데 딜레이가 존재해서 그렇겠죠?
use_list_data = use_data.select('div.col-md-12 td')
print("========현재 랭킹========")
tag=0
rank=1
a=[]
a.clear()

for i in use_list_data :
    tag+=1
    name = i.getText().strip()
    a.append(name)
    if tag>5 :
        if a[4]=="삭제" :
            print(rank , "내가 추천함", a[2], end=" ")
            print('|| ' + "좋아요" +' : ' +a[1], end='')
        else :
            print(rank , a[4], a[2], end=" ")
            print('|| ' + "좋아요" +' : ' +a[1], end='')

        if a[0]=="취소" :
            print(" || 좋아요 누름")
        else :
            print("")

        a.clear()
        rank+=1
        tag=0
