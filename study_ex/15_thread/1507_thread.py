import threading

Q = 1000

def drink(max):
    global Q
    for i in range(max):
        Q -= 1

A = threading.Thread(target = drink, args = (400, ))
B = threading.Thread(target = drink, args = (550, ))

A.start()
B.start()

A.join()
B.join()

print(Q)
