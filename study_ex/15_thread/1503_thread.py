import threading  # Thread를 사용하기 위해서 가져오기
import time       # time.sleep() 사용


def client_thread(clientname, sec):
    for i in range(10):
        print("%s - 지연 %d" % (clientname, sec))
        time.sleep(sec)


# threading.Thread를 활용 | target은 사용하고자 하는 method명 | args는 전달하고자 하는 매개변수)
clientA = threading.Thread(target = client_thread, args = ("clientA", 0.1))
clientB = threading.Thread(target = client_thread, args = ("clientB", 0.1))
clientC = threading.Thread(target = client_thread, args = ("clientC", 2.0))
clientD = threading.Thread(target = client_thread, args = ("clientD", 0.1))
clientE = threading.Thread(target = client_thread, args = ("clientE", 0.1))
clientF = threading.Thread(target = client_thread, args = ("clientF", 0.1))
clientG = threading.Thread(target = client_thread, args = ("clientG", 0.1))
clientH = threading.Thread(target = client_thread, args = ("clientH", 1))

# 만들어둔 Thread 실행
clientA.start()
clientB.start()
clientC.start()
clientD.start()
clientE.start()
clientF.start()
clientG.start()
clientH.start()
