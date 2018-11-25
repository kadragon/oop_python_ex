"""
Project     과제4|네트워킹|MafiaGame|Server
Auth        2513 지명금
Date        2018.11.10.
"""
# 네트워킹을 이용하여 진행하는 마피아 게임
# random을 활용하여 마피아, 의사, 시민을 선택

import socket
import random
import threading
import time
import sys

# 내 서버의 주소 및 포트
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

# 서버를 열 준비
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()

# 게임 플레이 인원 = 4 ~ 8명으로 제한하고 있음
# 게임 플레이 인원 변경시 client쪽 code에서도 수정해야 함
total = 4
character = {"MAFIA": 1, "POLICE": 1, "DOCTOR": 1, "CITIZEN": total - 3}
live_list = {}  
charc_list = {}

client_list = []
first_client_list = []
client_id = []

textline = 30
mafia = 0
select_victim = 0
select_life = 0
gameDay = 0

def sendMessage(sock, message):
    """
    send에 있어서 ConnectionResetError가 방지하는 것을 막기 위해 조정
    """
    try:
        sock.send(bytes(str(message),'utf-8'))
        time.sleep(0.5) # 문장 간의 간격을 띄우게끔 조정하는 것
    except ConnectionResetError:
        print(">> 연결된 Client 중 하나가 끊어졌습니다")
        print(">> 해당하는 Client 정보를 삭제합니다")

        if sock in first_client_list:
            first_client_list.remove(sock)
        if sock in client_list:
            client_list.remove(sock)
        if sock.fileno() in client_id:
            client_id.remove(sock.fileno())
        if sock.fileno() in live_list.keys():
            del live_list[sock.fileno()]

        for sock in client_list:
            sendMessage(sock,"#2:>> 연결된 Client 중 하나가 끊어져서 게임을 종료합니다")
            sendMessage(sock,'#7:')
        server_sock.close()
        

def recvMessage(sock,turn):
    """
    해당하는 sock로 온 data를 받아서 decode해서 되돌려주는 것
    """
    try:
        data = sock.recv(1024).decode('utf-8')
    except (ConnectionError,UnboundLocalError):
        print(">> {}의 차례에서 연결이 끊겼습니다".format(turn))
        print(">> 게임을 종료합니다")
        for sock in cilent_list:
            sendMessage(sock,"#2:>> {}의 차례에서 연결이 끊겼습니다".format(turn))
            sendMessage(sock,"#2:>> 게임을 종료합니다")
            sendMessage(sock,"#7:")
        server_sock.close()
        sys.exit()
    else:
        return data
    
def chooseCharacter():
    """
    client에게 줄 역할을 선정해서 넘겨주는 것
    :return: choose
    """
    global character
    global client_list

    for sock in client_list:
        sendMessage(sock, '#2:캐릭터가 정해지는 중...\n')
        
        choose = random.choice(list(character.keys()))
        character[choose] = character[choose] - 1

        if character[choose] == 0:
            del character[choose]

        charc_list[choose] = sock.fileno()
        
        sendMessage(sock,'#1:'+choose) 

def startGame():
    """
    게임에 대한 설명을 하라고 지시를 보내고 캐릭터를 보내주는 함수
    """
    global client_list
    for sock in client_list:
        sendMessage(sock, '#0:게임을 시작합니다\n')

def gameEnd():
    """
    1) 마피아를 잡았거나
    2) 모두 죽었거나
    """
    global mafia
    
    try:
        if int(mafia) == charc_list['MAFIA'] :
            return False
        else :
            live = 0
            for client in live_list.keys():
                live += live_list[client]
            if live == 0 :
                return False
        return True
    except KeyError:
        print(">> Client간 중첩으로 인해 게임이 원활하게 진행되지 않습니다")
        print(">> 게임을 종료합니다")
        for sock in client_list:
            sendMessage(sock,'#2:>> Client간 중첩으로 게임을 종료합니다')
            sendMessage(sock,'#7:')
        server_sock.close()
        sys.exit()

def TimeMent(time,gameDay):
    """
    낮/밤이 되었습니다 멘트
    """
    global client_list
    
    for sock in client_list:
        ment = '#2:'+"-"*(textline*2+11)+'\n'+'> {}번째 {}이 되었습니다\n'.format(gameDay,time)+"-"*(textline*2+11)+'\n'
        sendMessage(sock, ment)

def chooseToKill():
    """
    지난 밤 살해당한 이를 출력해준다
    """
    global select_victim, select_life

    if select_victim == select_life:
        for sock in client_list:
            message = '#2:'+"-"*(textline*2+11)+'\n'+'> 지난 밤 살해당한 사람은...\n'
            sendMessage(sock,message)
            meessage = '#2:> 없습니다! 모두 생존하셨군요!\n'+"-"*(textline*2+11)+'\n'
            sendMessage(sock,message)
    else:
        for sock in client_list:
            message = '#2:'+"-"*(textline*2+11)+'\n'+'> 지난 밤 살해당한 사람은...\n'
            sendMessage(sock,message)
            message = '#2:> {}가 살해당했습니다!\n'.format(select_victim)+"-"*(textline*2+11)+'\n'
            sendMessage(sock,message)

        live_list[select_victim] = 0
        
        for client in charc_list.keys():
            if charc_list[client] == select_victim:
                del charc_list[client]

        client_id.remove(int(select_victim))
        
    
