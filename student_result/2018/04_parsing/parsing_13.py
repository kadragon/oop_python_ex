import bs4
import requests
# pip3 install requests
# pip3 install beautifulsoup4


def get_html(url):
    """웹사이트 주소를 입력받아 html tag를 읽어 반환"""

    response = requests.get(url)
    response.raise_for_status()

    return response.text

# 전달받은 페이지의 제목, 별점, 리뷰를 반환 함수


def movie_review_page(page):
    html = get_html(
        'https://movie.naver.com/movie/point/af/list.nhn?&page='+str(page))
    soup = bs4.BeautifulSoup(html, 'html.parser')

    review_point = soup.select('div#old_content td.point')
    review_title = soup.select('div#old_content td.title')

    review = []

    for i, j in zip(review_title, review_point):
        content = i.getText().strip().strip("신고").strip().split('\n')
        point = int(j.getText().strip())
        review.append([content[0], point, content[1]])

    return review


# a 페이지부터 b 페이지까지 리뷰 합산해서 반환
def review_index(a, b):
    review = []
    for i in range(a, b+1):
        review.extend(movie_review_page(i))
    return review

# 리뷰 출력


def print_review(review, a, b):
    print("%d page ~ %d page" % (a, b))
    for r in review:
        print("%s (%d) : %s" % (r[0], r[1], r[2]))

# 원하는 영화의 평균평점을 확인


def title_avg_point(review, title):
    count = 0
    sum = 0
    for r in review:
        if(r[0] == title):
            count += 1
            sum += r[1]
    try:
        return sum/count
    except ZeroDivisionError:
        print('<%s>영화의 리뷰가 없습니다' % (title))


a, b = map(int, input('페이지를 띄어쓰기로 구분해 입력해주세요(ex: 1 20) :').split())
review = review_index(a, b)

# a~b페이지까지 모든 리뷰확인
print('리뷰를 확인합니다.')
print_review(review, a, b)

# 영화 평점 확인
title = input('\n평점을 확인하고싶은 영화를 입력해주세요 : ')
print("%.3f" % title_avg_point(review, title))
