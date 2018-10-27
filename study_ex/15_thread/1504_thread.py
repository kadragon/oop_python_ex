import threading
import time


class client_thread():
    def __init__(self, clientname, sec):
        self.clientname = clientname
        self.sec = sec

    def __call__(self):
        for i in range(10):
            print("%s - 지연 %d" % (self.clientname, self.sec))
            time.sleep(self.sec)
        
        
clientA = threading.Thread(target = client_thread, args = ("clientA", 0.1))
clientB = threading.Thread(target = client_thread, args = ("clientB", 0.1))
clientC = threading.Thread(target = client_thread, args = ("clientC", 2.0))
clientD = threading.Thread(target = client_thread, args = ("clientD", 0.1))
clientE = threading.Thread(target = client_thread, args = ("clientE", 0.1))
clientF = threading.Thread(target = client_thread, args = ("clientF", 0.1))
clientG = threading.Thread(target = client_thread, args = ("clientG", 0.1))
clientH = threading.Thread(target = client_thread, args = ("clientH", 1))

threading.Thread()

clientA.start()
clientB.start()
clientC.start()
clientD.start()
clientE.start()
clientF.start()
clientG.start()
clientH.start()
