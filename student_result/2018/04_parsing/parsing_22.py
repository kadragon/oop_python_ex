from bs4 import BeautifulSoup as bs
import requests
print("이번 주의 신청 메뉴를 보여주는 코드입니다!!")
# 필요한 라이브러리 import

# 로그인이 사이트를 위한 데이터 저장
LOGIN_INFO = {
    'id': '아이디',
    'passwd': '비번'
}
# session 활용 로그인
with requests.Session() as s:
    # 목표 페이지에서 받아옴.
    page_text = s.get('https://go.sasa.hs.kr')
    html = page_text.text
    detail = bs(html, 'html.parser')
    print("...로그인 중...")
    csrf = detail.find('input', {'name': 'csrf_test_name'})
    LOGIN_INFO.update({'csrf_test_name': csrf['value']})
    login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)
    # 만약 로그인 에러시
    if login_req.status_code != 200:
        raise Exception('로그인 실패')
    print("...로그인 완료...")
    print("...데이터 받는 중...")
    # 급식 페이지를 html로 받아옴
    notice_board_data = bs(
        s.get('https://go.sasa.hs.kr/main/foodList').text, 'html.parser')
    # timeline-body에 목표 내용이 있기에 그 부분을 받아옴.
    notice_board_title = notice_board_data.find_all(class_='timeline-body')
    # 이 중 음식만 따로 뽑아냄.
    notice_board_title = str(notice_board_title).split('/')
    temp = list()
    final = list()
    print("...데이터 가공 중...")
    for i in notice_board_title:
        temp.extend((i.split('\n')))
    for i in temp:
        final.append(i.strip())
    temp = list()
    for i in final:
        if '<' in i:
            pass
        elif '>' in i:
            pass
        else:
            temp.append(i)
    final = list()
    # 음식들 중 신청된 것만 따로 뽑아냄.
    for i in temp:
        if '(' in i or ')' in i:
            final.append(i)
    print("이번 주의 신청 메뉴는", final, "입니다!!")
