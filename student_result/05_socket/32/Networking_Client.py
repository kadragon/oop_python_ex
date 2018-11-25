
import socket, threading
import base64

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)


#소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)

#암호화에 필요한것
CodeKey='asdf'
decode_mode=False
encode_mode=False
lock=threading.Lock()

#안내문
note='''
connection complete\n
If you want to leave chat, just type !quit\n
Group명령어를 받으면 같은 암호 그룹을 만들 사람들을 입력할 수 있게 된다.\n
Decode activate 명령어를 받으면 복호화 기능이 비활성화 된다.
Decode deactiviate 명령어를 받으면 앞으로 받는 모든 문자를 해독한 상태로 출력된다.\n
Encode activate 명령어를 받으면 앞으로 보내는 모든 문자를 암호화된 상태로 보내진다.
Encode deactiviate 명령어를 받으면 암호화 기능이 비활성화 된다.\n
Help 명령어를 받으면 가능한 명령어를 다 보여준다.\n
List 명령어를 받으면 현재 접속중인 사람들을 다 보여준다.\n
'''
print(note)


#복호화&암호화 함수(opensourced by https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password)

def encode(clear, key='asdf'):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c))%9876543210)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode('utf-8')).decode('utf-8')

def decode(enc, key='asdf'):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode('utf-8')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((9876543210+ord(enc[i]) - ord(key_c))%9876543210)
        dec.append(dec_c)
    return "".join(dec)

# 서버로부터 메시지를 받아, 출력하는 함수.
def receive():
    global mysock, lock
    global CodeKey, decode_mode
    while True:
        try:
            data = mysock.recv(1024)  # 서버로 부터 값을 받는것
        except ConnectionError:
            print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
            break

        if not data:  # 넘어온 데이터가 없다면.. 로그아웃!
            print("서버로부터 정상적으로 로그아웃했습니다.")
            break

        data=data.decode('UTF-8')

        #나에게 주는 키 받기
        if data=='yourKey':
            lock.acquire()
            CodeKey=mysock.recv(1024).decode('UTF-8')
            lock.release()
            continue

        #상대가 주는 키 받기
        if data=='Key':
            lock.acquire()
            print('Someone gave you the key')
            CodeKey=mysock.recv(1024).decode('UTF-8')
            lock.release()
            continue
                   
        #아이디 빼고 decode하기
        if decode_mode:
            try:
                i=data.find(':')
                t=data[i+1:]
                data=data[:i]+':'+decode(''.join(t), CodeKey)
            except:
                pass

        print(data)  # 서버로 부터 받은 값을 출력

    print('소켓의 읽기 버퍼를 닫습니다.')
    mysock.shutdown(socket.SHUT_RD)


# 서버에게 메시지를 발송하는 함수 | Thread 활용
def main_thread():
    global mysock, lock
    global CodeKey, encode_mode, decode_mode
    
    # 메시지 받는 스레스 시작
    thread_recv = threading.Thread(target=receive, args=())
    thread_recv.start()

    while True:
        try:
            data = input('>')
        except KeyboardInterrupt:
            continue

        if data.lower().strip() == '!quit':
            print("서버와의 접속을 끊는 중입니다.")
            break

        #암호화/복호화 명령어 받기
        if data.lower().strip() =='decode activate':
            decode_mode=True
            print('*'*50+'\nDecode mode is activated'+'*'*50)
            continue

        if data.lower().strip() =='decode deactivate':
            decode_mode=False
            print('*'*50+'\nDecode mode is deactivated\n'+'*'*50)
            continue
        
        if data.lower().strip() =='encode activate':
            encode_mode=True
            print('*'*50+'\nEncode mode is activated\n'+'*'*50)
            continue

        if data.lower().strip() =='encode deactivate':
            encode_mode=False
            print('*'*50+'\nEncode mode is deactivated\n'+'*'*50)
            continue

        #그룹 명령어 받기
        if data.lower().strip()=='group':
            print('누구랑 대화를 나누시겠습니까?')
            print('한명씩 id를 입력해주시고 입력을 모두 마치셨으면 "finish"라고 입력해주세요')
            try:
                mysock.send(bytes(data, 'UTF-8'))
                t=input('\nWho will join the team? : ')
                while t.lower().strip()!='finish':
                    mysock.send(bytes(t, 'UTF-8'))
                    lock.acquire()
                    t=input('\nWho will join the team? : ')
                    lock.release()
                mysock.send(bytes(t, 'UTF-8'))
                continue
            except KeyboardInterrupt:
                print('You should be type wisely')
                break;
            except ConnectionError:
                print("Something's wrong with your connection")
                break;

        #도움말
        if data.lower().strip()=='help':
            print(note)
            continue
        
        #list
        if data.lower().strip()=='list':
            mysock.send(bytes('list', 'utf-8'))
            continue

        #암호화 하기
        try:
            if encode_mode:
                data=encode(data, CodeKey)
            mysock.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
        except ConnectionError:
            print("Something's wrong with your connection")
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