def MAFIA():
    """
    마피아의 선택
    """
    global charc_list
    global client_list
    global client_id

    mafia_id = charc_list['MAFIA']
    mafia_sock = 0
    for sock in client_list:
        sendMessage(sock,'#2:> 이번 순서는 마피아입니다\n')
        
    for sock in client_list:
        if sock.fileno() == mafia_id:
            mafia_sock = sock
            break

    sendMessage(mafia_sock,'#3:> 마피아는 누구를 죽일 것인지 선택해주세요\n')

    candidate = '#3:> 후보는 '
    for client in client_id:
        if client != mafia_id:
            candidate+= '<{}>'.format(client)
    sendMessage(mafia_sock,candidate+'\n')
    sendMessage(mafia_sock,'#4:')
    select = recvMessage(mafia_sock,'MAFIA')    
    return select

def DOCTOR():
    """
    의사의 선택
    """
    global charc_list
    global client_list
    global client_id

    doctor_id = charc_list['DOCTOR']
    doctor_sock = 0
    for sock in client_list:
        sendMessage(sock,'#2:> 이번 순서는 의사입니다\n')
        
    for sock in client_list:
        if sock.fileno() == doctor_id:
            doctor_sock = sock
            break

    sendMessage(doctor_sock,'#3:> 의사는 누구를 살릴 것인지 선택해주세요\n')

    candidate = '#3:> 후보는 '
    for client in client_id:
        candidate+= '<{}>'.format(client)

    sendMessage(doctor_sock,candidate+'\n')
    sendMessage(doctor_sock,'#4:')
    
    select = recvMessage(doctor_sock,'DOCTOR')
    return select

def POLICE():
    """
    경찰의 선택
    """
    global charc_list
    global client_list
    global client_id

    police_id = charc_list['POLICE']
    police_sock = 0
    for sock in client_list:
        sendMessage(sock,'#2:> 이번 순서는 경찰입니다\n')
        
    for sock in client_list:
        if sock.fileno() == police_id:
            police_sock = sock
            break

    sendMessage(police_sock,'#3:> 경찰은 누구를 마피아로 지목할 것인지 선택해주세요\n')
    
    candidate = '#3:> 후보는 '
    for client in client_id:
        if client != police_id:
            candidate+= '<{}>'.format(client)
    sendMessage(police_sock,candidate+'\n')
    sendMessage(police_sock,'#4:')

    select = recvMessage(police_sock,'POLICE')
    return select

def lastDisscuss():
    """
    최후의 변론
    """
    global cilent_list, client_id
    lastDiscuss = []

    for sock in client_list:
        sendMessage(sock,"#2:최후의 변론시간입니다. 본인의 입장을 밝혀주세요\n")
        sendMessage(sock,'#4:')

        answer = recvMessage(sock,sock.fileno())
        lastDiscuss.append(answer)

    for i in range(len(client_id)):
        print("> {}의 말 : {}".format(client_id[i],lastDiscuss[i]))
        for sock in client_list:
            sendMessage(sock,'#2:'+"-"*(textline*2+11)+'\n')
            sendMessage(sock,"#2:> {}의 말 : {}".format(client_id[i],lastDiscuss[i]))
            sendMessage(sock,'#2:'+"-"*(textline*2+11)+'\n')

def connection():
    """
    Client와 Server간의 연결상태를 확인하는 함수
    """
    global client_list
    global client_id

    while len(client_list)<=total:
        client_sock, client_addr = server_sock.accept()

        client_list.append(client_sock)
        first_client_list.append(client_sock)
        client_id.append(client_sock.fileno())
        live_list[client_sock.fileno()] = 1  # 대기 상태
        print("{}가 접속하였습니다".format(client_sock.fileno()))  # 접속사실을 모두에게 알려야함

        for sock in client_list:  # Server#2:전체공지
            server2_message = "#5-1:{}가 접속하였습니다".format(client_sock.fileno())              
            sendMessage(sock,server2_message)
            sendMessage(sock,'#5-2:'+str(len(client_list)))

        if len(client_list)==total:
            break

connect_thread = threading.Thread(target = connection,args=())
connect_thread.start()
connect_thread.join()

startGame()
chooseCharacter()

for client in charc_list.keys():
    print(client, charc_list[client])

while gameEnd():
    TimeMent('밤',gameDay)
            
    select_victim = MAFIA()
    select_life = DOCTOR()
            
    TimeMent('낮',gameDay)
            
    chooseToKill()
    lastDisscuss()
            
    mafia = POLICE()
    gameDay += 1

    if gameEnd() == False:
        if int(mafia) == charc_list['MAFIA']:
            for sock in first_client_list:
                win_message = '#2:'+"="*textline+" 게임 결과 "+"="*textline+'\n\n'
                win_message += " 마피아가 잡혔습니다! 시민 여러분들이 승리하셨습니다!\n"
                win_message += "="*(textline*2+11)
                sendMessage(sock,win_message)
                sendMessage(sock,'#7:')
        else :
            for sock in first_client_list:
                win_message = '#2:'+"="*textline+" 게임 결과 "+"="*textline+'\n\n'
                win_message += " 마을이 몰살당했습니다! 마피아가 승리했습니다!\n\n"
                win_message += "="*(textline*2+11)
                sendMessage(sock,win_message)
                sendMessage(sock,'#7:')
    
server_sock.close()
