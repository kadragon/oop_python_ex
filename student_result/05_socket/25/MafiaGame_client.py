"""
Project     과제4|네트워킹|MafiaGame|Client
Date        2018.11.10.
"""
# 네트워킹을 이용하여 진행하는 마피아 게임
# random을 활용하여 마피아, 의사, 시민을 선택

# 동일한 파일에서 두 번 컴파일하게 되면 서버에 Error발생하므로
# 플레이를 할 경우에는 동일한 코드의 다른 파이썬 파일에서 실행해주세요

import socket
import sys
import time

# 접속하고자 하는 서버의 주소 및 포트
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

# 게임 플레이 인원 = 4 ~ 8명으로 제한하고 있음
# 게임 플레이 인원 변경시 client쪽 code에서도 수정해야 함
total = 4
textline = 30
first = True
myid = 0


def aboutWaiting(client_len):
    """
    게임 접속 현황에 대한 설명을 하는 함수
    :param: client_len :: 현재 접속자 수
    :param: total :: global 변수로 게임 플레이 인원을 의미
    """
    global total

    explain = "=" * textline + " 접속 현황 " + "=" * textline + "\n\n"
    explain += " 현재 접속자 : {}/{}명입니다\n".format(client_len, total)
    explain += " {}명이 모두 접속해야 게임을 시작할 수 있습니다\n\n".format(total)
    explain += "=" * (textline * 2 + 11) + "\n"
    print(explain)


def aboutGame():
    """
    게임에 대한 설명을 작성한 함수 (Server & Client)에게 동시 공지
    """
    explain = "=" * textline + " 게임 설명 " + "=" * textline + "\n\n"
    explain += " 지금부터 여러분들은 '마피아게임'을 하시게 됩니다\n"
    explain += " 여러분들이 지내시는 마을에는 마피아가 1명 의사가 1명 경찰이 1명\n"
    explain += " 그리고 그 외에는 전부 시민입니다\n"
    explain += " 힘을 합하여 모든 시민이 죽기 전에 마피아를 잡아주세요\n\n"
    explain += "=" * (textline * 2 + 11) + "\n"
    print(explain)


def receive():
    """
    서버로부터 메시지를 받는 함수
    """
    global first

    while True:
        try:
            # 전달되는 data의 속성에 따라 코드를 다르게 하여 진행함
            data = mysock.recv(1024).decode('utf-8')
        except ConnectionError:
            print(">> 서버와 접속이 끊겼습니다. Enter를 눌러주세요")
            break
        except OSError:
            print(">> 서버와의 접속을 끊었습니다")
            break

        if not data:
            print(">> 서버가 준비되지 않은 상태입니다")
            break

        if data[1:4] == '5-1':  # [#5-1]:접속자와 관련된 안내
            print(data[5:])
            if first == True:
                myid = data[5:8]
                first = False
        elif data[1:4] == '5-2':  # [#5-2]:접속자 수에 대한 안내
            aboutWaiting(data[5:])  # aboutWaiting() 함수를 통해 접속자와 관련된 정보를 제공
        elif data[1] == '0':  # [#0]: 게임 시작에 대한 안내
            print(data[3:])
            aboutGame()  # aboutGame() 함수를 통해 게임에 대한 설명을 제공
        elif data[1] == '1':  # [#1]: 게임 캐릭터에 대한 안내
            print("> 당신[ {} ]의 캐릭터는 [ {} ]입니다!\n".format(
                myid, data[3:]))  # 본인의 id와 캐릭터를 알려주고 있음
        elif data[1] == '2':  # [#2]: 접속자 전체 안내
            print(data[3:])
        elif data[1] == '4':  # [#4]: 입력이 필요한 안내
            while True:
                select = input(' [ 입력 ]>')
                if select != '':
                    mysock.send(bytes(select, 'utf-8'))
                    break
        elif data[1] == '3':  # [#3]: 특정 접속자에게 보내는 안내
            print(data[3:])
        elif data[1] == '7':  # [#7]: 접속자 프로그램 종료 요청
            break


# socket을 이용해서 접속 할 준비
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect(address)
except ConnectionRefusedError:  # 서버와 연결이 되지 않는 경우에 ConnectionRefusedError 발생
    print(">> 서버오류입니다. 나중에 다시 시도해주십시오")
else:
    receive()
finally:
    mysock.close()
    sys.exit()
