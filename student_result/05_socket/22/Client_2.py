# Client 2, 즉 도망치는 자의 코드입니다, 함수에 주어지는 인자가 (1->2, 2->1)으로 바뀐것을 제외하면 client1과 동일합니다.
import socket
import threading
import sys
import time
from os import system

init_map = [[0]*10 for i in range(20)]
init1 = [0, 0]
init2 = [19, 9]


def init_game():
    time.sleep(3)
    print("게임을 다시 시작합니다.")
    global init1, init2
    init1 = [0, 0]
    init2 = [19, 9]
    map_print(init1, init2)


def mover(to, pl):
    place = [0, 0]
    global init1, init2
    if pl == 1:
        place = init1
    else:
        place = init2
    if to == 'w':
        if place[1] >= 1:
            place[1] = place[1]-1
    if to == 'a':
        if place[0] >= 1:
            place[0] = place[0]-1
    if to == 's':
        if place[1] <= 8:
            place[1] = place[1]+1
    if to == 'd':
        if place[0] <= 18:
            place[0] = place[0]+1
    return place


def map_print(p1, p2):
    print("\n")
    if init1 == init2:
        print("술래[1]이 잡았습니다!! 승리했습니다.")
        now_map = [[0] * 10 for i in range(20)]
        now_map[p1[0]][p1[1]] = 1
        for i in range(0, 10):
            for j in range(0, 20):
                print(now_map[j][i], end=' ')
            print('')
        init_game()
    else:
        now_map = [[0] * 10 for i in range(20)]
        now_map[p1[0]][p1[1]] = 1
        now_map[p2[0]][p2[1]] = 2
        for i in range(0, 10):
            for j in range(0, 20):
                print(now_map[j][i], end=' ')
            print('')


# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect(address)
except ConnectionRefusedError:
    print("연결이 거부됐습니다. 서버의 문제 또는 최대 플레이어 수를 초과했습니다.")
    sys.exit()

print("connection complete")
print("If you want to leave chat, just type !quit\n")

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
        global init1, init2
        init1 = mover((data.decode('UTF-8')).split(':')[1], 1)
        map_print(init1, init2)

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

        if data == '!quit':
            print("서버와의 접속을 끊는 중입니다.")
            break

        try:
            mysock.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
            global init1, init2
            init2 = mover(data, 2)
            map_print(init1, init2)
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
