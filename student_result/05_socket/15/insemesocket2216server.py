import socket
import random

myip = '127.0.0.1'
myport = 50000
address = (myip, myport)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()

print("===== 클라이언트 접속을 대기하는 중입니다.")
client_sock, client_addr = server_sock.accept()
print("===== 클라이언트가 접속하였습니다.")

firstmassage='이 문제는 1부터 1000까지의 수 중에 어느 수가 랜덤으로 생성되었는지 알아맞히는 것입니다.\n' \
             '당신이 입력한 값보다 답이 큰지 작은지를 알려드릴 것입니다.\n' \
             '답일 경우 몇 번만에 맞혔는지 알려드릴 것입니다.'
client_sock.send(bytes(firstmassage, 'UTF-8'))

print("1부터 1000 사이의 수를 생성했습니다.")
ans = random.randrange(1, 1001)
print("정답: ",ans)
anslist=[]
for i in range(1,1001): anslist.append(str(i))
howmany=1

while True:
    try:
        massage='1부터 1000까지의 값을 입력하십시오'
        client_sock.send(bytes(massage, 'UTF-8'))
        data = client_sock.recv(1024)
        try:
            data=int(data)
            if int(data)>ans:
                massage='당신이 입력한 값은 답보다 큽니다'
                client_sock.send(bytes(massage, 'UTF-8'))
                howmany+=1
            elif int(data)<ans:
                massage='당신이 입력한 값은 답보다 작습니다.'
                client_sock.send(bytes(massage, 'UTF-8'))
                howmany+=1
            elif int(data) == ans:
                massage='정답입니다. '+str(howmany)+'번 만에 맞히셨습니다'
                client_sock.send(bytes(massage,'UTF-8'))
                break

        except ValueError:
            get = data.decode('UTF-8')
            if get.strip().find('답')!=-1:
                massage='\'답\'이라는 글자가 포함된 입력을 받을 시 답을 알려드립니다. '+str(ans)
                client_sock.send(bytes(massage, 'UTF-8'))
            else:
                massage='잘못된 입력을 시행했습니다'
                client_sock.send(bytes(massage, 'UTF-8'))

    except OSError:
        print('연결이 종료되었습니다.')
        break

client_sock.close()
server_sock.close()
