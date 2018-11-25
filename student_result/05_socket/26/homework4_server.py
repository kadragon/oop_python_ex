# Homework 4 - 서버
print("<<본격 가위바위보 프로그램>>")
import sys, socket, threading, os, time
from random import *
hands = ["가위", "바위", "보"]

myip = socket.gethostbyname(socket.getfqdn()) # 내 아이피 가져옴
print("당신의 아이피는 " + myip + " 입니다.")
myport = int(input("원하는 포트 값을 입력해주세요 : "))
os.system('cls')

print("<<본격 가위바위보 프로그램>>")
print("당신의 아이피는 " + myip + " 입니다.")
print("당신의 포트는 " + str(myport) + " 입니다.")
address = (myip, myport)

# 서버 열기
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)  # 위에 설정한 address로 접속 대기
server_sock.listen()  # 입력을 받아들이는 상태로 대기

try:
    print("클라이언트의 연결을 기다립니다...")
    client_sock, client_addr = server_sock.accept() # 접속을 대기하며, 접속하면 클라이언트 정보 받아옴
except ConnectionError:
    print("클라이언트와 연결이 끊겼습니다. 에러.")
    sys.exit()

os.system('cls')
print("클라이언트 {} 로부터 연결되었습니다.".format(client_addr))
client_sock.send(b"1") # 클라이언트에게 연결되었다고 확인메시지 보냄
time.sleep(1)
os.system('cls')

server_choice = randint(0, 2) # 서버 턴
print("서버는 " + hands[server_choice] + "를 냈습니다!")
client_sock.send(bytes(str(server_choice), 'utf-8'))
time.sleep(1)

client_choice = client_sock.recv(1024)  # 클라이언트 턴
client_choice = int(client_choice.decode('UTF-8'))
print("클라이언트는 " + hands[client_choice] + "를 냈습니다!")
print("")
time.sleep(1)

if server_choice == 0: # 승리 판정
    if client_choice == 0:
        print("비겼습니다.")
    elif client_choice == 1:
        print("졌습니다...")
    elif client_choice == 2:
        print("이겼습니다!!!")
elif server_choice == 1:
    if client_choice == 0:
        print("이겼습니다!!!")
    elif client_choice == 1:
        print("비겼습니다.")
    elif client_choice == 2:
        print("졌습니다...")
elif server_choice == 2:
    if client_choice == 0:
        print("졌습니다...")
    elif client_choice == 1:
        print("이겼습니다!!!")
    elif client_choice == 2:
        print("비겼습니다.")


time.sleep(1)
client_sock.close() # 소켓 닫기
server_sock.close()
print("")
print("클라이언트와의 접속이 종료되었습니다.")
