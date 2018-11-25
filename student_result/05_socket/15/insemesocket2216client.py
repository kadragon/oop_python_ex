import socket, threading

server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)

thread_end = 0

def receive():
    global mysock

    while True:
        try:
            data = mysock.recv(1024)
            print(data.decode('UTF-8'), " *from Server")
            get=data.decode('UTF-8')
            if get[0]=='정': break
        except OSError:
            print('연결이 종료되었습니다.')
            break

    mysock.close()

thread_recv = threading.Thread(target=receive, args=())
thread_recv.start()

while True:
    try:
        data = input('>')
    except KeyboardInterrupt:
        break
    if data == '!quit' or '':
        break

    mysock.send(bytes(data, 'UTF-8'))

mysock.close()
print("disconneted")