# 클라이언트 코드
import socket, threading

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)
print("서버와 연결되었습니다.")
print("준비된 문제를 모두 맞추면 게임이 종료됩니다")
print("친구보다 먼저 맞춰봐요!\n")
print("종료하고 싶으시면 quit이라고 입력해주세요.")
print("게임을 시작하고 싶으시면 start라고 입력해주세요.")
print("친구의 플레이가 종료되지 않았는데 start를 눌러주시는 것은 지양해주세요.")
print("시작한 후 다시 start를 입력하시면 새로운 문제가 로드됩니다.\n")
print("당신의 ID 입니다!")

# 서버로부터 메시지를 받아, 출력하는 함수.
def receive():
    global mysock
    while True:
        try:
            data = mysock.recv(1024)  # 서버로 부터 값을 받는것
        except ConnectionError:
            print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
            break

        if not data:  # 넘어온 데이터가 없다면.. 로그아웃!
            print("서버로부터 정상적으로 로그아웃했습니다.")
            break

        print(data.decode('UTF-8'))  # 서버로 부터 받은 값을 출력

    print('소켓의 읽기 버퍼를 닫습니다.')
    mysock.shutdown(socket.SHUT_RD)


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

        if data == 'quit':
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
