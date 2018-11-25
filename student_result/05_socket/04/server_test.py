import socket
import threading

server_ip = '127.0.0.1'  # self ip
server_port = 50000  # 변경 가능한지 확인할 것
address = (server_ip, server_port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)  # 주소를 받아 접속 대기 상태
server_socket.listen()  # 입력 대기 상태 , 클라이언트로부터 입력 가능

# 클라이언트 목록
client_list = []
client_id = {}

# 필터링 문장 목록
warning_list = ['I hate Python',
                'Java is better than Python', 'Python is rubbish']

# 접속자의 표기 아이디 입력 함수


def set_name(client_socket, num):
    global client_list
    global client_id

    client_socket.send(b"Welcome to my server. What's your nickname?")
    try:
        # 바이트 타입으로 이름을 받는다
        name = client_socket.recv(1024)
    # 만약 연결이 안되는 경우
    # 해당 접속자의 정보를 삭제하고 리턴
    except ConnectionError:
        print("{} nothing input".format(client_socket))
        client_list.remove[client_socket]
        return 0

    # 닉네임을 넘버링한 수에 대응하여 client_id 저장
    client_id[num] = name

# 접속자로부터 데이터를 받는 함수


def from_client(client_socket, num):
    global client_list
    global client_id

    while True:
        try:
            # 바이트 타입으로 데이터를 받는다
            data = client_socket.recv(1024)
        except ConnectionError:
            # 접속 오류시 break
            print("{} has disconnected".format(client_id[num]))
            break

        # 입력한 문장이 필터링 목록에 있으면
        # 접속자와의 연결을 끊는다.
        for i in warning_list:
            if data.decode('utf-8') == i:
                client_socket.send(b"you cannot use those words.")
                del client_id[num]
                client_list.remove(client_socket)
                client_socket.shutdown(socket.SHUT_RD)
                return 0

        #!quit를 입력받으면 메세지를 중지한다
        if not data:
            print("{} required disconnection".format(client_id[num]))
            client_socket.send(
                bytes("Server is going to remove your profile", 'utf-8'))
            break

        # 접속자를 제외한 나머지 접속자들에게 메세지를 출력
        for i in client_list:
            if i != client_socket:
                i.send(client_id[num]+b": "+data)

    # 메세지 전송이 끝나면 접속자를 제거
    print("id {}, {} has normally disconnected".format(
        client_id[num], client_socket))
    del client_id[num]
    client_list.remove(client_socket)
    client_socket.close()
    return 0

# 서버를 연결하는 함수


def connect():
    global client_list

    while True:
        # 임의의 클라이언트에 접속되면
        # 접속자의 socket정보를 client_list에 저장
        # 접속자를 임의의 넘버링으로 client_id에 저장
        client_socket, client_address = server_socket.accept()

        client_list.append(client_socket)
        num = client_socket.fileno()

        # 접속자의 이름을 묻는 스레드 생성
        thread_set_name = threading.Thread(
            target=set_name, args=(client_socket, num))
        thread_set_name.start()
        thread_set_name.join()

        # 접속이 완료되면 해당 접속자의 소켓 정보와 닉네임을 출력
        print("{} has connected".format(client_socket))
        print("id is {}" .format(client_id[num].decode('utf-8')))

        # 접속자가 메세지를 보낼 수 있는 스레드 생성
        thread_recv = threading.Thread(
            target=from_client, args=(client_socket, num))
        thread_recv.start()


# 서버 실행
thread_server = threading.Thread(target=connect, args=())
thread_server.start()

print("Server is running...")
thread_server.join()
server_socket.close()
