# UpDown Game
# Client Code
# '서버 소켓'은 서버로 향하는 소켓을 의미합니다...

import socket
import threading
from os import sys

server_ip='127.0.0.1'
server_port=39824
server_address=(server_ip, server_port)

my_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(server_address) # 소켓으로 서버에 접속

game_playing=False # 게임을 플레이하고 있는지를 알려주는 변수
my_turn=True # 내 턴(클라이언트)인지 알려주는 변수(먼저 시작)
opportunity=20 # 남은 기회의 횟수

def receive_from_server(sv_sock):
    """
    서버 소켓에서 데이터를 받습니다.
    :parameter sv_sock: 서버 소켓입니다.
    :return: 받은 데이터를 반환합니다. (디코딩됩니다.)
    """
    try:
        return sv_sock.recv(1024).decode("utf-8")
    except ConnectionError:
        print("Disconnected. Please turn off this program.")
        sv_sock.close()
        sys.exit(0)

def send_to_server(sv_sock,data):
    """
    서버 소켓으로 데이터를 보냅니다.
    :parameter sv_sock: 서버 소켓입니다.
    :data: 보낼 데이터입니다. (인코딩됩니다.)
    """
    try:
        sv_sock.send(bytes(str(data),"utf-8"))
    except ConnectionError:
        print("Disconnected. Please turn off this program.")
        sv_sock.close()
        sys.exit(0)

def listening(sv_sock):
    """
    서버 소켓에서 오는 데이터를 받아 출력합니다.
    자신의 턴이 아니었고, 서버에게서 답이 온다면, 자신의 턴으로 만들어줍니다. 
    :parameter sv_sock: 서버 소켓입니다.
    """
    global game_playing

    while game_playing: # 게임을 플레이하고 있는 동안만 스레드 실행
        message=receive_from_server(sv_sock) # 메시지를 받는다
        if message==win_key: # 승리 키를 받으면
            print("You Win!")
            print("Please turn off this program.")
            game_playing=False
            sys.exit() # 게임 끝
        print(message) # 받은 메시지를 출력한다
        # 만약 받은 메시지가 추측에 대한 답이라면
        global my_turn
        if not my_turn and '[Answer]' in message: # 상대가 단서를 제공해준다면?
            my_turn=True # 내 턴으로 만든다

def speaking(sv_sock):
    """
    서버 소켓으로 갈 데이터를 입력받아 보냅니다.
    자신의 턴이라면, 그리고 '추측'의 형태를 갖춘다면 추측 횟수를 차감하고 턴을 넘깁니다. 
    :parameter sv_sock: 서버 소켓입니다.
    """
    global game_playing, opportunity

    while game_playing: # 게임을 플레이하고 있는 동안만 스레드 실행
        try:
            data=input().replace("[Guess]","") # 입력을 받는다(키워드 제거)
        except (KeyboardInterrupt, EOFError):
            continue
        global my_turn
        if my_turn: # 내 턴이라면?
            try:
                data=int(data)
            except ValueError:
                pass
            else:
                if 1<=data and data<=1000000: # 이것이 '추측'의 형태를 갖춘다면
                    data="[Guess] "+str(data) # 키워드를 붙이고
                    my_turn=False # 내 턴을 넘긴 뒤
                    opportunity-=1 # 기회를 차감한다
                    print("You have %d chances left." %opportunity)
        send_to_server(sv_sock,data) # 전송!

win_key=receive_from_server(my_sock) # 승리 키를 받는 쪽이 이긴다
print(receive_from_server(my_sock))
print(receive_from_server(my_sock))

game_playing=True
listen=threading.Thread(target=listening,args=(my_sock,)) # 귀를 열어둔다
speak=threading.Thread(target=speaking,args=(my_sock,)) # 입도 열어둔다
listen.start() # 듣기도 시작한다
speak.start() # 말하기도 시작한다

print("You should guess his/her number within 20 times.")

while opportunity>=0:
    pass
send_to_server(my_sock,win_key)
game_playing=False
my_sock.close()
print("You lose...")
print("Please turn off this program.")