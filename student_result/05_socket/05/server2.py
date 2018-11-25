import socket
import threading as trd
import multiprocessing
from time import sleep


MY_IP = '127.0.0.1'
MY_PORT = 50000
address = (MY_IP, MY_PORT)

CONNECTION_WAIT_TIME = 60
RESPONSE_WAIT_TIME = 30
current_time = 0


print("Start")


client_dict = {}
client_info_dict = {}


class client(trd.Thread):

    def __init__(self, client_socket, client_address):

        trd.Thread.__init__(self)

        self.client_socket = client_socket
        self.client_address = client_address
        self.rcp = None
        self.is_alive = True

    def get_client_num(self):

        try:
            data = self.client_socket.recv(1024)
        except ConnectionError:
            print("Connection with %d lost!" % (self.client_socket.fileno()))

        return data

    def run(self):

        global client_info_dict
        global current_time

        while self.rcp is None:
            client_num = self.get_client_num()

            if self.is_alive == False:
                err_msg = bytes("패자는 말이 없습니다.", 'UTF-8')
                self.client_socket.send(err_msg)
            else:
                self.rcp = client_num.decode('UTF-8')
                break


def timekeeper(time):

    global current_time
    global server_socket
    global connect_thread

    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    time_msg = "{}초 남았습니다!"

    for i in range(time):
        sleep(1)
        if i % 5 == 0:
            send_msg(time_msg.format(time - i))
        print(time_msg.format(time - i))
        current_time += 1

    # connect_thread._stop()
    server_socket.close()


def connection():

    global current_time
    global client_info_dict
    lock = trd.Lock()

    while True:
        try:
            client_socket, client_address = server_socket.accept()
        except OSError:
            break
        lock.acquire()
        client_thread = (client_socket, client_address)
        client_info_dict.update({client_socket.fileno(): client_thread})
        lock.release()

    current_time = 0


def get_winner(client_list):

    moves = ('rock', 'paper', 'scissors')
    check = {'rock': False, 'paper': False, 'scissors': False}

    for client in client_list:
        client_move = client.rcp
        if client_move in moves:
            check[client_move] = True

    if check['rock'] == False and check['paper'] == check['scissors'] == True:
        return 'scissors'
    elif check['paper'] == False and check['rock'] == check['scissors'] == True:
        return 'rock'
    elif check['scissors'] == False and check['rock'] == check['paper'] == True:
        return 'paper'
    else:
        return 'tie'


def send_msg(msg):

    global client_info_dict

    items = client_info_dict.values()
    for client in items:
        bytemsg = bytes(msg, 'UTF-8')
        try:
            client[0].send(bytemsg)
        except:
            continue


# connect_time = trd.Thread(target=timekeeper, args=(CONNECTION_WAIT_TIME,))
# connect_thread = trd.Thread(target=connection, args=())
# response_time = trd.Thread(target=timekeeper, args=(RESPONSE_WAIT_TIME,))


print("new")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen()

connect_time = trd.Thread(target=timekeeper, args=(CONNECTION_WAIT_TIME,))
connect_thread = trd.Thread(target=connection, args=())
response_time = trd.Thread(target=timekeeper, args=(RESPONSE_WAIT_TIME,))

connect_thread.start()
connect_time.start()

connect_time.join()
connect_thread.join()

msg = "가위바위보 게임 시작!"
values = list(client_info_dict.values())
for client_info in values:
    client_socket = client_info[0]
    client_address = client_info[1]
    try:
        new_client = client(client_socket, client_address)
        client_dict.update({client_socket.fileno(): new_client})
    except TypeError:
        client_info_dict.pop(client_socket.fileno(), None)
        client_dict.pop(client_socket.fileno(), None)
        continue

send_msg(msg)

response_time.start()

for client in client_dict.values():
    client.start()

response_time.join()
for client in client_dict.values():
    client.join()

print("end")

current_time = 0

client_list = list(client_dict.values())
winner = get_winner(client_list)
print(winner)

print("test")

if winner == "tie":
    msg = bytes("무승부입니다!", "UTF-8")

    for client in client_dict.values():
        moves = ('rock', 'paper', 'scissors')

        if client.rcp not in moves:
            msg = bytes("안내면 지는거죠", 'UTF-8')
            client.is_alive = False

        try:
            client.client_socket.send(msg)
        except:
            continue

else:
    for client in client_dict.values():

        if client.rcp != winner:
            print("lose")
            msg = bytes("당신은 졌습니다!", 'UTF-8')
            client.is_alive = False
            try:
                client.client_socket.send(msg)
            except:
                continue
        else:
            print("win")
            msg = bytes("당신의 승리입니다!", 'UTF-8')
            try:
                client.client_socket.send(msg)
            except:
                continue

send_msg("end")
