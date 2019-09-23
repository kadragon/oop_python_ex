import socket
import threading
import random

# 윈도우 운영체제에서 cmd를 실행한 후 ipconfig 명령어로 IP address를 확인, 리눅스 운영체제에서 터미널을 실행 후 ifconfig 명령어 사용
myip = '192.168.101.145'
myport = 50000
address = (myip, myport)

# 소켓 설정
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
client_sock, client_addr = server_sock.accept()


# 랜덤으로 6개의 숫자를 반환
def choice():
    set1 = set()
    while len(set1) < 6:
        set1.add(random.choice(range(1, 46)))
    return set1


# 클라이언트의 접속을 대기, 접속한 클라이언트와 통신
# choice 함수에서 반환된 값을 클라이언트에 전송
while True:
    print("대기중...")
    print("Connection from {}".format(client_addr))
    client_sock.send(b"This is random int return Server. Welcome!")
    client_sock.send(bytes(str(choice()), 'utf-8'))
    client_sock.close()

# 통신 종료 및 소켓 닫음
server_sock.close()
