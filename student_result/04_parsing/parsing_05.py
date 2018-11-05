# 실행 불가

import bs4 as b
import requests as re

#웹사이트의 주소를 반환
def get_url(url):
    link=re.get(url)
    link.raise_for_status()
    return link.text

#롯데시네마 박스오피스 상영중인 영화 순위
data='http://www.lottecinema.co.kr/LCHS/Contents/Movie/Movie-List.aspx'
#get_url로 주소를 저장
url=get_url(data)
soup=b.BeautifulSoup(url, 'html.parser')

# <ul class="curr_list movie_clist" id="ulMovieList"> 에서 <li class>의 목록들을 뽑아온다.
movie_list=soup.select('ul.curr_list movie_clist li')

#저장 변수
movie=[]
cnt=1

for i in movie_list:
    #<dl class="list_text"> 에서 영화 제목, 예매율, 평점을 뽑아 i번째의 리스트에 저장
    now = i.select('dl.list_text')
    #<dt> 에서 영화 제목
    #순위를 매겨주기 위해 cnt변수를 이용
    movie[i].append(str(cnt)+'위 '+now.select('dt a')[0].getText().split())
    #<dd> 에서 예매율, 평점
    movie[i].append('예매율: '+now.select('dd span.rate')[0].getText().split()[1])
    movie[i].append('평점: '+now.select('dd span.lit_score')[0].getText().split()[1])
    cnt+=1


#각 영화와 예매율, 평점을 한칸씩 띄어서 출력
for i in movie:
    for j in i:
        print(j)
    print("")
