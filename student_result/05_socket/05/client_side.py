import socket
import threading as trd
import time
import random
import sys

SERVER_IP = '127.0.0.1'
SERVER_PORT = 50000
address = (SERVER_IP, SERVER_PORT)

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(address)

# print(my_socket.fileno())

flag = True


def receive():

    global my_socket
    global flag

    while flag is True:

        try:
            msg = my_socket.recv(1024)
        except ConnectionError as e:
            print(e)
            continue
        except OSError as e:
            print(e)
            break

        print(msg.decode('UTF-8'))
        if msg.decode('UTF-8') == 'end':
            flag = False
            exit()
            
        

def main():

    global my_socket
    global flag

    rcv_thread = trd.Thread(target=receive, args=())
    rcv_thread.start()

    while flag is True:
        data = input()
        if (data == '!quit'):
            break
        try:
            my_socket.send(bytes(data, 'UTF-8'))
        except ConnectionError:
            break

    print("연결을 종료합니다")
    my_socket.shutdown(socket.SHUT_WR)
    flag = False
    rcv_thread.join()


main_thread = trd.Thread(target=main, args=())
main_thread.start()

# rcv_thread = trd.Thread(target=receive, args=())
# rcv_thread.start()

# rcv_thread.join()

# my_socket.close()
