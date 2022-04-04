# global parameter threading share same parameter
# use threading Lock, acquire() and release(), need to prevent dead lock
import threading
import time

#global number
g_num = 0

def test1(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        # mutex.acquire()
        g_num += 1  # this can be divided into 3 CPU commands
        # mutex.release()
    mutex.release()
    print("----in test g_num=%d"% g_num)

def test2(num):
    global g_num
    # mutex.acquire()
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    # mutex.release()
    print("----in test g_num=%d"% g_num)

mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()
    time.sleep(0.1)



if __name__ == "__main__":
    main()