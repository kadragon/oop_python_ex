import socket
import threading
import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library
import tkinter

# 접속할 서버의 정보
server_ip = '10.171.36.XXX'
server_port = 50000
address = (server_ip, server_port)

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)
print("connection complete")
print("If you want to leave chat, just type !quit\n")


def draw_board(board):
    window = tkinter.Tk()
    window.title("Time_Table")
    window.geometry("1285x673+100+10")
    window.resizable(False, False)

    for j in range(0, 12):
        for i in range(0, 6):
            if i == 0 and j == 0:
                t = tkinter.Button(window, text="시간표", height=3, width=10)
            elif i == 0:
                t = tkinter.Button(window, text="%d교시" % j, height=3, width=10)
            elif j == 0:
                if i == 1:
                    t = tkinter.Button(window, text="월요일", height=3, width=33)
                elif i == 2:
                    t = tkinter.Button(window, text="화요일", height=3, width=33)
                elif i == 3:
                    t = tkinter.Button(window, text="수요일", height=3, width=33)
                elif i == 4:
                    t = tkinter.Button(window, text="목요일", height=3, width=33)
                elif i == 5:
                    t = tkinter.Button(window, text="금요일", height=3, width=33)
            else:
                if board[i-1][j-1] == "-":
                    t = tkinter.Button(window, text="%s" %
                                       board[i - 1][j - 1], height=3, width=33)
                else:
                    t = tkinter.Button(
                        window, text="%s" % board[i - 1][j - 1], height=3, width=33, fg="blue", bg="skyblue")
            t.grid(row=j, column=i)

    window.mainloop()

# 서버로부터 메시지를 받아, 출력하는 함수.


def receive():
    global mysock
    while True:
        try:
            qoard = [['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', ''],
                     ['', '', '', '', '', '', '', '', '', '', '', ''], [
                         '', '', '', '', '', '', '', '', '', '', '', ''],
                     ['', '', '', '', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '']]
            for i in range(6):
                data = mysock.recv(2048)  # 서버로 부터 값을 받는것
                temp = data.decode('UTF-8')
                qoard[i] = temp.split(",")

        except ConnectionError:
            print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
            break

        if not data:  # 넘어온 데이터가 없다면.. 로그아웃!
            print("서버로부터 정상적으로 로그아웃했습니다.")
            break

        draw_board(qoard)

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
