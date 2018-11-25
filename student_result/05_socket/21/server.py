'''

'''

import socket
import threading

print('''
2018.11.05
DataBase Server Server Code by YoungKeun Jung

socket과 threading을 이용하여 텍스트파일을 공유할 수 있는 서버 구축

server 측에서는 server를 initialize 할 때 password를 설정하여 client의 접근을 제한 할 수 있다.
client 측에서는 LOAD 메소드를 이용하여 Server의 database에 있는 파일에 접근할 수 있고
SAVE 메소드를 이용하여 Server의 database에 새로운 데이터를 업로드 할 수 있다.

''')

print('Initializing Server')

myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

password = input('Input Server Access Password >> ')

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()

print('SERVER ACTIVE')

client_list = []
client_id = []

database = {'Introduction':'Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace.', 'Developer':'Guido van Rossum'}
def send_data(client_sock, data):
    try:
        client_sock.send(bytes(data, 'utf-8'))
    except ConnectionError:
        print("Lost Connection with {}.".format(client_sock.fileno()))


def response(client_sock):
    global database
    send_data(client_sock, password)

    while True:
        try:
            rec = client_sock.recv(1024)

            if rec.decode('UTF-8') == 'LOAD':
                send = ''
                for keys in list(database):
                    send = send + keys + '\n'
                send_data(client_sock, send)
                try:
                    rec = client_sock.recv(1024)
                    try:
                        send_data(client_sock, database[rec.decode('UTF-8')])
                    except KeyError:
                        send_data(client_sock, 'KeyError: Try it Again')
                except ConnectionError:
                    print("Lost Connection with {}.".format(client_sock.fileno()))
                    break

            elif rec.decode('UTF-8') == 'SAVE':
                try:
                    name = client_sock.recv(1024)
                    contents = client_sock.recv(1024)
                    database[name.decode('utf-8')] = contents.decode('utf-8')
                    #print(name.decode('utf-8'))
                    #print(contents.decode('utf-8'))
                    #print(database)
                except ConnectionError:
                    print("Lost Connection with {}.".format(client_sock.fileno()))
                    break
        except ConnectionError:
            print("Lost Connection with {}.".format(client_sock.fileno()))
            break


    #print(send)

    # 메시지 송발신이 끝났으므로, 대상인 client는 목록에서 삭제.
    client_id.remove(client_sock.fileno())
    client_list.remove(client_sock)
    #print("현재 연결된 사용자: {}\n".format(client_id), end='')
    # 삭제 후 sock 닫기
    client_sock.close()
    print("클라이언트 소켓을 정상적으로 닫았습니다.")
    print('#----------------------------#')
    return 0

# 연결 수립용 함수 | Thread 활용
def connection():
    global client_list
    global client_id
    global database

    while True:
        client_sock, client_addr = server_sock.accept()

        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{} Logged in.".format(client_addr))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=response, args=(client_sock,))
        thread_recv.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

thread_server.join()
server_sock.close()