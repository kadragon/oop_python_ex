import socket
import threading
import requests
from bs4 import BeautifulSoup as bs
import random
import time

# 서버의 설정값을 저장
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

# 서버를 연다.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
print('*'*30, ' Game Start ', '*'*30)

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []
client_point = {}
data = 0
check = []


# 클라이언트들로 부터 메시지를 받는 함수 | Thread 활용
def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    global data
    while True:
        # 클라이언트로부터 데이터를 받는다.
        q_number = random.randint(0, n)
        if q_number not in check :
            check.append(q_number)
            client_sock.send(bytes(problems[q_number][1],'utf-8'))
        try:
            data = client_sock.recv(1024).decode('utf-8')
            data.replace(' ','')
            
        except ConnectionError:
            print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
            break
        
        # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
        if not data:
            print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
            client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
            break
        '''
        # 데이터가 들어왔다면 접속하고 있는 모든 클라이언트에게 메시지 전송
        data_with_id = bytes(str(client_sock.fileno()), 'utf-8') + b":"+data
        for sock in client_list:
            if sock != client_sock:
                sock.send(data_with_id)
        '''
        print(data)
        print('답 : ',problems[q_number][2])
        while True :
            if type(problems[q_number][2]) == 'list' :
                if data in problems[q_number][2] :
                    break
            else :
                if data == problems[q_number][2] :
                    break

            client_sock.send(bytes('땡!\n','utf-8'))
            data = client_sock.recv(1024).decode('utf-8')
        client_sock.send(bytes('정답입니다!!\n','utf-8'))
        
    # 메시지 송발신이 끝났으므로, 대상인 client는 목록에서 삭제.
    client_id.remove(client_sock.fileno())
    client_list.remove(client_sock)
    print("현재 연결된 사용자: {}\n".format(client_id), end='')
    # 삭제 후 sock 닫기
    client_sock.close()
    print("클라이언트 소켓을 정상적으로 닫았습니다.")
    print('#----------------------------#')
    return 0


# 연결 수립용 함수 | Thread 활용
def connection():
    global client_list
    global client_id

    while True:
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()
        
        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        print("현재 연결된 사용자: {}\n".format(client_list))

        client_sock.send(bytes("안녕! 난 스핑크스의 사자. 너에게 문제를 내주지!\n", 'utf-8'))
        time.sleep(1)
        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock, ))
        thread_recv.start()

def fix(problems):  # 넌센스 퀴즈 문제를 수정하는 과정!
    delete = []
    x = []
    x.append(problems[1][2])
    x.append('9')
    problems[1][2] = x

    for i in range(len(problems)):
        if problems[i][1].find('란?') != -1 :
            delete.append(i)

    delete.append(9)
    delete.append(19)
    delete.append(20)
    delete.append(22)
    delete.append(24)
    delete.append(25)
    delete.append(57)
    delete.append(65)
    delete.append(66)
    delete.append(121)
    delete.append(138)
    delete.append(161)
    delete.append(165)
    delete.append(178)
    delete.append(248)
    delete.append(249)
    delete.append(251)
    delete.append(252)
    delete.append(259)
    for i in range(269,276):
        delete.append(i)
    delete.append(277)
    delete.append(279)
    delete.append(281)
    for i in range(289,295):
        delete.append(i)
    for i in range(297,305):
        delete.append(i)
    delete.append(307)
    delete.append(310)
    delete.append(311)
    delete.append(319)
    delete.append(321)
    delete.append(322)
    for i in range(326,340):
        if i != 329:
            delete.append(i)
    delete.append(353)
    delete.append(128)
    
    problems[72][1] = problems[72][1].replace('공중에서','대부분의')
    problems[90][1] = '두 발로 걷는 소는?'
    problems[123][1] = problems[123][1].replace('탤런트 최지우','SASA의 홍지우')
    problems[144][1] = problems[144][1].replace('데','뎅')
    problems[256][2] += '금지'
    problems[306][2] = problems[306][2].replace(".",",")
    problems[190][2] = problems[190][2].replace(".",",")

    delete.sort(reverse=True)
    for i in delete:
        del(problems[i])
    

# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()


# 넌센스 문제 파싱
with requests.Session() as q :
    quiz_page = q.get('http://w3devlabs.net/wp/?p=1561')
    quiz_page.encoding = 'utf-8'
    quiz_html = quiz_page.text
    quiz_soup = bs(quiz_html, 'html.parser')

# 넌센스 문제 딕셔너리로 정리
problems = str(quiz_soup.select('div.entry-content p'))
problems = problems.split('<br/>\n')
n = len(problems)-1
problems[0] = problems[0].replace('[<p>','')
problems[n] = problems[n].replace('</p>]','')
problems[2] += ' ' + problems[3]
del(problems[3])

for i in range(int(len(problems))):
    problems[i] = problems[i].split('?')
    problems[i].extend(problems[i][0].split('.'))
    del(problems[i][0])
    problems[i].append(problems[i][0])
    del(problems[i][0])
    if len(problems[i]) == 4 :
        problems[i][1] =problems[i][1] + problems[i][2]
        del(problems[i][2])
    problems[i][1] += '?'
    
    #print(problems[i])
    
    problems[i][2] = problems[i][2].replace(' ','')
    if '(' in problems[i][2] :
        pro = problems[i][2].split('(')
        problems[i][2] = pro[0]
    if ',' in problems[i][2] :
        problems[i][2] = problems[i][2].split(',')
    #print(problems[i])

    try :
        problems[i][0] = int(problems[i][0])-1
    except ValueError :
        continue

fix(problems)
n = len(problems)-1
'''
for i in range(len(problems)):
    print(i,':',problems[i])
print(type(problems[50][1]))
print(problems[50][1].replace('공중에서','대부분의'))
'''
'''
check = []
while True :
    q_number = random.randint(0, len(problems)-1)
    if q_number not in check :
        check.append(q_number)
        for sock in client_list:
            sock.send(bytes(problems[q_number][1]+'\n','utf-8'))
    while True :
        if data : break
'''

thread_server.join()
server_sock.close()
