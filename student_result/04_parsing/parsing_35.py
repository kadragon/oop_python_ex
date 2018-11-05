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

num=0
check=0
count= int(input('건강백과의 키워드와 링크에 대해 알아볼 페이지 수를 입력하세요(페이지당 15개):'))

while True: # 정보가 없거나 주어진 숫자까지 반복
    num=num+1    # 페이지의 양식에 맞추어 1부터 페이지를 하나하나 완성하는 과정
    pre_html = 'https://terms.naver.com/list.nhn?cid=50871&categoryId=50871&page='
    pre_html += str(num)
    html = get_html(pre_html)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # <div class='subject'> 안에 있는, <strong class='title'> 안에 있는 <a> 중 첫 번째 것만을 검색하여 List 형식으로 반환한다.
    disease_info = soup.select('div.subject > strong.title > a:nth-of-type(1)')

    for i in disease_info:
        if not disease_info or num>count:     # 정보가 없거나 주어진 숫자까지
            check=1
        disease_title = i.getText().strip()  # <a> 에 담겨있는 text 를 가져온다.
        disease_url = i.get('href')  # <a> 에 설정되어 있는 href 값을 가져온다.
        print("%s | https://terms.naver.com%s" % (disease_title, disease_url))
    if check==1:
        break