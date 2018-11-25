#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import threading

# 서버의 설정값을 저장
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)
num = ['1','2','3','4']
result = {'1':0 , '2':0 , '3':0, '4':0}

# 서버를 연다.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
print('Start Chat - Server')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []


# 서버로 부터 메시지를 받는 함수 | Thread 활용
def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
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
        D = str(data.decode('UTF-8'))
        if D in num:
            result[D]=result[D]+1
            print(result)
            break
        else:
            client_sock.send(bytes("형식에 맞지 않습니다. 다시 투표해 주세요", 'utf-8'))
            

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
        client_sock.send(bytes("투표=====================================\n",'UTF-8'))
        client_sock.send(bytes("1. -----\n",'UTF-8'))
        client_sock.send(bytes("2. -----\n",'UTF-8'))
        client_sock.send(bytes("3. -----\n",'UTF-8'))
        client_sock.send(bytes("4. -----\n",'UTF-8'))
        client_sock.send(bytes("위의 말 중 하나를 골라 번호를 입력하세요",'UTF-8'))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock, ))
        thread_recv.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== 투표 프로그램 ==============")

thread_server.join()

server_sock.close()


# In[ ]:




