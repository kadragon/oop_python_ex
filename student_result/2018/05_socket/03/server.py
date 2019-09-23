import socket
import threading

my_ip = "127.0.0.1"
my_port = 51742

client_list = []
client_id = []
partition = {}


def chat(client_sock):
    global client_list
    global client_id
    global partition

    status = 0

    while status == 0:
        client_sock.send(bytes(repr(tuple(partition.keys())), 'utf-8'))
        print("\r{}에게 채팅방 정보를 전송했습니다.\n\n> ".format(
            client_sock.fileno()), end='')

        try:
            data = client_sock.recv(1024)
        except ConnectionError:
            print("\r{}과(와) 연결이 끊겼습니다.".format(client_sock.fileno()))
            break
        if data == b'!quit':
            print("\r{}이(가) 연결을 종료했습니다.".format(client_sock.fileno()))
            client_sock.send(bytes("!pauseReceiving", 'utf-8'))
            break
        selected_partition = data.decode('utf-8')
        if selected_partition not in partition:
            partition.setdefault(selected_partition, [])
            print("\r{}이(가) {} 채팅방을 생성했습니다.".format(
                client_sock.fileno(), selected_partition))
        partition[selected_partition].append(client_sock.fileno())
        print("{}이(가) {} 채팅방에 들어갔습니다.".format(
            client_sock.fileno(), selected_partition))
        print("현재 연결된 사용자: {}".format(client_id))
        print("현재 생성된 채팅방과 사용자: {}\n\n> ".format(partition), end='')

        while True:
            try:
                data = client_sock.recv(1024)
            except ConnectionError:
                print("\r{}과(와) 연결이 끊겼습니다.".format(client_sock.fileno()))
                status = 1
                break

            if data == b'!quit':
                print("\r{}이(가) 연결을 종료했습니다.".format(client_sock.fileno()))
                client_sock.send(bytes("!pauseReceiving", 'utf-8'))
                status = 1
                partition[selected_partition].remove(client_sock.fileno())
                break
            if data == b'!leave':
                print("\r{}이(가) {} 채팅방을 나갑니다.".format(
                    client_sock.fileno(), selected_partition))
                client_sock.send(bytes("!pauseReceiving", 'utf-8'))
                partition[selected_partition].remove(client_sock.fileno())
                print("현재 연결된 사용자: {}".format(client_id))
                print("현재 생성된 채팅방과 사용자: {}\n\n> ".format(partition), end='')
                break

            data_with_id = bytes(str(client_sock.fileno()),
                                 'utf-8') + b" : " + data
            for sock in client_list:
                if sock != client_sock and sock.fileno() in partition[selected_partition]:
                    sock.send(data_with_id)
            print("\r{}이(가) {} 채팅방에 메시지를 전송했습니다.\n\n> ".format(
                client_sock.fileno(), selected_partition), end='')

    client_list.remove(client_sock)
    client_id.remove(client_sock.fileno())
    client_sock.close()
    print("현재 연결된 사용자: {}".format(client_id))
    print("현재 생성된 채팅방과 사용자: {}\n\n> ".format(partition), end='')


def connect():
    global client_list
    global client_id
    global partition

    while True:
        client_sock, client_address = server_sock.accept()

        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("\r{}이(가) 접속하였습니다.".format(client_sock.fileno()))
        print("주소 : {}".format(client_address))
        print("현재 연결된 사용자: {}".format(client_id))
        print("현재 생성된 채팅방과 사용자: {}\n\n> ".format(partition), end='')

        thread_chat = threading.Thread(target=chat, args=(client_sock, ))
        thread_chat.start()


def get_command():
    global client_id
    global partition

    while True:
        command = input('> ')
        if command == '?' or command == 'help':
            print("=" * 80)
            print("도움말")
            print("=" * 80)
            print("help : 이 창을 띄워 줍니다.")
            print("- 사용법 : 'help'")
            print("status : 현재 연결된 사용자와 생성된 채팅방, 그 안의 사용자를 출력합니다.")
            print("- 사용법 : 'status'")
            print("tell : 특정 채팅방에 관리자 메시지를 전송합니다.")
            print("- 사용법 : 'tell <채팅방 이름> <메시지>'")
            print("=" * 80)
        elif command == 'status':
            print("현재 연결된 사용자: {}".format(client_id))
            print("현재 생성된 채팅방과 사용자: {}\n".format(partition))
        elif command.split(' ')[0] == 'tell':
            chosen_partition = command.split(' ')[1]
            string = "ADMIN : " + ' '.join(command.split(' ')[2:])
            for sock in client_list:
                if sock.fileno() in partition[chosen_partition]:
                    sock.send(bytes(string, 'utf-8'))
            print("{} 채팅방에 관리자 메시지를 전송했습니다.\n".format(chosen_partition))
        else:
            print("명령어가 존재하지 않습니다.\n")


my_address = (my_ip, my_port)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(my_address)
server_sock.listen()
print("채팅 서버 시작")
print("명령어 도움말을 보고 싶으시면 help를 입력하세요.\n")

thread_server = threading.Thread(target=connect, args=())
thread_command = threading.Thread(target=get_command, args=())
thread_server.start()
thread_command.start()

thread_server.join()
thread_command.join()

server_sock.close()
