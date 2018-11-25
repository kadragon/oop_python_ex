# -*- coding: utf-8 -*-
"""
Title       AIPaper (Client)
Author      ITSC (Taewon Kang)
Date        2018.11.07
"""

import socket, threading

# 접속할 서버의 IP, 포트 입력
ip = '127.0.0.1'
port = 50035
serv = (ip, port)

# 소켓을 이용해서 서버에 접속
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) 서버에 접속이 안됨을 가정하여 예외처리(try ~ except)
try:
    sck.connect(serv)
except ConnectionRefusedError:
    print('서버 상태를 확인하십시오.')
    exit()

print("============== AIPaper Client ==============")
print("연결이 완료되었습니다.")
print("만약 연결을 종료하고 싶다면, !quit 명령을 입력하세요.\n")
print("인공지능 논문 정보를 받으려면 aipaper 명령을 활용하시면 됩니다.")
print("매 입력마다 랜덤한 논문이 제시됩니다.\n")


# 서버로부터 메시지를 받아 출력
def receive():
    global sck
    while True:
        # 2) 서버에서 제대로 된 정보를 못 받아올것을 가정하여 예외처리(try ~ except)
        try:
            data = sck.recv(1024)  # 서버로부터 값 받기
        except ConnectionError:
            print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
            break
        except OSError:
            print("서버와의 접속을 끊었습니다.")
            break

        if not data:  # 넘어온 데이터가 없으면 로그아웃
            print("서버로부터 정상적으로 로그아웃했습니다.")
            break

        # print(data.decode('UTF-8'))
        dec = data.decode('UTF-8')
        try:
            a, b, c = dec.split('#')
        except ValueError:
            exit()

        print('=' * 50)
        print('읽어볼 만한 최신 인공지능 논문 추천') # 논문 정보 출력
        print('=' * 50)

        # 논문 정보를 아래와 같이 가공함
        year = 2000 + int(c[6:8])
        month = int(c[8:10])
        paper_title = a[8:]
        paper_authors = b[9:]
        paper_url = 'https://arxiv.org/pdf/' + c[6:16]

        # 논문 정보 출력
        print('논문 제목: ' + paper_title)
        print('논문 발표 년월: ' + str(year) + '년 ' + str(month) + '월')
        print('저자: ' + paper_authors)
        print('URL: ' + paper_url)

    print('소켓의 읽기 버퍼를 닫습니다.')
    try:
        sck.shutdown(socket.SHUT_RD)
    except OSError:
        print("읽기 버퍼를 닫기 전에 서버에서 연결이 종료되었습니다. !quit로 종료하십시오.")

def main_thread():
    global sck

    # 3) Thread를 활용하여 상호 교류가 가능하도록 구성
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
            sck.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
        except ConnectionError:
            break

    print("소켓의 쓰기 버퍼를 닫습니다.")
    try:
        sck.shutdown(socket.SHUT_WR)
    except OSError:
        exit()
    thread_recv.join()


# 메시지 보내는 스레드 시작
thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()

# 메시지를 받고 보내는 스레드가 종료되길 기다림
thread_main.join()

# 스레드가 종료되면 열어둔 소켓을 닫는다.
sck.close()
print('소켓을 닫습니다.')
print('클라이언트 프로그램이 정상적으로 종료되었습니다.')