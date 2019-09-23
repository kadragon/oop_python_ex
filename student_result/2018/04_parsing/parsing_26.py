# pip install beautifulsoup4
# pip install requests
# pip install pyperlcip

import bs4
import requests
from sys import exit
import os
import pyperclip


def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


print("""
<<청와대 국민청원 둘러보기>>""")
print("국민의 나라, 정의로운 대한민국 - 문재인 정부")
print("""
""")


html = get_html("https://www1.president.go.kr/petitions?order=best")
soup = bs4.BeautifulSoup(html, 'html.parser')
agree = soup.select('div.csp_box div.bl_agree')
title = soup.select('div.csp_box div.bl_subject a')


print("─ 답변 대기중 목록 ─")
for i in range(0, len(title)):
    this_title = title[i].getText().strip().replace("제목 ", "")
    this_agree = agree[i+1].getText().strip().replace("참여인원  ", "")
    print("제목 : " + this_title)
    print("참여인원 : " + this_agree)
    print("─" * 20)

print("""

내용이 궁금한 청원이 있습니까?
몇 번째 청원인지 입력하면 주소를 클립보드에 복사해 드립니다.
범위를 벗어나는 수, 또는 아무 문자를 입력하면 프로그램이 종료됩니다.
""")

want = input("이 청원이 궁금합니다 : ")
if want.isdigit():
    want = int(want)
else:
    os.system('cls')
    exit()
if (want > len(title)) or (want < 1):
    os.system('cls')
    exit()
want = want-1

url = title[want].get('href')
url = "https://www1.president.go.kr" + url

os.system('cls')
print("")
print(url)
pyperclip.copy(url)
print("클립보드에 복사가 완료되었습니다")
