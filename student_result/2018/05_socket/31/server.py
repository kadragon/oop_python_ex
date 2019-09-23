import socket
import threading
import os.path as op
from os import makedirs, listdir

SERVER_IP = '127.0.0.1'
SERVER_PORT = 50000

ADDRESS = (SERVER_IP, SERVER_PORT)

ABSPATH = op.dirname(op.abspath(__file__)) + '\\files\\'


class reciever(threading.Thread):

    def __init__(self, socket):
        self.client = socket
        self.clno = socket.fileno()
        print('{}가 연결되었습니다.'.format(socket.fileno()))

    def run(self):
        while True:
            try:
                data = self.client.recv(1024)
            except ConnectionError:
                print('{}과 연결이 끊겼습니다.'.format(self.clno))
                break

            args = data.decode('UTF-8').split()

            if not args:
                print('{}과 연결이 끊겼습니다.'.format(self.clno))
                break

            if args[0] == 'list':
                dat = ' '.join(listdir(ABSPATH))
                self.client.send(bytes(dat, 'UTF-8'))

            if args[0] == 'quit':
                print('{}과 연결이 종료되었습니다.'.format(self.clno))
                break

            if args[0] == 'upload':
                isOk = self.client.recv(4096).decode('UTF-8')
                if isOk == 'error':
                    print('{}가 업로드에 실패했습니다.')
                else:
                    try:
                        f = open(ABSPATH + args[1], 'wb')
                        upload = self.client.recv(4096)
                        while True:
                            if b'fileend' in upload:
                                upload.replace(b'fileend', b'')
                                f.write(upload)
                                break
                            f.write(upload)
                            upload = self.client.recv(4096)
                        print('{}가 {}를 업로드 되었습니다.'.format(self.clno, args[1]))
                        f.close()
                    except ConnectionError:
                        print('파일 업로드 도중 {}의 연결이 끊겼습니다.'.format(self.clno))
                        break

            if args[0] == 'download':
                try:
                    f = open(ABSPATH + args[1], 'rb')
                    self.client.send(b'ok')
                    download = f.read(1024)

                    while download:
                        self.client.send(download)
                        download = f.read(1024)

                    self.client.send(b'fileend')
                    print('{}가 {}를 다운로드 했습니다.'.format(self.clno, args[1]))
                    f.close()
                except ConnectionError:
                    print('다운로드 중 {}의 연결이 끊겼습니다.'.format(self.clno))
                    break
                except FileNotFoundError:
                    print('{}가 존재하지 않는 파일에 접근했습니다.'.format(self.clno))
                    self.client.send(b'error')
        self.client.close()


makedirs(ABSPATH, exist_ok=True)

print('서버가 시작되었습니다.')

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(ADDRESS)
server_sock.listen()

while True:
    socket, add = server_sock.accept()
    socks = reciever(socket)
    socks.run()
