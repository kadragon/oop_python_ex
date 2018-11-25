
import socketserver
from os.path import exists
import time

HOST = '192.168.1.146'
PORT = 9009

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print('[%s] connected'%self.client_address[0])
        # filename = self.request.recv(1024)
        # filename = filename.decode()

        filename = input()
        self.request.send(filename.encode())

        if not exists(filename):
            return

        print('file [%s] 전송 시작'%filename)
        start = time.time()

        with open(filename, 'rb') as f:
            try:
                data = f.read(1024)
                while data:
                    data_transferred += self.request.send(data)
                    data = f.read(1024)
            except Exception as e:
                print(e)
        print('전송완료[%s], 전송량[%d]'%(filename, data_transferred))
        end = time.time()
        print('소요시간: %s seconds'%(end-start))

def runServer():
    print('++++++원하는 파일을 드래그++++++')
    #print("+++파일 서버를 끝내려면 'Ctrl + C'를 누르세요")
    while(True):
        try:
            server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n서버초기화")
            server.server_close()

runServer()