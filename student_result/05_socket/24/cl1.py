import socket, threading

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)
print("공용 메모장 시스템입니다\n")
print("""메모장 번호는 0번부터 99번까지 있습니다.
처음 각 번호에는 'empty'가 기록되어 있습니다.
<사용 방법>
write/num/str : num번 메모지에 str을 기록합니다. 이미 기록된 내용이 있으면 덮어씁니다.
ex) write/14/Hello World!
당연한 사실이지만, 기록할 내용에 '/'가 포함되지 않도록 기록하셔야 합니다!!!
read/num : num번 메모지에 적힌 내용을 읽어옵니다.
ex) read/14
clear/num: num번 메모지를 empty로 초기화합니다.
ex) clear/14\n
그 외 명령어가 입력될 경우 아무 일도 일어나지 않습니다
""")
print("나가고 싶으시면 !quit 을 입력해 주시면 됩니다")



# 서버로부터 메세지 받기
def receive():
    global mysock
    while True:
        try:
            data = mysock.recv(1024)  # 서버로 부터 값을 받는것
        except ConnectionError:
            print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
            break
        except OSError:
            print("서버와의 접속을 끊었습니다.")
            break

        if not data:  # 넘어온 데이터가 없다면.. 로그아웃!
            print("서버로부터 정상적으로 로그아웃했습니다.")
            break

        print(data.decode('UTF-8'))  # 서버로 부터 받은 값을 출력

    print('소켓의 읽기 버퍼를 닫습니다.')
    try:
        mysock.shutdown(socket.SHUT_RD)
    except OSError:
        print("읽기 버퍼를 닫기 전에 서버에서 연결이 종료되었습니다.")


# 서버에게 메시지를 발송하는 함수 | Thread 활용
def main_thread():
    global mysock

    # 메시지 받는 스레스 시작
    thread_recv = threading.Thread(target=receive, args=())
    thread_recv.start()

    while True:
        try:
            data = input('>')
        except KeyboardInterrupt:
            continue

        if data == '!quit':
            print("서버와의 접속을 끊는 중입니다.")
            break

        try:
            mysock.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
        except ConnectionError:
            break

    print("소켓의 쓰기 버퍼를 닫습니다.")
    mysock.shutdown(socket.SHUT_WR)
    thread_recv.join()


# 메시지 보내는 스레드 시작
thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()

# 메시지를 받고, 보내는 스레드가 종료되길 기다림
thread_main.join()

# 스레드가 종료되면, 열어둔 소켓을 닫는다.
mysock.close()
print('소켓을 닫습니다.')
print('클라이언트 프로그램이 정상적으로 종료되었습니다.')