import socket
import threading
import time

# 서버의 설정값을 저장
myip = '127.0.0.1'
myport = 50000
cnt=0
address = (myip, myport)
gameplay={}


# 서버를 연다.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []

def timecall(target_id):
    global gameplay
    global cnt

    success = 'N/A'

    timestamp = time.time()
    tmp = gameplay.setdefault(target_id,timestamp)
    if tmp == timestamp :
        pass
    else:
        original_time = gameplay[target_id]
        finale_time = timestamp
        delta_time = finale_time -  original_time
        del(gameplay[target_id])
        success=delta_time
        if 0.95 < delta_time < 1.05:
            cnt = cnt + 1

    return success


# 클라이언트로 부터 요청을 받는 함수 | Thread 활용
def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    global gameplay

    while True:
        # 클라이언트로부터 데이터를 받는다.
        try:
            data = client_sock.recv(1024)
        except ConnectionError:
            print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
            break

        # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
        if not data:
            print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
            client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
            break

        # 데이터가 들어왔다면 접속하고 있는 모든 클라이언트에게 메시지 전송
        Isreal = timecall(str(client_sock.fileno()))
        data_with_id = bytes(str(client_sock.fileno())+'님이'+str(Isreal)[0:9] + '초의 기록으로 성공하셨습니다.', 'utf-8') + b""
        print(str(client_sock.fileno()) + ' : ' + str(Isreal))
        if Isreal == 'N/A':
            pass
        elif 0.95 < Isreal < 1.05 :
            howgreat = str(abs(Isreal-1))[0:8]
            for sock in client_list:
                if sock != client_sock:
                    sock.send(data_with_id)
                else:
                    sock.send(bytes("성공을 축하드립니다! 기록은 "+howgreat+" 초 정확도 입니다.(낮을수록 좋음)",'utf-8')+b"")
        else:
            client_sock.send(bytes("실패하셨군요..... ㅠㅠㅠㅠ",'utf-8')+b"")



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
    global gameplay

    while True:
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()

        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("현재 연결된 사용자: {}\n".format(client_list))

        data_with_admin = b"admin : " + bytes("게임의 규칙을 설명하겠습니다.\n규칙은 매우 간단합니다.\n아무 문자를 보내고, 그 이후에 또 다시 아무 문자를 보내세요.\n두 문자를 보낸 간격이 1초에 가깝다면 당신은 승리합니다.\n"
                                              "admin : 당신의 경쟁자는 %d명 입니다.\n현재까지 누적된 성공횟수는 %d회 입니다.\n행운을 빌어요!\n"
                                              "admin : 당신의 아이디는 %s입니다"%(len(client_list)-1,cnt,str(client_sock.fileno())),'utf-8')
        client_sock.send(data_with_admin)

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock,))
        thread_recv.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== Game Server ==============")

thread_server.join()
server_sock.close()