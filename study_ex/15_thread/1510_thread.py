import threading
import time

MAKE_CNT = 10

def make_product(maker, maker_id):
    maked_produnct = 0
    while maked_produnct < 5000000:
        maked_produnct += 1

"""
싱글 스레드
"""
print("[싱글 스레드 시작]")
start_time = time.time() 

for i in range(MAKE_CNT):
    make_product(str(i+1), i)

single_time = time.time() - start_time
print("[종료 스레드 시작]")

"""
멀티 스레드
"""
print("[멀티 스레드 시작]")
start_time = time.time() 

client = []
for i in range(MAKE_CNT):
    # Thread를 만들어서 저장함.
    client.append(threading.Thread(target = make_product, args = (str(i+1), i)))

# 만든 Thread 실행
for i in range(MAKE_CNT):
    client[i].start()

for i in range(MAKE_CNT):
    client[i].join()

thread_time = time.time() - start_time
print("[멀티 스레드 시작]")
print("싱글: %0.4f | 멀티: %0.4f" % (single_time, thread_time))
