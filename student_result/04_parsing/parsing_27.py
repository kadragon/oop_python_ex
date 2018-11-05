# pip install beautifulsoup4
# pip install requests

import sys
import datetime
import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
    'id': '',
    'passwd': ''
}

APP_INFO = {
    'nightDate': '',
    'nightTime': '',
    'uidT': '',
    'nightReason': '',
    'nightPlace': '',
    'with_student': ''
}

MESSAGE_INFO = {
    'recvList': '',
    'message': ''
}

REQ_message = "선생님, 기타지도 신청 승인해주세요!"    # 승인 요청
WAIT_message = "선생님, 기숙사에 기타지도 승인 연락해주시면 안될까요?"    # 대기 상태

def guidance_list():
    print("-" * 90)
    print("<지도 리스트>")
    print("  지도일    |   지도장소   |   지도시간   |  지도교사  |   승인   |   삭제   |  추가정보")

    for i in guide_list:
        each_list = i.select('td')
        cnt = 0
        for j in each_list:
            cnt += 1
            if cnt == 7:
                print(j.getText().strip().center(8))
            elif cnt == 1:
                print("%s  |"%j.getText().strip(), end='')
            elif cnt == 3:
                print("%s|"%j.getText().strip().center(15), end='')
            else:
                var = j.getText().strip()
                if len(var)%2 == 0:
                    print("%s|"%j.getText().strip().center(8), end='')
                else:
                    print("%s|" % j.getText().strip().center(9), end='')
    print("-"*90)

