'''
덧셈 퀴즈 _ 서버
'''
import socket
import threading
import random

# 서버의 설정값을 저장
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)
# 서버를 연다.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
print('Start Quiz - Server')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []


def send_data(client_sock, data):
    try:
        client_sock.send(bytes(data, 'utf-8'))
    except ConnectionError:
        print("Lost Connection with {}.".format(client_sock.fileno()))
        sys.exit()


def question(sock):

    numA = random.randint(1, 100000)
    numB = random.randint(1, 100000)
    ans = int(numA) + int(numB)
    numdata = bytes((str(numA) + " + " + str(numB) + " = "), 'utf-8')
    sock.send(numdata)
    data = ''

    while True:
        try:
            data = sock.recv(1024)
            # print(data)
            # print(ans)
            if data.decode('UTF-8') == str(ans):
                send_data(sock, 'Right')
                break
            else:
                send_data(sock, 'wrong')
        except ConnectionError:
            print("{}와 연결이 끊겼습니다. #code1".format(sock.fileno()))


# 서버로 부터 메시지를 받는 함수 | Thread 활용
def receive(client_sock):

    for i in range(10):
        question(client_sock)

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

        #print("{}가 접속하였습니다.".format(client_sock.fileno()))
        #print("{}가 접속하였습니다.".format(client_addr))
        print("현재 연결된 사용자: {}\n".format(client_list))
        # start()
        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock, ))
        thread_recv.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== Chat Server ==============")
