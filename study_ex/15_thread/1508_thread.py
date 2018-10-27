import threading

Q = 1000000

def drink(max):
    global Q
    for i in range(max):
        Q -= 1

A = threading.Thread(target = drink, args = (500000, ))
B = threading.Thread(target = drink, args = (500000, ))

A.start()
B.start()

A.join()
B.join()

print(Q)  # 0이 나오지 않는다...!
