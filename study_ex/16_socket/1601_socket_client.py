import socket

# 접속하고자 하는 서버의 주소 및 포트
server_ip = '192.168.1.80'
server_port = 50000
address = (server_ip, server_port)

# socket을 이용해서 접속 할 준비
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)  # 서버에 접속

data = mysock.recv(1024)  # 1024 바이트 수신
print(data.decode('UTF-8'))

data = mysock.recv(1024)  # 1024 바이트 수신
print(data.decode('UTF-8'))

mysock.close()
