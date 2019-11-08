import bs4
from selenium import webdriver
from datetime import datetime


def webdriver_maker():
    """
    headless 브라우저(창이 안뜨는)를 위해서 설정.
    :return: webdriver (크롬)을 생성
    """
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")

    return webdriver.Chrome('/Users/kadragon/Dev/oop_python_ex/project_ex/14_chromedriver',
                            options=options)


def timestamp_to_str(timestamp):
    """
    timestamp 를 2000-00-00 00:00:00 형태로 변환
    :param timestamp: timestamp
    :return: 2000-00-00 00:00:00
    """
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


driver = webdriver_maker()
driver.get('https://www.facebook.com/SASABamboo/')  # 세종과학예술영재학교 대나무숲 페이지 주소

# 페이스북의 경우 페이지 스크롤링을 해야 새로운 게시물을 볼 수 있다.
scroll_count = 20

# 페이지 스크롤링 코드
while driver.find_element_by_tag_name('div'):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs = driver.find_element_by_tag_name('div').text
    if 'End of Results' in Divs:  # 영어 버전에서 작동하는 코드
        print('end')
        break
    else:
        if scroll_count != 0:  # 일정량만 제한하기 위하여 조치함.
            scroll_count -= 1
            continue
        else:
            break

html = driver.page_source  # html 추출

soup = bs4.BeautifulSoup(html, 'html.parser')  # bs4에게 부탁
posts = soup.select('div.userContentWrapper')  # 게시물이 포함되어 있는 <div class='userContentWrapper'> 검색

first_post_pass = True

for post in posts:
    # 첫 포스트 제외 | 오래된 포스트일 가능성이 높음.
    if first_post_pass is True:
        first_post_pass = False
        continue

    j = post.select('div')

    print(timestamp_to_str(int(j[15].select('abbr')[0].get('data-utime').strip())))  # 날짜 출력
    print(j[16].getText().strip())  # 내용 출력

    print("=" * 20)

print('END')

driver.quit()  # 드라이버 사용 종료. 이 코드가 없을 경우 프로세스가 남게 됨.
