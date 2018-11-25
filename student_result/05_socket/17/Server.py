"""
TIc Tac Toe Game을 두명이서 즐길 수 있는 코드이다.
Client1은 player1로 'O' 기호를 가지고 있으며, 먼저 시작한다.
Client2은 player2로 'X' 기호를 가지고 있으며, 나중에 시작한다.

"""

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
print('Start Chat - Server')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []
pos = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']

# 결과 판정하기
def ending():
    # 상하좌우 대각선 중 3개 모두 일치한 것이 있는지 판별하기(1,5,9 / 2,5,8 / 3,5,7 / 4,5,6)
    for i in range(1,5):
        if pos[5] == 'O' and pos[5+i] == 'O' and pos[5-i] == 'O':
            return 'O'
        elif pos[5+i] == 'X' and pos[5-i] == 'X' and pos[5] == 'X':
            return 'X'

    # 중심을 제외한 가장자리에서 일어날 수 있는 결과 중 3개 모두 일치하는 것이 있는지 판별하기(1,2,3 / 1,4,7 / 3,6,9 / 7,8,9)
    for i in (1, 9):
        for j in (3, 7):
            if pos[i] == 'O' and pos[j] == 'O' and pos[int((i+j)/2)] == 'O':
                return 'O'
            elif pos[i] == 'X' and pos[j] == 'X' and pos[int((i+j)/2)] == 'X':
                return 'X'

    temp = 0    # 1~9 위치 중 문자가 있으면 temp를 1 증가시켜, 모든 문자가 있고(temp==9) 끝나지 않았다면 비긴 결과를 출력하기
    for i in range(1,10):
        if pos[i] != ' ':
            temp += 1
    if temp == 9:
        return 'Draw'
    else:
        return 'NotEnd'

# 서버로 부터 메시지를 받는 함수 | Thread 활용
def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    global pos

    while True:
        # 클라이언트로부터 데이터를 받는다.
        try:
             data = client_sock.recv(1024)
            #data = input('>')
        except ConnectionError:
            print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
            break

        # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
        if not data:
            print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
            client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
            break

        info_arr = str(data).split(".")
        print(info_arr)
        mark = info_arr[1]
        position = info_arr[2]
        pos[int(position)] = mark

        # 데이터가 들어왔다면 접속하고 있는 모든 클라이언트에게 메시지 전송
        data_with_conf = '.'+ mark + '.' + position + '.OK. .'
        for sock in client_list:
            if sock != client_sock:
                sock.send(bytes(data_with_conf, 'utf-8'))
                #sock.send(data)

        winner = ending()
        print(winner)
        if winner != 'NotEnd':
            if winner == 'O':
                result = "....'O' is Winner!"
            elif winner == 'X':
                result = "....'X' is Winner!"
            elif winner == 'Draw':
                result = "....Draw"
            for sock in client_list:
                    sock.send(bytes(result, "utf-8"))


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
    global client_list, client_id
    count = 0
    while count <2:
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()
        print(client_sock)
        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        print("현재 연결된 사용자: {}\n".format(client_list))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock, ))
        thread_recv.start()

        count += 1

# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== Chat Server ==============")

thread_server.join()
server_sock.close()

