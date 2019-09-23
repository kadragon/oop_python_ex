# pip install -U requests
# pip install -U beautifulsoup4

import requests
import bs4


def get_html(url):  # html 가져오는 함수
    response = requests.get(url)
    response.raise_for_status()

    return response.text


# html에서 판매랭킹 1위부터 10위까지 상품 브랜드, 상품 이름, 상품 가격 가져오는 함수
def sub_get_insert_time_and_press(url):
    sub_html = get_html(url)
    sub_soup = bs4.BeautifulSoup(sub_html, 'html.parser')
    name_temp = []
    brand_temp = []
    price_temp = []

    for i in range(0, 10):
        item_brand = sub_soup.select('div.article_info p.item_title a')[
            i].getText()  # 상품 브랜드 가져오기
        item_name = sub_soup.select('div.article_info > p.list_info')[
            i].get('title')  # 상품 이름 가져오기
        item_price = sub_soup.select('div.article_info > p.price')[
            i].getText().split()[1]  # 상품 가격 가져오기
        if item_price == '▼' or item_price == '▲':  # 예외처리
            item_price = sub_soup.select('div.article_info > p.price')[
                i].getText().split()[0]
        name_temp.append(item_name)  # 상품 이름 list에 추가
        brand_temp.append(item_brand)  # 상품 브랜드 list에 추가
        price_temp.append(item_price)  # 상품 가격 list에 추가

    return brand_temp, name_temp, price_temp  # 상품 이름, 브랜드, 가격 list 3개 return


def recom_size(n):  # 관심있는 상품 url 출력 함수
    # 무신사 판매랭킹 Top 10 주소 html
    recom_html = get_html('https://store.musinsa.com/app/contents/bestranking')
    recom_soup = bs4.BeautifulSoup(recom_html, 'html.parser')
    print("관심있는 상품의 url입니다.")
    print("https://store.musinsa.com"+recom_soup.select('div.list_img a')
          [n-1].get('href'))  # 관심있는 랭킹의 상품 url 출력


brand_item, name_item, price_item = sub_get_insert_time_and_press(
    'https://store.musinsa.com/app/contents/bestranking')  # 무신사 판매랭킹 Top 10 받아오기

print("무신사 판매랭킹 Top 10")
for i in range(0, 10):  # 판매랭킹 Top 10 브랜드, 이름, 가격 출력
    print("Rank %d : %s | %s | %s" %
          (i+1, brand_item[i], name_item[i], price_item[i]))

while 1:
    # 관심있는 상품의 번호 물어보기
    a = input('\n관심있는 상품이 있다면 번호를 눌러주세요 (관심있는 상품이 없다면 0을 입력하세요) ')
    if a == '0':  # 관심있는 상품 없다면
        break  # 프로그램 종료
    elif a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8' or a == '9' or a == '10':  # 관심있는 상품 있다면
        recom_size(int(a))  # 관심 상품 url 출력
        break
    else:
        print("0부터 10까지 정수를 입력해주십시오.")  # 잘못된 입력이라면 올바른 입력 유도
