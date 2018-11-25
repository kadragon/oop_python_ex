# -*- coding:utf-8 -*-

import socket
import threading

# 서버의 설정값을 저장
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

# 서버를 연다.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
print('Start Korean Spelling Test - Server')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []

# 한글 맞춤법에서 단어 차원의 오류 문제들
problems_and_answers = [('그녀는 지난 주말에 긴 머리를 (싹뚝) 잘랐어.', '싹둑'), ('아침 (등교길)에 친구를 만났어.', '등굣길'), ('오늘은 (왠지) 기분이 무척 좋아.', '왠지'), ('저도 내년이면 수험생이 (돼요).', '돼요'), ('밥을 먹었다. (그리고는) 물을 마셨다.', '그러고는/그리고'), ('두 살배기가 아주 말을 잘하(데).', '데'), ('주머니 사정도 (넉넉치) 않아.', '넉넉지'), ('(다행이도) 얼마 지나지 않아 그가 돌아왔다.', '다행히도'), ('우리의 간절한 (바램)은 그가 무사히 돌아오는 것이었다.', '바람'), ('많은 독자들에게 (읽혀지는) 책이다.', '읽히는'), ('그날 처음 내 눈에 (띠었던) 것은 강아지였다.', '띄었던'), ('아이는 (금새) 조용해졌다.', '금시에'), ('어떤 길을 (가던지) 간에 오르막길이 있으면 내리막길이 있기 마련이다.', '가든지'),
                        ('나는 내 말투에 대한 문제점을 (고칠려고) 노력했다.', '고치려고'), ('그를 (오랫만에) 만난다.', '오랜만에'), ('넌 왜 이리 (주책없니)?', '주책없니'), ('이 자리를 (빌어) 심심한 감사의 말씀을 드립니다.', '빌려'), ('이 엘리베이터는 (각층마다) 서지 않습니다.', '층마다/각 층에'), ('학생회 (임원으로써) 최선을 다할 것입니다.', '임원으로서'), ('저는 찬성측의 입장에서 의견을 (말했었습니다).', '말했습니다'), ('인문학적 소양이란 치열한 질문으로부터 출발한다. 이 질문은 언제나 세계에 대한 비판적 (관념)과 분석을 필요로 한다.', '관점/인식/생각'), ('그 대학이 과학기술 분야에서 명문인 것은 (여태까지) 훌륭한 과학 인재를 배출해냈다는 사실만 보아도 잘 알 수 있다.', '지금까지'), ('오늘 친구들과 (까페)에 갔다.', '카페'), ('친구의 생일을 축하하기 위해 (케이크)를 샀다.', '케이크')]

# 클라이언트와 메시지를 주고 받는 함수 | Thread 활용


def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    global problems_and_answers
    num = 0  # 문제 번호

    while True:
        try:
            problem = str(num+1) + ". " + problems_and_answers[num][0]
            client_sock.send(bytes(problem, 'UTF-8'))  # 클라이언트에 메시지를 전송
        except (ConnectionError, IndexError):
            break
        else:
            # 클라이언트로부터 데이터를 받는다.
            try:
                data = client_sock.recv(1024)
            except ConnectionError:
                print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
                break

            # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
            if not data:
                print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
                client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
                break

            data = data.decode('utf-8')
            if data in problems_and_answers[num][1].split('/'):
                client_sock.send(bytes("정답!", 'utf-8'))
            else:
                client_sock.send(
                    bytes("답 : " + problems_and_answers[num][1], 'utf-8'))
            num += 1

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

        # 접속한 클라이언트를 기준으로 메시지를 송신할 수 있는 스레드를 생성함.
        thread_transmit = threading.Thread(target=receive, args=(client_sock,))
        thread_transmit.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== Test Server ==============")

thread_server.join()
server_sock.close()
