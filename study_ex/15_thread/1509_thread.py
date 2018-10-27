import threading

Q = 1000000
lock = threading.Lock()  # 마치 화장실 처럼, 접근 제한 공간을 만들 수 있다.

def drink(max):
    global Q
    for i in range(max):
        lock.acquire()  # 화장실 잠그기
        Q -= 1
        lock.release()  # 화장실 열기


A = threading.Thread(target = drink, args = (500000, ))
B = threading.Thread(target = drink, args = (500000, ))

A.start()
B.start()

A.join()
B.join()

print(Q)
