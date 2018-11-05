# ================================#
# 달빛학사 분실물 게시판을 읽으면서
# 'ㅠ'나 'ㅜ'가 들어간 게시물을
# 연도별로 분류함.
# 조건: 글 제목이나 내용에 'ㅜ' 혹은 'ㅠ' 가 들어있는가?
# ================================#


# 모듈 import
from bs4 import BeautifulSoup as bs
import requests
import matplotlib.pyplot as plt


# pip install matplotlib


# url의 html코드를 반환
def get_html_text(sess, url):
    page = sess.get(url)
    # http 코드를 받아 200(ok)가 아닐 경우 에러 raise
    page.raise_for_status()
    return page.text


# 글이 올라온 시점에서 딕셔너리를 업데이트
def update_dict(time, target_dict):
    if time not in target_dict:
        target_dict.update({time: 1})
    else:
        # 글의 개수 +1
        target_dict[time] += 1


# requests.Session()을 사용해 페이지에 로그인
def login_function(sess, info):  # Session을 유지하기 위해 매개변수로 받음

    login_page = get_html_text(sess, 'https://go.sasa.hs.kr/auth')
    login_soup = bs(login_page, 'html.parser')
    # 로그인을 위해 csrf 코드를 받음
    csrf = login_soup.find('input', {'name': 'csrf_test_name'})
    info.update({'csrf_test_name': csrf['value']})

    # 로그인 시도
    login_req = sess.post('https://go.sasa.hs.kr/auth/login', data=info)

    # 로그인 실패시 오류 raise
    if login_req.status_code != 200:
        raise Exception('Login Error!')


# 로그인에 사용되는 정보
# 사용자가 직접 입력해야함
LOGIN_INFO = {
    'id': 'MY_ID',
    'passwd': 'MY_PASSWORD'
}

# 조건에 맞는 글의 수를 연도별로 저장하는 dictionary
Tdict = {}
# 전체 글의 수를 저장하는 dictionary
# 나중에 Tdict를 allDict로 나눠 조건에 맞는 글의 비율을 구할 것
allDict = {}

# 현재 페이지
count = 25

while True:
    # 로그인 상태 유지를 위한 Session
    sess = requests.Session()
    # 특정 시간이나 요청 횟수가 지나면 로그인이 풀리는듯 해서 매번 다시 로그인함
    login_function(sess, LOGIN_INFO)

    # 현재 분실물 페이지
    current_page = get_html_text(sess, 'https://go.sasa.hs.kr/board/lists/2/page/%d' % count)
    soup = bs(current_page, 'html.parser')
    # 글 제목 리스트
    title_list = soup.select('div.box-body tbody tr')

    # 글 제목 리스트가 비어있으면 모든 게시판을 다 본것이므로 탐색 종료
    if not title_list:
        break

    # 글 제목을 하나씩 훑으면서
    for title in title_list:

        # 실제 글 제목
        text = title.find('a').getText().strip().split('\n')[0]
        try:
            # 글이 올라온 시간
            time = title.find('time').getText().strip().split()[0].split('-')
            time = int(time[0])
            # 전체 글 수를 담는 딕셔너리 업데이트
            update_dict(time, allDict)

        # 글 작성 시간이 표시되지 않는 게시물이 몇개 있음
        # 달빛학사 오류인듯 함
        except IndexError:
            # print(text)
            pass

        # 글 링크
        link = title.find('a').get('href')

        # 만약 글 제목이 조건에 맞는다면
        if 'ㅠ' in text or 'ㅜ' in text:
            # 딕셔너리 업데이트하고 다음 글로 continue
            update_dict(time, Tdict)
            continue
        # 아니라면
        else:
            # 글 내용이 조건에 맞는지 확인
            url = "https://go.sasa.hs.kr" + link

            new_page = get_html_text(sess, url)
            new_soup = bs(new_page, 'html.parser')
            # 간혹 글에 첨부파일 등이 있는 글이 있는데, 이 글도 div.box-body 안에 들어있어서
            # select_one함수를 이용해 첫번째 텍스트만 받아옴
            text = new_soup.select_one('div.content-wrapper section.content div.box-body').getText().strip()

            # 만약 글 내용이 조건에 맞는다면
            if 'ㅠ' in text or 'ㅜ' in text:
                # 딕셔너리 업데이트하고 다음 글로 continue
                update_dict(time, Tdict)
                continue

    # print(count, Tdict)
    print('현재 게시판:' + str(count))
    # 다음 게시판으로 가기 위해 count++
    count += 1

# 그래프 x축:시간
keys = Tdict.keys()
# 조건에 맞는 글 수
Tvalues = list(Tdict.values())
# 전체 글 수
Avalues = list(allDict.values())
# 조건에 맞는 글의 비율 구하기
values = []
for i in range(len(Tvalues)):
    values.append(Tvalues[i] / Avalues[i] * 100)
    print("%d년: %d%%" % (list(keys)[i], values[i]), end=' ')

# matplotlib.pyplot을 사용해 꺾은선그래프로 묘사
plt.plot(keys, values)
plt.show()
