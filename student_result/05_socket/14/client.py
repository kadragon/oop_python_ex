import socket, threading

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)
print("릴레이 소설방에 참가하였습니다.")
print("소설방을 떠나고 싶다면, 자신의 차례에 !quit 을 입력해주세요.\n")


# 서버에게 메시지를 발송하는 함수 | Thread 활용
def send():
    global mysock

    while True:
        try:
            data = input(' : ')
        except KeyboardInterrupt:
            continue

        if data == '!quit':
            print("서버와의 접속을 끊는 중입니다.")
            break

        try:
            mysock.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
        except ConnectionError:
            break

    print('소켓의 쓰기 버퍼를 닫습니다.')
    try:
        mysock.shutdown(socket.SHUT_RD)
    except OSError:
        print("읽기 버퍼를 닫기 전에 서버에서 연결이 종료되었습니다.")
    print("소켓의 읽기 버퍼를 닫습니다.")
    mysock.shutdown(socket.SHUT_WR)


# 서버로부터 메시지를 받아, 출력하는 함수.
def receive():
    global mysock

    # 메시지 보내는 스레스 시작
    thread_send = threading.Thread(target=send, args=())
    thread_send.start()

    while True:
        try:
            data = mysock.recv(1024)  # 서버로 부터 값을 받는것
        except ConnectionError:
            print("서버와 접속이 끊겼습니다.")
            break
        except OSError:
            print("서버와의 접속을 끊었습니다.")
            break

        print(data.decode('UTF-8'))  # 서버로 부터 받은 값을 출력


# 메시지 받는 스레드 시작
thread_recv = threading.Thread(target=receive(), args=())
thread_recv.start()

# 메시지를 받고, 보내는 스레드가 종료되길 기다림
thread_recv.join()

# 스레드가 종료되면, 열어둔 소켓을 닫는다.
mysock.close()
print('소켓을 닫습니다.')
print('클라이언트 프로그램이 정상적으로 종료되었습니다.')