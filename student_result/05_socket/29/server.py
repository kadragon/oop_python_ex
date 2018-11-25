import socket
import threading
import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library

LOGIN_INFO = {
    'id': '',
    'passwd': ''
}

# 서버의 설정값을 저장
myip = '10.171.36.218'
myport = 50000
address = (myip, myport)

# 서버를 연다.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
print('Start Chat - Server')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []


def find_teacher(name):
    with requests.Session() as s:
        # 로그인 페이지를 가져와서 html 로 만들어 파싱을 시도한다.
        first_page = s.get('https://go.sasa.hs.kr')
        html = first_page.text
        soup = bs(html, 'html.parser')

        # cross-site request forgery 방지용 input value 를 가져온다.
        # https://ko.wikipedia.org/wiki/사이트_간_요청_위조
        csrf = soup.find('input', {'name': 'csrf_test_name'})

        # 두개의 dictionary 를 합친다.
        LOGIN_INFO.update({'csrf_test_name': csrf['value']})

        # 만들어진 로그인 데이터를 이용해서, 로그인을 시도한다.
        login_req = s.post(
            'https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)
        get_timetable = s.get(
            'https://go.sasa.hs.kr/timetable/search_new/teacher?target='+name, data={'target': ''}).text
        timetable_soup = bs(get_timetable, 'html.parser')
        qmp = timetable_soup.select('script')
        qmp = str(qmp).split('\n')
        qmp = list(qmp)
        qmp2 = []
        qmp3 = []
        qoard = [['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], [
            '', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '']]
        for i in qmp:
            if "tar = " in i:
                qmp2.append(i)
            if "$('#time" in i:
                qmp2.append(i)

        for i in qmp2:
            if "tar = " in i:
                i = i.split('"')[1].replace("<br />", " / ").split(" / ")[0:3]
                qmp3.append(i)
            if "$('#time" in i:
                if "append(tar)" in i:
                    i = i.split("'")[1].replace("#time", "").split("-")
                    qmp3.extend(i)
                else:
                    i = i.split("'")[4:0:-3]
                    i[0] = i[0].replace(">", "").replace('</button");', "")
                    qre_i = i[1].replace("#time", "").split("-")
                    i[1] = qre_i[0]
                    i.append(qre_i[1])
                    qmp3.extend(i)
        for i in range(0, len(qmp3), 3):
            qoard[int(qmp3[i+1])-1][int(qmp3[i+2])-1] = qmp3[i]
        return qoard


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text

# 서버로 부터 메시지를 받는 함수 | Thread 활용


def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    while True:
        # 클라이언트로부터 데이터를 받는다.
        try:
            data = client_sock.recv(2048)
            name = data.decode('UTF-8')
            qoard = find_teacher(name)
        except ConnectionError:
            print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
            break

        # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
        if not data:
            print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
            client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
            break

        # 데이터가 들어왔다면 접속하고 있는 모든 클라이언트에게 메시지 전송
        for sock in client_list:
            if sock == client_sock:
                for i in range(0, 6):
                    for j in range(0, 12):
                        if type(qoard[i][j]) == list:
                            qoard[i][j] = qoard[i][j][2]
                        elif qoard[i][j] == "":
                            qoard[i][j] = "-"
                for i in range(0, 6):
                    strr = ",".join(qoard[i])
                    sock.send(bytes(strr, 'UTF-8'))

    # 메시지 송발신이 끝났으므로, 대상인 client는 목록에서 삭제.
    client_id.remove(client_sock.fileno())
    client_list.remove(client_sock)
    print("현재 연결된 사용자: {}\n".format(client_id), end='')
    # 삭제 후 sock 닫기
    client_sock.close()
    print("클라이언트 소켓을 정상적으로 닫았습니다.")
    print('#----------------------------#')
    return 0


# 연결 수립용 함수 | Thread 활용
def connection():
    global client_list
    global client_id

    while True:
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()

        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        print("현재 연결된 사용자: {}\n".format(client_list))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock,))
        thread_recv.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== Chat Server ==============")

thread_server.join()
server_sock.close()
