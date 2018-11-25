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

# 아이디의 입력을 기다려주세요...
# 스레딩으로 반환값을 받지 못해 id입력을 순서대로 기다립니다
print("Pleas wait unitl [Welcome to my server. What's your nickname?] printed")

# 서버로부터 메시지를 받아, 출력하는 함수.


def receive():
    global mysock
    while True:
        try:
            # 서버로부터 데이터를 수신
            data = mysock.recv(1024)
        except ConnectionError:
            # 연결 오류시 종료
            print("You has disconnected")
            break
        except OSError:
            print("You disconnected with server")
            break

        if not data:  # 넘어온 데이터가 없다면.. 로그아웃!
            print("You logout from server")
            break

        print(data.decode('UTF-8'))  # 서버로 부터 받은 값을 출력

    try:
        mysock.shutdown(socket.SHUT_RD)
    except OSError:
        print("Server has closed before reaing buffer closed")


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
            print("disconnecting from server...")
            break

        try:
            mysock.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
        except ConnectionError:
            break

    print("closing writting buffer")
    mysock.shutdown(socket.SHUT_WR)
    thread_recv.join()


# 메시지 보내는 스레드 시작
thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()

# 메시지를 받고, 보내는 스레드가 종료되길 기다림
thread_main.join()

# 스레드가 종료되면, 열어둔 소켓을 닫는다.
mysock.close()
print("Closing socket")
