import socket
import threading
import time

# 서버 정보, 전역변수 선언
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)
flag = 1
endflag = 1
answer = ''

# 서버 소켓 개방
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
print('Start Quiz Server')

# server와 client 연결
client_sock, client_addr = server_sock.accept()


# 프로그램 종료하는지 결정하는 함수
def end_judge():
    global endflag
    global client_sock
    while True:
        if endflag == 0:
            client_sock.close()
            break


# client에게 문제와 시간제한 출력하는 함수
def send():
    global client_sock
    global flag
    global ans
    # 문제 입력 받기
    problem = input("write problem ")
    number1 = input("what is number1? ")
    number2 = input("what is number2? ")
    number3 = input("what is number3? ")
    ans = input("what is answer? ")  # 답 입력 받기

    # client에게 보낼 문자열 생성
    send_problem = problem+"\n1. "+number1+"\n2. "+number2+"\n3. "+number3
    send_problem = bytes(send_problem, 'utf-8')

    # client에게 문제 send
    client_sock.send(send_problem)

    time.sleep(1)
    # 시간 제한 client에게 send
    client_sock.send(bytes("10초 남았습니다", 'utf-8'))
    time.sleep(4)

    # 시간제한 10초
    for i in range(1, 6):
        time.sleep(1)
        client_sock.send(bytes("%d초 남았습니다." % (6-i), 'utf-8'))

    client_sock.send(bytes("끝!", 'utf-8'))
    flag = 0

# 정답, 오답 판별하는 함수


def judge():
    global flag
    global answer
    global ans
    global endflag

    while True:
        if flag == 0:  # 시간 제한 끝났고
            if answer == ans:  # sever에서 입력한 답과 client가 입력한 답이 같다면
                client_sock.send(bytes("두근두근두근두근", 'utf-8'))
                time.sleep(3)
                client_sock.send(bytes("정답입니다!", 'utf-8'))  # 정답입니다! 출력
                endflag = 0
                break
            else:  # 나머지 경우에는
                client_sock.send(bytes("두근두근두근두근", 'utf-8'))
                time.sleep(3)
                client_sock.send(bytes("오답입니다..", 'utf-8'))  # 오답입니다.. 출력
                endflag = 0
                break

# 답 입력받는 함수


def receive(client_sock):
    global ans
    global answer
    thread_send = threading.Thread(target=send, args=())  # send thread 생성 및 실행
    thread_send.start()
    thread_judge = threading.Thread(
        target=judge, args=())  # judge thread 생성 및 실행
    thread_judge.start()
    thread_end_judge = threading.Thread(
        target=end_judge, args=())  # end_judge thread 생성 및 실행
    thread_end_judge.start()

    while flag:  # 시간 제한 안 지났을 경우는
        try:
            data = client_sock.recv(1024)  # client가 보낸 메세지 받음
        # 예외 경우 처리
        except ConnectionError:
            print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
            break
        if not data:
            print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
            client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
            break
        # 사용자가 입력한 답 decode
        answer = data.decode('UTF-8')

    # 소켓 닫기
    client_sock.close()
    print("클라이언트 소켓을 정상적으로 닫았습니다.")
    print('#----------------------------#')
    return 0


# receive thread 생성 밍 실행
thread_recv = threading.Thread(target=receive, args=(client_sock, ))
thread_recv.start()

thread_recv.join()
server_sock.close()
