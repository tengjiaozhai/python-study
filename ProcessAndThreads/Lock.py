# 线程锁
# multithread
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    with lock:
        balance = balance + n
        balance = balance - n

def run_thread(n):
    for i in range(10000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(8,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
