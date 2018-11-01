import socket
import random

# 1~100까지의 숫자중에 랜덤한 값을 돌려주는 함수
def choice():
    return random.randint(1, 100)

# 서버 설정 값
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

# 서버 열기
# 소켓을 사용하기 위해서, 소켓 객체를 만든다.
# Af_INET, SOCK_STREAM 은 socket에 선언되어 있는 상수
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)  # 위에 설정한 (ip, port)로 접속 대기
server_sock.listen()  # 입력을 받아드리는 상태로 대기


# 클라이언트의 접속을 대응하기 위해서 반복문 설정
while True:
    print("waiting for connection...")
    client_sock, client_addr = server_sock.accept()  # 클라이언트가 접속을 대기하다가 접속하면 정보를 가져옴.

    print("Connection from {}".format(client_addr))
    # 데이터를 전송할때에는 bytes 형태로 보내야 하기 때문에 변환하여 전송.
    client_sock.send(b"This is random int return Server. Welcome!")  # 1)
    client_sock.send(bytes(str(choice()), 'utf-8'))                  # 2)
    # 데이터 전송이 끝났으므로, 닫는다.
    client_sock.close()

# 열어놓은 서버 소켓을 닫는다.
server_sock.close()
