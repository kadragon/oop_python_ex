import socket
import threading
import random

# 서버의 설정값을 저장
myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

# 서버를 연다.
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()
print('Start Chat - Server')

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []
# 클라이언트별로 정답을 저장할 공간
client_ans = []
# 클라이언트별 시도 횟수를 저장할 공간
client_cnt = []

# 클라이언트로 부터 메시지를 받는 함수 | Thread 활용


def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    global client_ans  # 클라이언트 별 정답을 저장한다.
    global client_cnt

    client_index = -1
    senddata = ''

    while True:
        # 클라이언트로부터 데이터를 받는다.
        try:
            data = client_sock.recv(1024)
        except ConnectionError:
            print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
            break

        # 클라이언트 리스트에서 메시지를 받은 소켓의 위치를 찾는다.
        client_index = client_list.index(client_sock)
        recv = data.decode('UTF-8')  # 받은 메시지를 str로 디코딩한다.

        client_cnt[client_index] += 1  # 클라이언트의 시도횟수를 1늘린다.

        # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
        if not data:
            print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
            client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
            break

        if int(recv) < client_ans[client_index]:
            senddata = recv+': up'
        elif int(recv) > client_ans[client_index]:
            senddata = recv + ': down'
        else:
            senddata = 'Answer!'

        client_sock.send(bytes(senddata, 'utf-8'))

        # 정답을 맞추면 연결을 종료한다.
        if senddata == 'Answer!':
            client_sock.send(
                bytes("정답을 맞추셨으니 서버에서 클라이언트 정보를 삭제하는 중입니다ㅎㅎ", 'utf-8'))
            break

        # 시도 횟수가 10이 되어도 종료한다.
        if client_cnt[client_index] > 9:
            client_sock.send(
                bytes("10번째 시도에 실패했습니다. 서버에서 클라이언트 정보를 삭제합니닿", 'utf-8'))
            break

    # 메시지 송발신이 끝났으므로, 대상인 client는 목록에서 삭제.
    client_id.remove(client_sock.fileno())
    client_list.remove(client_sock)
    del client_cnt[client_index]
    del client_ans[client_index]
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
    global client_ans
    global client_cnt

    while True:
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()
        ans = random.randint(1, 100)

        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())
        client_ans.append(ans)
        client_cnt.append(0)

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        print('정답 : {}'.format(ans))
        print("현재 연결된 사용자: {}\n".format(client_list))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock,))
        thread_recv.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== Chat Server ==============")

thread_server.join()
server_sock.close()