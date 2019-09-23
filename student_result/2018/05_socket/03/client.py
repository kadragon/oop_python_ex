import socket
import threading

server_ip = '127.0.0.1'
server_port = 51742


def receive():
    global my_socket
    global status

    while True:
        try:
            data = my_socket.recv(1024)
        except ConnectionError:
            print("\r[@] 접속이 끊겼습니다. Enter를 누르세요.")
            status = 1
            break

        if data == b'!pauseReceiving':
            break

        print('\r' + data.decode('utf-8') + '\n>', end='')
        #print(data.decode('utf-8') + '\n> ', end='')


def send():
    global my_socket
    global status

    while True:
        try:
            data = input('> ')
        except KeyboardInterrupt:
            continue

        try:
            my_socket.send(bytes(data, 'utf-8'))
        except ConnectionError:
            break

        if data == '!quit':
            print("[@] 클라이언트 프로그램을 종료합니다.")
            status = 1
            break
        if data == '!leave':
            print("[@] 채팅방에서 나갑니다.")
            break


def enter():
    global my_socket

    while status == 0:
        print("[@] 클라이언트 프로그램을 종료하고 싶으시면 !quit을 입력하세요.\n")

        try:
            data = my_socket.recv(1024)
        except ConnectionError:
            print("\r[@] 접속이 끊겼습니다.")
            return
        partition_name = eval(data.decode('utf-8'))
        print("[@] 채팅방 목록")
        print('=' * 20)
        for i in partition_name:
            print(i)
        print('=' * 20)
        print("[@] 들어갈 채팅방을 입력하세요.")
        print("[@] 목록에 없는 이름을 입력하면 채팅방을 생성합니다.")

        while True:
            try:
                input_str = input('> ')
                break
            except KeyboardInterrupt:
                continue
        data = bytes(input_str, 'utf-8')
        try:
            my_socket.send(data)
        except ConnectionError:
            print("\r[@] 접속이 끊겼습니다.")
            break
        if input_str == '!quit':
            return

        print("\n[@] 다른 사람의 채팅이 올라오면 쓰던 내용은 사라집니다.")
        print("[@] 채팅방을 나가고 싶으시면 !leave를 입력하세요.")
        thread_send = threading.Thread(target=send, args=())
        thread_receive = threading.Thread(target=receive, args=())
        thread_send.start()
        thread_receive.start()

        thread_send.join()
        thread_receive.join()


server_address = (server_ip, server_port)

status = 0

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    my_socket.connect(server_address)
except ConnectionRefusedError:
    print("[@] 서버에 연결할 수 없습니다. 프로그램을 종료합니다.")
    quit()
print("[@] 서버에 연결되었습니다.\n")

enter()

my_socket.close()
print("[@] 클라이언트 프로그램이 정상적으로 종료되었습니다.")
