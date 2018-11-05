# pip install beautifulsoup4
# pip install requests
#웹 공부나 다른 언어를 공부할 수 있는 생활코딩의 수업들 소개
URL1='https://opentutorials.org/course/1'

from bs4 import BeautifulSoup
import requests

responce = requests.get(URL1)
html=responce.text

soup=BeautifulSoup(html, 'html.parser')
for tag in soup.select('div[class="label public"]'):
    print(tag.text.strip())