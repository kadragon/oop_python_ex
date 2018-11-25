"""server에 client가 접속해서 server에서 객관식 문제를 하나 제출하면
시간 제한 안에 client가 답을 입력해서 정답, 오답 여부를 client에게 알려주는 프로그램입니다."""

import socket, threading

#접속할 서버 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

#서버 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#서버 접속이 안되는 경우 예외 처리
try:
    mysock.connect(address)
#서버가 안 열렸다면
except ConnectionRefusedError:
    #서버 열리지 않았다고 출력 후
    print("서버가 아직 열리지 않았습니다. 잠시 뒤에 시도해주시기 바랍니다.")
    #프로그램 종료
    exit(0)

print("서버와 연결되었습니다")
print("곧 서버로부터 객관식 퀴즈가 발송될 것입니다! 열심히 맞춰주세요!")

# 서버로부터 메시지를 수신하는 함수
def receive():
    global mysock
    while True:
        #서버로부터 값 receive
        try:
            data = mysock.recv(1024)
        #예외 처리
        except ConnectionError:
            print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
            break
        if not data:
            print("서버로부터 정상적으로 로그아웃했습니다.")
            break

        #sever로부터 받은 정보 decode해서 출력
        print(data.decode('UTF-8'))  # 서버로 부터 받은 값을 출력

    print('소켓의 읽기 버퍼를 닫습니다.')
    mysock.shutdown(socket.SHUT_RD)


#server에게 메세지 발신
def main_thread():
    global mysock

    #메세지 수신 thread 생성 및 실행
    thread_recv = threading.Thread(target=receive, args=())
    thread_recv.start()

    while True:
        try:
            data = input()
        #예외 처리
        except KeyboardInterrupt:
            continue
        try:
            mysock.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
        #예외 처리
        except ConnectionError:
            break

    print("소켓의 쓰기 버퍼를 닫습니다.")
    mysock.shutdown(socket.SHUT_WR)
    thread_recv.join()


#메세지 발신하는 thread 생성 및 실행
thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()

thread_main.join()

mysock.close()
print('소켓을 닫습니다.')
print('클라이언트 프로그램이 정상적으로 종료되었습니다.')
