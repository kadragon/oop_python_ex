# 서버 코드입니다.
import socket
import threading
print('술래잡기 게임입니다. 서버를 실행 후 Client 1, 2를 연결해 주세요.\nw, a, s, d로 조종하며, 각 방향 입력 후 엔터를 쳐서 서버로 송신해 주세요.\n게임은 두 명이 모두 서버에 접속한 순간 부터 시작해주십시오. 미리 이동시 두 플레이어간 맵이 동기화되지 않습니다.\n술래 1이 도망자 2를 잡게 되면 게임이 종료되고 바로 다음 게임이 시작됩니다.')

# 서버 설정 저장
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

# 서버 open
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()

# 접속한 클라이언트들을 저장한다
client_list = []
client_id = []


# 서버로 부터 이동정보를 받는다. | Thread 활용한다.
def receive(client_sock):
    global client_list
    while True:
        try:
            data = client_sock.recv(1024)
        except ConnectionError:
            print("{}와의 연결 종료".format(client_sock.fileno()))
            break
        # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
        if not data:
            print("{}에서 연결 종료를 요청을 합니다.".format(client_sock.fileno()))
            client_sock.send(bytes("서버에서 클라이언트 정보를 삭제 중입니다.", 'utf-8'))
            break

        # 데이터 입력 시  데이터를 보낸 접속하고 있는 모든 클라이언트에게 메시지 전송
        data_with_id = bytes(str(client_sock.fileno()), 'utf-8') + b":" + data
        for sock in client_list:
            if sock != client_sock:
                sock.send(data_with_id)

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
        if len(client_list) >= 2:
            break
        client_sock, client_addr = server_sock.accept()
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        print("현재 연결된 사용자: {}\n".format(client_list))
        thread_recv = threading.Thread(target=receive, args=(client_sock,))
        thread_recv.start()


thread_server = threading.Thread(target=connection, args=())
thread_server.start()

thread_server.join()
server_sock.close()
