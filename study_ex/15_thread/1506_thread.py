import threading, queue
import time
import random

data_from_client = {}

def client(name, inputdata, sec):
    time.sleep(sec)
    data_from_client[name] = inputdata

def result():
    # time.sleep(2)

    A.join()  # A Thread가 종료될 때까지 흐름을 멈춤(대기)
    B.join()  # B Thread가 종료될 때까지 흐름을 멈춤(대기)

    print("A: ", data_from_client["A"])
    print("B: ", data_from_client["B"])

A = threading.Thread(target= client, args = ("A", random.randint(0, 2), random.randint(1, 4)))
B = threading.Thread(target= client, args = ("B", random.randint(0, 2), random.randint(1, 4)))

C = threading.Thread(target= result, args=())

A.start()
B.start()
C.start()

# KeyError: 'A'
