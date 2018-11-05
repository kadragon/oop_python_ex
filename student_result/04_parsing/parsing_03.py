# pip3 install -U beautifulsoup4
# pip3 install -U requests

import bs4
import requests

login_info = {
    'id': '',  # 달빛학사 id 입력
    'passwd': ''  # 달빛학사 비밀번호 입력
}

while True:
    song_good_list = list()  # 노래의 좋아요 숫자를 저장하는 리스트
    song_name_list = list()  # 노래의 이름을 저장하는 리스트
    song_is_good_list = list()  # 노래의 좋아요/취소 상태를 저장하는 리스트
    with requests.Session() as s:  # 로그인하는 Session
        first_page = s.get('https://go.sasa.hs.kr/')
        html_login = first_page.text
        soup_login = bs4.BeautifulSoup(html_login, 'html.parser')
        csrf = soup_login.find('input', {'name': 'csrf_test_name'})
        login_info.update({'csrf_test_name': csrf['value']})
        login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=login_info)
        if login_req.status_code != 200:
            raise Exception('로그인이 되지 않았습니다')

        # 달빛학사 음악추천 사이트의 정보를 가져와 BeautifulSoup로 가공
        song = bs4.BeautifulSoup(s.get('https://go.sasa.hs.kr/RcmndMusic/musicView').text, 'html.parser')
        song_good = song.select('td.text-center.text-info')  # 노래의 좋아요 숫자를 추출
        for i in song_good:
            song_good_list.append(i.getText().strip())  # 각 노래의 좋아요 숫자를 현재 순위별로 저장
        song_name = song.select('td')  # td 를 모두 추출
        song_is_good = song.select('td.text-center button')  # 노래의 좋아요/취소 상태를 추출
        for i in song_is_good:  # 각 노래의 좋아요/취소 상태를 현재 순위별로 저장
            song_is_good_list.append(i.getText().strip())
        cnt = -1
        while True:
            cnt += 1
            try:
                for i in song_name[2 + 6 * cnt]:  # td 안에서 노래 이름이 있는 위치에서 노래이름을 추출
                    song_name_list.append(song_name[2 + 6 * cnt].getText().strip())
            except IndexError:
                break
        for i in range(len(song_good_list)):  # 노래이름을 현재 순위대로 저장
            print('{}'.format(i + 1), end=' ')
            print(song_is_good_list[i], song_good_list[i], ': ', song_name_list[i * 3])
        button_info = song.select('button')  # 좋아요/취소와 관련된 정보 추출
        button_like_id = ['0']  # 좋아요를 누를 때 사용할 id 리스트
        button_unlike_id = ['0']  # 취소를 누를 때 사용할 id 리스트
        for i in button_info:
            t = i.get('id')  # 각 노래의 id 추출
            if t == None:  # 맨 첫번째줄 정보 버림
                continue
            button_like_id.append(t[4] + t[5] + t[6] + t[7])  # 좋아요의 경우 앞의 4글자를 버림
            if t[0] == 'l':
                button_unlike_id.append(t[0])  # indexerror 방지
            elif t[0] == 'u':
                button_unlike_id.append(t[6] + t[7] + t[8] + t[9])  # 싫어요의 경우 앞의 6글자를 버림
        print('좋아요를 누르시려면 1, 취소를 하시려면 2를 눌러주세요')
        print('그 외를 입력하시면 프로그램이 종료됩니다')
        check = input()  # 사용자의 행동 판정
        if check == '1':  # 좋아요를 누르는 경우
            print('좋아요를 누를 노래를 선택하세요')
            print('ex) 3')
            print('"exit"을 입력하면 프로그램이 종료됩니다')
            like = input()
            if like == 'exit':  # 탈출조건
                print('프로그램이 종료됩니다')
                break
            try:  # 입력오류 방지
                like = int(like)
            except ValueError:
                print('잘못된 입력입니다 다시 입력해주세요')
                continue
            if song_is_good_list[like - 1] == '취소':  # 이미 좋아요가 눌려있는 경우
                print('이미 좋아요 상태인 노래입니다')
                continue
            try:  # 좋아요를 누르는 Session
                first_page_1 = s.get('https://go.sasa.hs.kr/RcmndMusic/musicView')
                html = first_page_1.text
                soup = bs4.BeautifulSoup(html, 'html.parser')
                dict_1 = {'musicIdx': button_like_id[like], 'action': 'insert'}
                like_req = s.post('https://go.sasa.hs.kr/RcmndMusic/likeControl', data=dict_1)
                print('성공적으로 좋아요가 입력되었습니다')
            except IndexError:  # 잘못된 입력
                print('노래번호를 다시 확인해주세요')
                continue
        elif check == '2':  # 취소의 경우
            print('취소를 누를 노래를 선택하세요')
            print('ex) 3')
            print('"exit"을 입력하면 프로그램이 종료됩니다')
            unlike = input()
            if unlike == 'exit':  # 탈출조건
                print('프로그램이 종료됩니다')
                break
            try:  # 입력오류 방지
                unlike = int(unlike)
            except ValueError:
                print('잘못된 입력입니다 다시 입력해주세요')
                continue
            if song_is_good_list[unlike - 1] == '좋아요':
                print('이미 취소상태인 노래입니다')
                continue
            try:  # 취소를 누르는 Session
                first_page_1 = s.get('https://go.sasa.hs.kr/RcmndMusic/musicView')
                html = first_page_1.text
                soup = bs4.BeautifulSoup(html, 'html.parser')
                dict_1 = {'musicIdx': button_unlike_id[unlike], 'action': 'delete'}
                unlike_req = s.post('https://go.sasa.hs.kr/RcmndMusic/likeControl', data=dict_1)
                print('성공적으로 취소가 입력되었습니다')
            except IndexError:  # 잘못된 입력
                print('노래번호를 다시 확인해주세요')
                continue
        else:  # 종료조건
            print('프로그램이 종료됩니다')
            break
