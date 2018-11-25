# Homework 4 - 클라이언트
print("<<본격 가위바위보 프로그램>>")
import sys, socket, threading, os, time
from random import *
hands = ["가위", "바위", "보"]

server_ip = input("서버의 아이피를 입력해주세요 : ")
server_port = int(input("서버의 포트를 입력해주세요 : "))
address = (server_ip, server_port)
os.system('cls')

try:
    print("아이피 " + server_ip + " , 포트 " + str(server_port) + " 로 접속을 시도합니다.")
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(address)
except ConnectionError:
    print("서버의 응답이 없습니다. 프로그램을 종료합니다.")
    sys.exit()

check = 0
check = mysock.recv(1024)  # 연결확인
check = check.decode('UTF-8')
if check=="1":
    print("서버 {} 와 성공적으로 연결되었습니다".format(address))
    time.sleep(1)
else:
    print("서버와의 연결이 이상합니다.")
    print("프로그램을 종료합니다.")
    sys.exit()

os.system('cls')
server_choice = mysock.recv(1024) # 서버 턴
server_choice = int(server_choice.decode('UTF-8'))
print("서버는 " + hands[server_choice] + "를 냈습니다!")
time.sleep(1)

client_choice = randint(0, 2) # 클라이언트 턴
print("클라이언트는 " + hands[client_choice] + "를 냈습니다!")
mysock.send(bytes(str(client_choice), 'utf-8'))
print("")
time.sleep(1)

if client_choice == 0: # 승리 판정
    if server_choice == 0:
        print("비겼습니다.")
    elif server_choice == 1:
        print("졌습니다...")
    elif server_choice == 2:
        print("이겼습니다!!!")
elif client_choice == 1:
    if server_choice == 0:
        print("이겼습니다!!!")
    elif server_choice == 1:
        print("비겼습니다.")
    elif server_choice == 2:
        print("졌습니다...")
elif client_choice == 2:
    if server_choice == 0:
        print("졌습니다...")
    elif server_choice == 1:
        print("이겼습니다!!!")
    elif server_choice == 2:
        print("비겼습니다.")

time.sleep(1)
mysock.close() # 소켓 닫기
print("")
print("클라이언트와의 접속이 종료되었습니다.")