

import socket
import sys

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

print('''
2018.11.05
DataBase Server Server Code by YoungKeun Jung

socket과 threading을 이용하여 텍스트파일을 공유할 수 있는 서버 구축

server 측에서는 server를 initialize 할 때 password를 설정하여 client의 접근을 제한 할 수 있다.
client 측에서는 LOAD 메소드를 이용하여 Server의 database에 있는 파일에 접근할 수 있고
SAVE 메소드를 이용하여 Server의 database에 새로운 데이터를 업로드 할 수 있다.

''')


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
pw = input('INPUT PASSWORD TO GAIN ACCESS >> ')
# 서버로부터 메시지를 받아, 출력하는 함수.
try:
    data = mysock.recv(1024)  # 서버로 부터 값을 받는것
    if data.decode('UTF-8') == pw:
        print('ACCESS GRANTED')
        while True:
            user_in = input('\nSELECT MODE (LOAD/SAVE) OR !QUIT TO EXIT >> ')
            if user_in == '!QUIT':
                mysock.shutdown(socket.SHUT_RD)
                sys.exit()

            elif user_in == 'LOAD':
                send_data(mysock, 'LOAD')
                try:
                    data = mysock.recv(1024)
                    print('Files::')
                    print(data.decode('UTF-8'))
                    user_in = input('''INPUT FILE NAME TO IMPORT>> ''')
                    send_data(mysock, user_in)
                    try:
                        data = mysock.recv(1024)
                        print(data.decode('UTF-8'))
                    except ConnectionError:
                        print("CONNECTION ERROR")
                        sys.exit()
                except ConnectionError:
                    print("CONNECTION ERROR")
                    sys.exit()

            elif user_in == 'SAVE':
                send_data(mysock, 'SAVE')
                f_name = input('INPUT FILE NAME >> ')
                f_contents = input('INPUT FILE CONTENTS >> ')
                send_data(mysock, f_name)
                send_data(mysock, f_contents)
                print('SAVE SUCCESSFUL')

    else:
        print('ACCESS DENIED')
        sys.exit()
except ConnectionError:
    print("CONNECTION ERROR")
    sys.exit()

mysock.shutdown(socket.SHUT_RD)


# 스레드가 종료되면, 열어둔 소켓을 닫는다.
mysock.close()
print('소켓을 닫습니다.')
print('클라이언트 프로그램이 정상적으로 종료되었습니다.')
