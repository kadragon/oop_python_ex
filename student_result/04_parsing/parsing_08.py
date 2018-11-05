# -*- coding: utf-8 -*-
"""
Title       arXiv에 등록된 인공지능 논문 확인
Date        2018.10.25
"""

# pip3 install -U beautifulsoup4
# pip3 install -U requests

import requests  # 웹 접속 관련 라이브러리
import random  # 랜덤 함수 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library

# 최신 인공지능 논문 정보가 담겨 있는 arXiv 파싱
html = requests.get('https://arxiv.org/list/cs.AI/recent').text
soup = bs(html, 'html.parser')
title_main = soup.select('dd')  # dd tag 정보 가져오기
title_main2 = soup.select('dt')  # dt tag 정보 가져오기

title = []
authors = []
cite = []

# dd tag에서 정보 파싱
for i in title_main:
    title.append(i.select('div.list-title')[0].getText())
    authors.append(i.select('div.list-authors')[0].getText())

# dt tag에서 정보 파싱
for i in title_main2:
    cite.append(i.select('span.list-identifier')[0].getText())

# print(cite)
title.reverse()
authors.reverse()
cite.reverse()

# 랜덤 숫자를 도출한다.
rand = random.randint(0, 15)
# print(rand)
# 논문의 제목과, 저자, Citation 정보를 불러온다.

# 도출된 랜덤 숫자를 기반으로 최신 인공지능 논문을 뽑아준다.
# arXiv에 공개된 최신 인공지능 논문 기준
a = title[rand]
b = authors[rand]
c = cite[rand]

print('='*50)
print('읽어볼 만한 최신 인공지능 논문 추천')
print('='*50)

# 논문 정보를 아래와 같이 가공함
year = 2000+int(c[6:8])
month = int(c[8:10])
paper_title = a[8:]
paper_authors = b[9:]
paper_url = 'https://arxiv.org/pdf/' + c[6:16]

# 논문 정보 출력
print('논문 제목: ' + paper_title)
print('논문 발표 년월: ' + str(year) + '년 ' + str(month) + '월')
print('저자: ' + paper_authors)
print('URL: ' + paper_url)
