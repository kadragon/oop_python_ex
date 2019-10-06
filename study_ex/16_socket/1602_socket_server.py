import socket
import random
import threading

# 서버의 정보 설정
myip = '127.0.0.1'
myport = 50001
address = (myip, myport)

# 소켓을 활용하여 서버 열기
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()

print("===== 클라이언트 접속을 대기하는 중입니다.")
client_sock, client_addr = server_sock.accept()
print("===== 클라이언트가 접속하였습니다.")


# 클라이언트가 보내온 메시지를 받아 출력해주는 함수 | Thread로 돌릴 예정
def receive():
    global client_sock
    while True:
        try:
            data = client_sock.recv(1024)
            if data == '':
                break
        except OSError:
            print('연결이 종료되었습니다.')
            break

        print(data.decode('UTF-8'), " *from Client")
    client_sock.close()


# Thread 생성 및 실행
thread_recv = threading.Thread(target=receive, args=())
thread_recv.start()

# 메시지 전송 및 판단 client_sock 처리
while True:
    try:
        data = input('>')
    except KeyboardInterrupt:
        break
    if data == '!quit' or '':
        client_sock.close()
        break
    client_sock.send(bytes(data, 'UTF-8'))

# 서버 종료
server_sock.close()
