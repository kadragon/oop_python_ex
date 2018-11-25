"""
Title       죄수의 딜레마 게임 Client
Date        2018.11.11
"""

import socket, threading

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)
turn = 1  # 서버로부터 결과가 오지 않았는데 입력할 경우 이를 막아주는 변수. 1일 때 입력 가능

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)

# Rule 설명
print("죄수의 딜레마 게임에 오신 것을 환영합니다. 게임에 관한 규칙을 간단히 설명해 드리겠습니다."
      "\n당신은 공범과 함께 범죄를 저질렀습니다. 저기 어딘가에 있는 공범 역할을 한 누군가도 다음과 같은 규칙으로 게임을 하고 있습니다."
      "\n첫 번째. 당신은 <자백> 과 <침묵>의 두 가지 선택지를 선택할 수 있습니다."
      "\n **** <자백> 선택지를 선택하려면 confess를 입력하고, <침묵> 선택지를 선택하려면 silent를 입력하면 됩니다. ****"
      "\n두 번째. 게임을 끝내고 싶으면, !quit을 입력한다."
      "\n세 번째. 공범의 선택과 나의 선택에 따라 나와 공범에게 떨어지는 형량이 결정됩니다. "
      "\n(자백 - 자백) : 둘 다 징역 3년, (침묵 - 침묵) : 둘 다 징역 1년, (자백 - 침묵) : 자백 - 집행 유예, 침묵 - 징역 10년."
      "\n게임은 무한히 진행되므로, 상대방의 반응에 따라 적절히 행동하시면 됩니다."
      "\n\n\n"
      "자 그럼 게임을 시작하겠습니다. Enter 키를 누르시면 시작합니다.")

# 서버로부터 메시지를 받아, 출력하는 함수.
def receive():
    global mysock
    global turn  # 전역변수 turn
    while True:
        chk = True  # 입력하지 않았는데 처음에 "다시 플레이합니다"라는 문구가 뜨는 것 방지용. 플레이했으면 False
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
        if int(data.decode('utf-8')) == -1:
            print('당신은 집행 유예입니다. 최상의 결과에요!')
            chk = False
        elif int(data.decode('utf-8')) == 2:
            print('당신은 징역 1년입니다. 나쁘지 않네요.')
            chk = False
        elif int(data.decode('utf-8')) == 3:
            print('당신은 징역 3년입니다. 좋지는 않군요...')
            chk = False
        elif int(data.decode('utf-8')) == 10:
            print('당신은 징역 10년입니다. 최악의 결과군요.')
            chk = False
        if not chk:
            print('다시 플레이합니다.'
                  '\n>')
            turn = 1

    print('소켓의 읽기 버퍼를 닫습니다.')
    try:
        mysock.shutdown(socket.SHUT_RD)
    except OSError:
        print("읽기 버퍼를 닫기 전에 서버에서 연결이 종료되었습니다.")


# 서버에게 메시지를 발송하는 함수 | Thread 활용
def main_thread():
    global mysock
    global turn  # 전역변수 turn
    # 메시지 받는 스레드 시작
    thread_recv = threading.Thread(target=receive, args=())
    thread_recv.start()

    while True:
        input_error = False  # 입력이 잘 못 되었을 때
        try:
            data = input('>')
        except KeyboardInterrupt:
            continue
        if data == '!quit':
            print("서버와의 접속을 끊는 중입니다.")
            break
        # 입력이 잘 되었을 경우
        if data.lower() == 'confess' or data.lower() == 'silent':
            pass
        # 입력이 잘 되지 않았을 경우
        else:
            if not turn:
                print('잠시만 기다리세요. 상대방이 아직 선택하지 않았습니다.')
            else:
                print('입력이 뭔가 잘못되었습니다. 다시 확인해주세요.')
            input_error = True
        # 입력이 잘 되었을 때
        if not input_error:
            # 전역변수 turn을 이용해 입력해도 되는 시점인지 check. turn = 1이면 입력 가능하고, 입력된 데이터를 Server로 보내고 turn = 0으로 바꿈
            if turn:
                turn = 0
                try:
                    mysock.send(bytes(data.lower(), 'utf-8'))
                except ConnectionError:
                    break
            else:
                print('잠시만 기다리세요. 상대방이 아직 선택하지 않았습니다.')
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