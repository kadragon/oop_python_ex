'''
덧셈 퀴즈 _ 클라이언트
'''
import socket
import sys

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

def send_data(client_sock, data):
    try:
        client_sock.send(bytes(data, 'utf-8'))
    except ConnectionError:
        print("Lost Connection with {}.".format(client_sock.fileno()))


# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect(address)
except ConnectionRefusedError:
    print("SERVER NOT ACTIVE")
    sys.exit()

print("CONNECTION COMPLETE")

# 서버로부터 메시지를 받아, 출력하는 함수.
for i in range(10):
    try:
        data = mysock.recv(1024)  # 서버로 부터 값을 받는것
        print(data.decode('UTF-8'))

        response = 'wrong'
        while response == 'wrong':
            send_data(mysock, input())
            try:
                data = mysock.recv(1024)  # 서버로 부터 값을 받는것
                print(data.decode('UTF-8'))
                response = data.decode('UTF-8')
            except ConnectionError:
                print("CONNECTION ERROR")
                sys.exit()

    except ConnectionError:
        print("CONNECTION ERROR")
        sys.exit()


mysock.shutdown(socket.SHUT_RD)




# 스레드가 종료되면, 열어둔 소켓을 닫는다.
mysock.close()
print('소켓을 닫습니다.')
print('클라이언트 프로그램이 정상적으로 종료되었습니다.')
