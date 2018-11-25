import socket, threading

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)
position = 0
marker = 'O'
ano_marker = 'X'
pos = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)
print("connection complete")
print("If you want to leave chat, just type !quit\n")

# 처음 시작 화면 출력하기(각 위치는 1~9의 숫자로 지정)
def display_intro():
    print('-'*50)
    print("""
        Let's Tic-Tac-Toe Game!
    Enter the coordinate with number.
    <The Coordinate of Each position> 
              1  |  2  |  3  
            -----------------
              4  |  5  |  6 
            -----------------
              7  |  8  |  9  
    """)
    print('-'*50)

# 현재 보드판 상황 출력하기
def display_board(position, mark):
    pos[int(position)] = mark
    print("""
      %c  |  %c  |  %c  
    ------------------
      %c  |  %c  |  %c  
    ------------------
      %c  |  %c  |  %c 
    """ %(pos[1], pos[2], pos[3], pos[4], pos[5], pos[6], pos[7], pos[8], pos[9]))
    pos[0]=' '

# 플레이어가 표식을 놓을 위치 입력받기
def get_value():
    try:
        a = int(input('Enter the position number: '))
        if a < 1 or a > 9:                                                  # 위치는 1~9의 숫자로 지정되어 있음
            print("Hey, you entered the wrong value! enter again!")
            return get_value()
        elif pos[a] != ' ':                                                 # 이미 표식이 있는 곳에 또 놓을 수 없도록 하기
            print("Hey, you can't put your marker there. enter again!")
            return get_value()
        else:
            return a
    except TypeError as e:                                                  # TypeError 발생시 e로 저장한 뒤 값 다시 받기
        print("Hey, you entered the wrong value! enter again!")
        return get_value()
    except ValueError as e:                                                 # ValueError 발생시 e로 저장한 뒤 값 다시 받기
        print("Hey, you entered the wrong value! enter again!")
        return get_value()

# 서버로부터 메시지를 받아, 출력하는 함수.
def receive():
    global mysock, turn, position, ano_marker, marker, ano_position
    while True:
        try:
            data = mysock.recv(1024)  # 서버로 부터 값을 받는것
            # data_with_conf = '.'+ mark + '.' + position + '.OK. .'
        except ConnectionError:
            print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
            break

        if not data:  # 넘어온 데이터가 없다면.. 로그아웃!
            print("서버로부터 정상적으로 로그아웃했습니다.")
            break

        info_arr = str(data).split(".")
        #print(info_arr)

        position = info_arr[2]

        turn = info_arr[3]
        result = info_arr[4]
        if result != ' ':
            print(result)
        display_board(position, ano_marker)
        # position = str(data).split(".")[1]
        # turn = str(data).split(".")[2]
        # marker = str(data).split(".")[3]
        # ano_marker = another(marker)
        # print(marker)
        # display_board(position, ano_marker)

    print('소켓의 읽기 버퍼를 닫습니다.')
    mysock.shutdown(socket.SHUT_RD)


# 서버에게 메시지를 발송하는 함수 | Thread 활용
def main_thread():
    global mysock, turn, marker, ano_marker, ano_position
    turn = 'OK'
    while True:
        try:
            senddata = get_value()
        except KeyboardInterrupt:
            continue

        if senddata == '!quit':
            print("서버와의 접속을 끊는 중입니다.")
            break

        try:
            if turn == "OK":
                display_board(senddata, marker)
                data = '.'+ marker +'.'+ str(senddata)+'. .'
                #print(data)
                mysock.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
                turn = ' '
        except ConnectionError:
            break

    print("소켓의 쓰기 버퍼를 닫습니다.")
    mysock.shutdown(socket.SHUT_WR)
    thread_recv.join()

display_intro()

# 메시지 받는 스레스 시작
thread_recv = threading.Thread(target=receive, args=())
thread_recv.start()

# 메시지 보내는 스레드 시작
thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()

# 메시지를 받고, 보내는 스레드가 종료되길 기다림
thread_recv.join()
thread_main.join()

# 스레드가 종료되면, 열어둔 소켓을 닫음.
mysock.close()
print('소켓을 닫습니다.')
print('클라이언트 프로그램이 정상적으로 종료되었습니다.')
