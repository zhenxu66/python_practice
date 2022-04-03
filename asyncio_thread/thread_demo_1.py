import threading
from time import sleep, ctime
# thread created object, create thread from start(), ended when the function finish, which start first, randomly
# Add sleep in main after thread start() to let is run and finish, use sleep wait to arrange which one run first
# main thread will close memory after this thread finish

def job1():
    for i in range(2):
        print('job1 is runnning %d\n' % i)
        sleep(1)

def job2():
    for i in range(5):
        print('job2 is runnning %d\n' % i)
        sleep(1)

def main():
    print('---starting----: %s' % ctime())
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    # sleep(1)
    # print("job1 Thread stop/n")
    t2.start()
    # sleep(1)
    # print("job2 Thread stop/n")
    # print(threading.enumerate())
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) == 3:
            print("all three threads are running")
        elif len(threading.enumerate()) == 2:
            print("only two threads are running")
        elif len(threading.enumerate()) == 1:
            print("only one thread is running, quit")
            break
        sleep(1)


if __name__ == "__main__":
    main()