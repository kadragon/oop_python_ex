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
print('릴레이 소설방 - open')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []
relay_list = []

# 작성된 소설들을 저장할 공간
relay_nv = []
latest_nv = []

# 현재 누구 차례인지
turn = 0

# 연결 수립용 함수


def connection():
    global client_list
    global client_id

    while True:
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()

        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}님이 접속하였습니다.".format(client_sock.fileno()))
        print("현재 연결된 사용자: {}\n".format(client_id))

        # 다른 접속자들에게 새로운 접속자를 알림, 새로운 접속자에게는 현재 상황을 알려줌.
        for sock in client_list:
            if sock != client_sock:
                sock.send(
                    bytes('-'*15+"> {}님이 참여합니다!".format(client_sock.fileno()), 'utf-8'))


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

while True:
    # 진행 중 임을 알림
    for writer in client_list:
        writer.send(bytes("----------> 소설이 진행중입니다.\n", 'utf-8'))

    # 5턴으로 이루어진 릴레이 소설을 순서대로 돌아가며 작성
    while turn < 20:
        turn += 1
        try:
            this_turn = turn % len(client_list)
        except ZeroDivisionError:
            this_turn = 0

        for writer in client_list:
            # 이번 턴인 사람에게서 내용을 받아들이고, 다른 사람들에게는 작성중임을 알림.
            if this_turn == client_list.index(writer):
                for w in client_list:
                    if client_list.index(w) != client_list.index(writer):
                        w.send(bytes("{}번째 작성자의 차례입니다.\n{}님이 작성중입니다...".format(this_turn + 1, writer.fileno()),
                                     'utf-8'))

                # 작성자를 위한 안내 문구
                writer.send(bytes("이전 내용 : {}".format(latest_nv), 'utf-8'))
                writer.send(bytes("당신의 차례입니다... 이어질 내용을 작성해주세요.", 'utf-8'))

                # 작성자로부터 내용 수신
                try:
                    data = writer.recv(1024)
                except ConnectionError:
                    print("{}님과 연결이 끊겼습니다.".format(writer.fileno()))
                    client_id.remove(writer.fileno())
                    client_list.remove(writer)
                    print("현재 연결된 사용자: {}\n".format(client_id), end='')
                    # 삭제 후 sock 닫기
                    writer.close()
                    print("클라이언트 소켓을 정상적으로 닫았습니다.")
                    print('#----------------------------#')
                    data = False

                # 만약 클라이언트로부터 종료 요청이 온다면, 종료함.
                if data == '!quit':
                    print("{}이 연결 종료 요청을 합니다.".format(writer.fileno()))
                    client_id.remove(writer.fileno())
                    client_list.remove(writer)
                    print("현재 연결된 사용자: {}\n".format(client_id), end='')
                    # 삭제 후 sock 닫기
                    writer.close()
                    print("클라이언트 소켓을 정상적으로 닫았습니다.")
                    print('#----------------------------#')

                elif data:
                    # 작성을 완료하였을 경우 소설에 추가
                    relay_nv.append(data.decode('utf-8'))
                    latest_nv = data.decode('utf-8')

                    # 작성자가 작성을 완료함을 다른 접속자들이게 알림
                    for other in client_list:
                        if client_list.index(other) != this_turn:
                            other.send(
                                bytes("{}님이 작성을 완료하였습니다.".format(writer.fileno()), 'utf-8'))

    else:
        # relay_nv에 저장된 내용을 문자열로 들어 전송
        for writer in client_list:
            writer.send(bytes("----------> 소설이 마무리 되었습니다.", 'utf-8'))
            result = ''
            for i in relay_nv:
                result = result + '\n' + i
            writer.send(bytes(result, 'utf-8'))
        turn = 0
        relay_nv = []
        latest_nv = []


thread_server.join()
server_sock.close()
