import threading
import time
import random


# threading.Thread를 상속해서 Thread를 사용할 수 있는 class 생성
class client_thread(threading.Thread):
    def __init__(self, clientname, sec):
        threading.Thread.__init__(self)  # Thread를 사용하기 위해서, __init__에 반드시 있어야 함.
        self.clientname = clientname
        self.sec = sec
    
    def run(self):
        while True:
            print("%s - delay %f" % (self.clientname, self.sec))
            time.sleep(self.sec)

# Thread를 저장하기 위한 리스트
client = []
for i in range(10):
    # Thread를 만들어서 저장함.
    client.append(client_thread("client" + str(i), random.randint(1, 10)))

    # 만든 Thread 실행
for i in range(10):
    client[i].start()
