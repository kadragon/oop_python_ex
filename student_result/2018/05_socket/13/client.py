import socket
import threading

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)
print("connection complete")
print("If you want to leave chat, just type !quit\n")
print("First letter is 'a'")

# 마지막으로 끝난 단어
last_char = 'a'
# 현재 턴 수
# 처음 들어온 사람은 매 짝수 턴마다,
# 나중에 들어온 사람은 매 홀수 턴마다 진행
turn = int(mysock.recv(1024).decode("UTF-8"))


# 서버로부터 메시지를 받아, 출력하는 함수.
def receive():
    global mysock
    global last_char
    global turn

    while True:
        try:
            data = mysock.recv(1024)  # 서버로 부터 값을 받는것
            try:
                # 마지막으로 끝난 단어
                last_char = data.decode('UTF-8')[-1]
            except:
                # 상대가 !quit하여 단어가 안 받아졌을 경우 pass
                pass
            print(last_char)
            turn += 1
        except ConnectionError:
            print("Connection dismissed. Press Enter")
            break
        except OSError:
            print("Connection dismissed.")
            break

        if not data:  # 넘어온 데이터가 없다면.. 로그아웃!
            print("Successfully logged out from server.")
            break

        print(data.decode('UTF-8'))  # 서버로 부터 받은 값을 출력

    print('Closing read buffer.')
    try:
        mysock.shutdown(socket.SHUT_RD)
    except OSError:
        print("Connection was lost before closing the read buffer.")


# 서버에게 메시지를 발송하는 함수 | Thread 활용
def main_thread():
    global mysock
    global turn
    global last_char

    # 메시지 받는 스레스 시작
    thread_recv = threading.Thread(target=receive, args=())
    thread_recv.start()

    while True:
        try:
            data = input('>')
        except KeyboardInterrupt:
            continue

        if data == '!quit':
            print("Dismissing connection...")
            break

        # 자기 턴일 때
        if turn % 2 == 0:
            # 시작하는 글자가 방금 전 마지막 글자가 아니라면 재시도
            if data[0] != last_char:
                print("Wrong word. Try again.")
                continue
            try:
                mysock.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
                turn += 1
            except ConnectionError:
                break

        else:
            print("Not your turn!")

    print("Dismissing connection...")
    mysock.shutdown(socket.SHUT_WR)
    thread_recv.join()


# 메시지 보내는 스레드 시작
thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()

# 메시지를 받고, 보내는 스레드가 종료되길 기다림
thread_main.join()

# 스레드가 종료되면, 열어둔 소켓을 닫는다.
mysock.close()
print('Socket closed.')
print('Client program had been successufully finished')
