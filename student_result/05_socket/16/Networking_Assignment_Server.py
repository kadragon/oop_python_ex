"""
Title       죄수의 딜레마 게임 Server
Date        2018.11.11
"""

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
print('Start Game Server')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []

# 각각의 클라이언트의 선택을 저장하는 리스트
client_q = []

# 각각의 클라이언트의 선택에 따라 형량을 return
def def_jingyouk(a, b):
    if a==1 and b==1:
        return [3, 3]
    elif a==1 and b==0:
        return [-1, 10]
    elif a==0 and b==1:
        return [10, -1]
    else:
        return [2, 2]

# 서버로 부터 메시지를 받는 함수 | Thread 활용
def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    global client_q
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

        # 만약 자백을 선택하면 client_q 리스트에 1을 append
        if data.decode('utf-8') == 'confess':
            client_q.append(1)
        # 침묵을 선택하면 0을 append
        else:
            client_q.append(0)
        # client_q 리스트가 2개의 원소를 가질 때 각각의 클라이언트에게 결과를 return.
        if len(client_q) == 2:
            jing = def_jingyouk(client_q[1], client_q[0])
            client_sock.send(bytes(str(jing[0]), 'utf-8'))
            for sock in client_list:
                if sock != client_sock:
                    sock.send(bytes(str(jing[1]), 'utf-8'))
            # 결과 return 후 client_q 리스트는 reset
            client_q = []



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

    while len(client_list) < 2:
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()

        # 연결된 정보를 가져와서 list에 저장함.
        client_sock.send(bytes(str(len(client_list)), 'UTF-8'))
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())
        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        # print("현재 연결된 사용자: {}\n".format(client_list))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock,))
        thread_recv.start()

        # 플레이어 입장 여부 확인
        if len(client_list) < 2:
            print('다른 플레이어를 기다리고 있습니다... (%d / 2)' % len(client_list))
        else:
            print('모든 플레이어 입장!')



# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== Game Server ==============")

thread_server.join()
server_sock.close()