with requests.Session() as s:
    LOGIN_stat = 0
    while LOGIN_stat == 0:
        try:
            print("달빛학사 ID와 Password를 입력해주세요.")
            LOGIN_INFO['id'] = input("ID: ")
            LOGIN_INFO['passwd'] = input("Password: ")

            login_page = bs(s.get('https://go.sasa.hs.kr').text, 'html.parser')
            csrf = login_page.find('input', {'name': 'csrf_test_name'})
            LOGIN_INFO.update({'csrf_test_name': csrf['value']})
            login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)

            if login_req.status_code != 200:
                raise IndexError

            main_page = bs(s.get('https://go.sasa.hs.kr/main').text, 'html.parser')
            user = main_page.select('li.dropdown.user.user-menu a span')[0].getText()     # 이름(학번)
            print("현재 사용자는%s입니다."%user)

        except IndexError:
            print("로그인 되지 않았습니다!\n")

        else:
            LOGIN_stat = 1
            today = datetime.datetime.now()
            today = str(today).split()[0]

            GUIDE_APP_page = bs(s.get('https://go.sasa.hs.kr/night_Control/user').text, 'html.parser')
            guide_list = GUIDE_APP_page.select('div.col-md-9 table.table.table-bordered.table-hover tbody tr')

            current_time = datetime.datetime.now()
            current_time = str(current_time).split()[1].split('.')[0].split(':')[0:2]
            current_time = ''.join(current_time)

            guidance_list()

            if int(current_time) >= 1630:
                print("기타지도 신청시간이 지나 신청할 수 없습니다.")
                for i in guide_list:
                    each_list = i.select('td')
                    cnt = 0

                    for j in each_list:
                        cnt += 1
                        guide_info = j.getText().strip()
                        if cnt == 1:
                            guide_day = guide_info
                        elif cnt == 3:
                            guide_time = guide_info
                        elif cnt == 4:
                            guide_teacher = guide_info
                        elif cnt == 5:
                            approve_stat = guide_info

                    if guide_day == today:
                        if approve_stat == '대기':
                            print("오늘자 %s의 기타지도 신청이 대기 상태입니다."%guide_time)
                            re = ''
                            while re.startswith('Y') == False and re.startswith('N') == False:
                                re = input("%s 선생님께 기숙사에 기타지도 승인 연락을 요청하는 메시지를 보낼까요?(Y/N) "%guide_teacher).strip().upper()

                                if re.startswith('Y'):
                                    APP_INFO['uidT'] = guide_teacher
                                    SMS_page = bs(s.get('https://go.sasa.hs.kr/sms/main').text, 'html.parser')
                                    csrf = SMS_page.find('input', {'name': 'csrf_test_name'})
                                    MESSAGE_INFO.update({'csrf_test_name': csrf['value']})

                                    teacher_json = s.get("https://go.sasa.hs.kr/autocomplete/get_smsList?term=" + APP_INFO['uidT'])
                                    teacher_ID = teacher_json.text.split(',')[1].split('"')[3].split('_')[0]
                                    MESSAGE_INFO['recvList'] = teacher_ID + '_' + APP_INFO['uidT']

                                    MESSAGE_INFO['message'] = WAIT_message
                                    sms_req = s.post('https://go.sasa.hs.kr/sms/main', data=MESSAGE_INFO)

                                    if sms_req.status_code != 200:
                                        raise Exception('메세지가 전송되지 않았습니다!')

                                elif not re.startswith('N'):
                                    print("제대로 입력해주세요!")
                        else:
                            print("오늘자 %s의 기타지도 신청이 승인되었습니다."%guide_time)
            else:
                cnt = 0
                while True:
                    rep = ''
                    while rep.startswith('Y') == False and rep.startswith('N') == False:
                        rep = input("기타지도 신청을 할건가요?(Y/N) ").strip().upper()

                        if rep.startswith('Y'):
                            cnt += 1
                            res = ''
                            while res.startswith('Y') == False and res.startswith('N') == False:
                                res = input("기타지도 신청에 대한 설명을 보겠습니까?(Y/N) ").strip().upper()

                                if res.startswith('Y'):
                                    print("-"*70)
                                    print('"지도 신청일" (예): 2001-10-25')
                                    print("단, 지도 신청일은 1개씩만 입력하세요. ")
                                    print('"지도 시간" (예)')
                                    print("       야간 1교시 / 19:00~21:00 -> 1")
                                    print("       야간 2교시 / 21:30~23:30 -> 2")
                                    print("       야간 1,2교시 / 19:00~23:30 -> 3")
                                    print("       주말 주간 / 14:30~17:30 -> 4")
                                    print("       이외시간 -> 5")
                                    print("             지도 시간 입력 (예): 13:00~14:00")
                                    print("단, '이외시간'을 신청하면, 지도 시간 입력(형식 준수!!!)을 해야한다.")
                                    print('"동료" (예): 홍길동, 홍길순')
                                    print("단, 동료가 없으면 Enter 를 입력하세요.")

                                elif not res.startswith('N'):
                                    print("제대로 입력해주세요!")
                            print("-"*70)
                            print("지도 신청일, 지도 시간, 지도교사, 사유, 장소, 동료를 입력하세요.")

                            APP_INFO['nightDate'] = input("지도 신청일: ")
                            APP_INFO['nightTime'] = input("지도 시간: ")
                            if APP_INFO['nightTime'] == '5':
                                APP_INFO.update({'nightTime2': input("지도 시간 입력: ")})
                            APP_INFO['uidT'] = input("지도교사: ")
                            APP_INFO['nightReason'] = input("사유: ")
                            APP_INFO['nightPlace'] = input("장소: ")
                            APP_INFO['with_student'] = input("동료: ")

                            friends_list = APP_INFO['with_student'].replace(' ', '').split(',')
                            APP_INFO['with_student'] = ''

                            for i in friends_list:
                                friend_json = s.get("https://go.sasa.hs.kr/autocomplete/get_smsList?term=" + i)
                                friend_ID = friend_json.text.split(',')[1].split('"')[3].split('_')[0]
                                APP_INFO['with_student'] += friend_ID + '_' + i + ', '

                            GUIDE_APP_page = bs(s.get('https://go.sasa.hs.kr/night_Control/user').text, 'html.parser')
                            csrf = GUIDE_APP_page.find('input', {'name': 'csrf_test_name'})
                            APP_INFO.update({'csrf_test_name': csrf['value']})
                            app_req = s.post('https://go.sasa.hs.kr/night_Control/user', data=APP_INFO)

                            if app_req.status_code != 200:
                                raise Exception('기타지도 신청이 되지 않았습니다!')

                            student_ID = user.split('(')[1].split(')')[0]
                            student_name = user.split('(')[0].lstrip()

                            alert_page = bs(app_req.text, 'html.parser')
                            alert = alert_page.select('body div div.content-wrapper script')[0].getText().strip()
                            ALARM = "alert('"+student_ID+'_'+student_name+"는 중복 신청으로 제외 되었습니다.');"

                            if alert == ALARM:
                                print("*** %s_%s는 중복 신청으로 제외 되었습니다. ***"%(student_ID, student_name))
                            else:
                                print("-"*70)
                                re = ''
                                while re.startswith('Y') == False and re.startswith('N') == False:
                                    re = input("%s 선생님께 승인 요청 메시지를 보낼까요?(Y/N) "%APP_INFO['uidT']).strip().upper()

                                    if re.startswith('Y'):
                                        teacher_json = s.get("https://go.sasa.hs.kr/autocomplete/get_smsList?term=" + APP_INFO['uidT'])
                                        teacher_ID = teacher_json.text.split(',')[1].split('"')[3].split('_')[0]

                                        MESSAGE_INFO['recvList'] = teacher_ID + '_' + APP_INFO['uidT']
                                        MESSAGE_INFO['message'] = REQ_message
                                        SMS_page = bs(s.get('https://go.sasa.hs.kr/sms/main').text, 'html.parser')
                                        csrf = SMS_page.find('input', {'name': 'csrf_test_name'})
                                        MESSAGE_INFO.update({'csrf_test_name': csrf['value']})
                                        sms_req = s.post('https://go.sasa.hs.kr/sms/main', data=MESSAGE_INFO)

                                        if sms_req.status_code != 200:
                                            raise Exception('메세지가 전송되지 않았습니다!')

                                    elif not re.startswith('N'):
                                        print("제대로 입력해주세요!")

                        elif not rep.startswith('N'):
                            print("제대로 입력해주세요!")

                    GUIDE_APP_page = bs(s.get('https://go.sasa.hs.kr/night_Control/user').text, 'html.parser')
                    guide_list = GUIDE_APP_page.select('div.col-md-9 div.box-body tbody tr')

                    if cnt != 0:
                        guidance_list()

                    sys.exit(0)