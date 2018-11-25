# UpDown Game
# Server Code
# '클라이언트 소켓'은 클라이언트로 향하는 소켓을 의미합니다...

import socket
import threading
import math
from random import shuffle
from os import sys

# 서버 정보
server_ip = '127.0.0.1'
server_port = 39824
server_address = (server_ip, server_port)

# 서버 열기
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(server_address)  # 위에 설정한 주소로 접속 대기
server_sock.listen()  # 입력을 받아들이는 상태로 대기

print("Waiting for connection...")
(client_sock, client_address) = server_sock.accept()  # 연결됨
print("Here comes a new challenger! {}".format(client_address))

game_playing = False
my_turn = False
win_key = ["a", "b", "c", "d", "e", "f", "g", "0",
           "1", "2", "3", "4", "5", "6", "7", "8", "9"]
shuffle(win_key)
win_key = "".join(win_key)
guess_num = -1
# 승리 키를 받는 쪽이 이긴다


def receive_from_client(cl_sock):
    """
    클라이언트 소켓에서 데이터를 받습니다.
    :parameter cl_sock: 클라이언트 소켓입니다.
    :return: 받은 데이터를 반환합니다. (디코딩됩니다.)
    """
    try:
        return cl_sock.recv(1024).decode("utf-8")
    except ConnectionError:
        print("Disconnected. Please turn off this program.")
        cl_sock.close()
        sys.exit(0)


def send_to_client(cl_sock, data):
    """
    클라이언트 소켓으로 데이터를 보냅니다.
    :parameter cl_sock: 클라이언트 소켓입니다.
    :data: 보낼 데이터입니다. (인코딩됩니다.)
    """
    try:
        cl_sock.send(bytes(str(data), "utf-8"))
    except ConnectionError:
        print("Disconnected. Please turn off this program.")
        cl_sock.close()
        sys.exit(0)


def listening(cl_sock):
    """
    클라이언트 소켓에서 오는 데이터를 받아 출력합니다.
    :parameter cl_sock: 클라이언트 소켓입니다.
    """
    global game_playing, guess_num

    while game_playing:  # 게임을 플레이하고 있는 동안만 스레드 실행
        message = receive_from_client(cl_sock)  # 메시지를 받는다
        if message == win_key:
            print("You Win!")
            game_playing = False
            print("Please turn off this program.")
            cl_sock.close()
            sys.exit()
        print(message)  # 메시지를 출력한다
        global my_turn
        if not my_turn:
            if "[Guess]" in message:  # 만약 저것이 상대의 '추측'이라면?
                guess_num = int(message.replace("[Guess] ", ""))  # 추측한 수
                if guess_num != num:
                    print("Answer to his/her guess. ('up'/'down')")
                else:  # 상대가 정답을 맞혔으면!
                    game_playing = False  # 게임 종료
                    send_to_client(cl_sock, win_key)  # 승리 키를 보낸다
                    print("You lose...")
                    print("Please turn off this program.")
                    cl_sock.close()
                    sys.exit()  # 게임 끝
                my_turn = True  # 차례를 내게로 가져온다


def speaking(cl_sock):
    """
    클라이언트 소켓으로 갈 데이터를 입력받아 보냅니다.
    :parameter cl_sock: 클라이언트 소켓입니다.
    """
    global game_playing

    while game_playing:
        try:
            data = input().replace("[Answer]", "")  # 데이터를 입력받는다
        except (KeyboardInterrupt, EOFError):
            continue
        global my_turn
        if my_turn:  # 만일 내 턴이라면?
            if (guess_num < num and data != 'up') or (guess_num > num and data != 'down'):
                print("Wrong! You Lose.")
                game_playing = False
                send_to_client(cl_sock, win_key)
                print("Please turn off this program.")
                cl_sock.close()
                sys.exit()
            else:
                data = "[Answer] "+data
                my_turn = False
                print("Good!")
        send_to_client(cl_sock, data)


def decide_number():
    """
    숫자를 결정합니다.
    :return: 양의 정수 하나
    """
    print("Type your number. (1<=N<=1000000, integer)", end=" ")
    num = input(">> ")
    try:
        num = int(num)
        if num <= 0 or num > 1000000:
            print("Invalid value.")
            return decide_number()
        else:
            return num
    except ValueError:
        print("Invalid value.")
        return decide_number()


send_to_client(client_sock, win_key)
send_to_client(client_sock, "Deciding a number...(Natural Number, <=1000000)")
num = decide_number()
send_to_client(client_sock, "Number decided.")

game_playing = True
listen = threading.Thread(target=listening, args=(client_sock,))  # 귀를 열어둔다
speak = threading.Thread(target=speaking, args=(client_sock,))  # 입도 열어둔다
listen.start()  # 듣기를 시작한다
speak.start()  # 말하기도 시작한다

print("You should answer to his/her guess. If you answer incorrectly, you lose.")
print("Your answer should be 'up' or 'down'.")
