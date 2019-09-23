import socket
import threading
import random

# 서버의 설정값을 저장
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

# 서버를 연다.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
print('Start Word Scramble Server')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []
words = 'people history way art world information map tow family government health system computer meat year thanks music person reading method data food understanding theory law bird literature problem software control knowlegde power ability economics love internet television science library nature fact product idea temperature investment area society passable cultivator knitting trip audio acquire active oxford'.split()
# 총 47개의 단어를 무작위로
# 서버로 부터 메시지를 받는 함수 | Thread 활용


def receive(client_sock):
    while True:
        global success
        chk = True
        success = True
        while True:
            # 클라이언트로부터 데이터를 받는다
            word = ""
            if chk:
                num = random.randrange(1, len(words))
                word = words[num]
                list_word = list(word)
                random.shuffle(list_word)
                message = "".join(list_word)
                client_sock.send(bytes(message, 'utf-8'))
            chk = False
            try:
                data = client_sock.recv(1024)
            except ConnectionError:
                print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
                success = False
                break
            # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
            if not data:
                print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
                client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
                success = False
                break
            elif data.decode('utf-8') == 'again':
                chk = True
                continue
            elif data.decode('utf-8') == word:
                client_sock.send(bytes("정답입니다!", 'utf-8'))
                chk = True
            elif data.decode('utf-8') == 'answer':
                client_sock.send(bytes(word, 'utf-8'))
                chk = True
            else:
                client_sock.send(bytes('다시 도전해보세요!', 'utf-8'))
        if success == False:
            break

    # 메시지 송발신이 끝났으므로, 대상인 client는 목록에서 삭제.
    client_id.remove(client_sock.fileno())
    client_list.remove(client_sock)
    print("현재 연결된 사용자: {}\n".format(client_id), end='')
    # 삭제 후 sock 닫기
    client_sock.close()
    print("클라이언트 소켓을 정상적으로 닫았습니다.")
    print('#----------------------------#')
    return 0


# 연결 수립용 함수 | Thread 활용
def connection():
    global client_list
    global client_id

    while True:
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()

        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        print("현재 연결된 사용자: {}\n".format(client_list))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock,))
        thread_recv.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== World Scramble Server ==============")

thread_server.join()
server_sock.close()
