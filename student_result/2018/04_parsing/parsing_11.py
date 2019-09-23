from bs4 import BeautifulSoup
from selenium import webdriver  # pip install selenium
from time import sleep

"""
Chrome web driver 설치
https://sites.google.com/a/chromium.org/chromedriver/downloads
"""
driver = webdriver.Chrome(
    '/Users/jwon0615/Downloads/chromedriver')  # chromedriver가 들어있는 path
driver.implicitly_wait(3)
driver.get('http://likms.assembly.go.kr/bill/LatestPassedBill.do')
sleep(1)

billList = []
key = 'o'
page = 1

while(key != 'x'):

    command = "GoPage("+str(page)+");"  # 페이지 번호 javascript로 전해준다
    driver.execute_script(command)
    sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    billList.extend(soup.select('div.tableCol01 table tbody tr'))
    print("현재 페이지: {}".format(page))
    print("지금까지 수집한 통과의안 목록: ", len(billList), "개")

    key = input('enter로 다음페이지, x로 종료\n')

    page += 1

for case in billList:
    infoList = case.select('td')

    if infoList[0].getText() == "조회결과가 없습니다.":
        print('조회결과가 없습니다.')
    else:
        number = str(infoList[0].getText())  # 의안번호
        title = infoList[1].select('a')[0].get('title')  # 의안명
        who = infoList[2].getText()  # 제안자구분
        when_start = str(infoList[3].getText())  # 제안일
        where = infoList[4].select('a')[0].get('title')  # 소관위
        when_end = str(infoList[5].getText())  # 의결일자
        result = infoList[6].getText()  # 의결결과

        print(number, title, who, when_start, where, when_end, result)
