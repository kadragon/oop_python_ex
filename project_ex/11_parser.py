# pip3 install -U beautifulsoup4
# pip3 install -U requests

import bs4
import requests


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text


def sub_get_insert_time_and_press(url):
    """
    기사에서 기사 등록일과 언론사를 찾아 반환한다.
    :param url: 기사 url
    :return: 기사 등록일, 언론사
    """
    sub_html = get_html(url)  # get_html() 을 이용해서, 대상 기사에 접속 html tag 를 가져온다.
    sub_soup = bs4.BeautifulSoup(sub_html, 'html.parser')  # bs4 parser 를 이용하여, 뽑아오기 쉽게 parsing 한다.

    # <div class='sponser'> 안에 있는, <span class='t11'> 의 text 를 추출한다.
    news_insert_time = sub_soup.select('div.sponsor span.t11')[0].getText().split()[1]

    # <div class='press_logo'> 안에 있는, <a> 안에 있는 <img> 들 중에 첫번째[0] 요소의 title 을 가져온다.
    news_press = sub_soup.select('div.press_logo a img')[0].get('title')

    return news_insert_time, news_press


html = get_html('https://news.naver.com')
soup = bs4.BeautifulSoup(html, 'html.parser')

# <div class='main_component'> 안에 있는, <li> 안에 있는 <a> 를 모두 검색하여 List 형식으로 반환한다.
news_main = soup.select('div.main_component li a')

for i in news_main:
    # ex) <a href="https://news.naver.com/main/..."><strong>CPU 가격 30% 급등…중소 PC업체들 '비상'</strong></a>
    news_title = i.getText().strip()  # <a> 에 담겨있는 text 를 가져온다.
    news_url = i.get('href')  # <a> 에 설정되어 있는 href 값을 가져온다.

    # hotissue 가 주소 내에 있을 경우, 기사로 바로 전달되지 않기 때문에 등록일이나 언론사 찾지 않는다.
    if 'hotissue' not in news_url.split('/') and 'officeList' != news_url.split('/')[4][0:10]:
        news_insert_time, news_press = sub_get_insert_time_and_press(news_url)
        print("%s | %s | %s | %s" % (news_title, news_press, news_insert_time, news_url))
    else:
        print("%s | %s" % (news_title, news_url))
