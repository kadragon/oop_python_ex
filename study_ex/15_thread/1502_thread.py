import time

while True:
    print("clientA")
    time.sleep(0.1)

    print("clientB")
    time.sleep(0.1)

    print("clientC")
    time.sleep(0.1)

    print("clientD - 지연 2초")
    time.sleep(2)

    print("clientE")
    time.sleep(0.1)

    print("clientF - 지연 3초")
    time.sleep(3)

    print("clientG")
    time.sleep(0.1)
    