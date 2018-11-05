# pip install beautifulsoup4
# pip install requests

from bs4 import BeautifulSoup
import requests


print("백준 온라인 저지의 문제 번호를 입력해주세요")

flag=0
while flag==0:
    a=input()
    req1=requests.get('https://www.acmicpc.net/problem/'+a)
    html1=req1.text
    soup1=BeautifulSoup(html1, 'html.parser')
    if not soup1.select("div.page-header h1 span"):
        print("잘못 입력하셨습니다. 다시 입력해주세요")
        continue
    flag=1
    print("문제 링크: https://www.acmicpc.net/problem/" + a)
    probname=soup1.select('div.page-header h1 span')[1].getText().strip()
    print('문제 이름: ',probname)

print("문제 푼 사람의 랭킹을 출력합니다.")
print("등수, 아이디, 메모리(kb), 시간(ms), 언어 종류, 코드 길이(B) 순으로 20위까지 출력합니다")
print("20위까지 나오지 않는 경우 푼 사람이 20명이 안 되는 것입니다 TT")

req=requests.get('https://acmicpc.net/problem/status/'+a)
html=req.text
soup=BeautifulSoup(html, 'html.parser')
ranks_main=soup.select('div.table-responsive tbody tr td')

cnt=0
for i in ranks_main:
    ranks_title=i.getText().strip()
    cnt+=1
    if cnt%9!=2 and cnt%9!=3 and cnt%9!=0: print(ranks_title, end=" ")
    if cnt % 9 == 0: print(' ')

