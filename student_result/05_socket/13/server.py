import threading
import socket

# Server setting
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

# Create socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
server_sock.bind(address)

# Listen
server_sock.listen()

client_list = []
client_id = []

print("Starting Kkutu!")
print("Waiting for players...({}/2)".format(len(client_list)))


# 서버로부터 메시지를 받는 함수 | Thread 활용
def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    while True:
        # 클라이언트로부터 데이터를 받는다.
        try:
            data = client_sock.recv(1024)
        except ConnectionError:
            print("{} connection dismissed. #code1".format(client_sock.fileno()))
            break

        # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
        if not data:
            print("{} connection dismiss request. #code0".format(
                client_sock.fileno()))
            client_sock.send(bytes("Deleting client information...", 'utf-8'))
            break

        # 데이터가 들어왔다면 접속하고 있는 모든 클라이언트에게 메시지 전송
        data_with_id = bytes(str(client_sock.fileno()), 'utf-8') + b":"+data
        for sock in client_list:
            if sock != client_sock:
                sock.send(data_with_id)

    # 메시지 송발신이 끝났으므로, 대상인 client는 목록에서 삭제.
    client_id.remove(client_sock.fileno())
    client_list.remove(client_sock)
    print("Currently connected users: {}\n".format(client_id), end='')
    # 삭제 후 sock 닫기
    client_sock.close()
    print("Successfully closed client socket.")
    print('#----------------------------#')
    return 0


def connection():
    global client_id
    global client_list

    while len(client_list) < 2:
         # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()

        # 연결된 정보를 가져와서 list에 저장함.
        # 몇 번째 플레이어인지 알려주기 (먼저 접속한 사람이 먼저 시작)
        client_sock.send(bytes(str(len(client_list)), 'utf-8'))
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{} connected.".format(client_sock.fileno()))
        print("{} connected.".format(client_addr))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock, ))
        thread_recv.start()

        if len(client_list) < 2:
            print("Waiting for players...({}/2)".format(len(client_list)))

    # 두 명이 모이면 게임 시작
    print("Game Started!")
    print("First letter starts with 'a'")


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== Kkutu Server ==============")

thread_server.join()
server_sock.close()
