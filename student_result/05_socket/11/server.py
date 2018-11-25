import socket
import threading
import random

# 서버의 설정값을 저장
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)
connect = True
subject = ['논리적 글쓰기', '영어독해와 작문', '정치경제', '미적분학 I', '확률과 통계', '일반물리학 II', '일반물리학실험 II', '물리첨단기기활용법', '객체지향프로그래밍', '고급알고리즘', '체육 IV']
subject = subject[random.randint(0, len(subject)-1)]
number = random.randint(1, 3)
cnt = 0

# 서버를 연다.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
print('서버 오픈!')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []


# 서버로 부터 메시지를 받는 함수 | Thread 활용
def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    global cnt
    while True:
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

        # 데이터가 들어왔다면 접속하고 있는 모든 클라이언트에게 메시지 전송
        if data.decode('UTF-8') == subject:
            if cnt < number:
                cnt += 1
                client_sock.send(bytes("성공! %d등입니다!" % cnt, 'utf-8'))
            else:
                client_sock.send(bytes("늦었습니다! 다음에 다시!", 'utf-8'))
        else:
            client_sock.send(bytes("잘못 입력했습니다!", 'utf-8'))

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
    global connect

    while True:        
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()

        # 늦게 들어온 클라이언트는 연결을 끊음.
        if not connect:
            client_sock.send(bytes("입장이 마감되었습니다!", 'utf-8'))
            client_sock.close()
            return
        
        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        print("현재 연결된 사용자: {}\n".format(client_list))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock, ))
        thread_recv.start()


# 서버가 'Start!'를 입력하면 추가 연결을 제한함.
def start():
    global connect
    global subject
    global number
    while True:
        if input() == 'Start!':
            break
    print('=========== 수강신청 시작합니다! ===========')
    connect = False

    for sock in client_list:
        sock.send(bytes("지금 신청하는 과목은 {}입니다!\n".format(subject), 'utf-8'))
        sock.send(bytes("신청하실 분은 '{}'을 입력하세요!\n".format(subject), 'utf-8'))
        sock.send(bytes("선착순 {}명입니다. 시작!\n".format(number), 'utf-8'))
                  
    


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

thread_start = threading.Thread(target=start, args=())
thread_start.start()

thread_server.join()
server_sock.close()
