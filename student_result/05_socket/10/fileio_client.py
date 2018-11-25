import socket

HOST = '192.168.1.146'
PORT = 9009

def getFileFromServer() :
    data_transferred = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))

        filename = sock.recv(1024)
        filename = filename.decode()

        data = sock.recv(1024)
        if not data:
            print('파일[%s]: 서버에 없거나 전송중 사라짐 뿅'%filename)
            return
        with open(filename, 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
                    print('파일[%s] 수신중... 수신량 [%d]'%(filename, data_transferred))
            except Exception as e:
                print(e)
    
    print('파일[%s] 수신종료. 수신량 [%d]'%(filename, data_transferred))

getFileFromServer()