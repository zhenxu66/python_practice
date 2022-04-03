#coding=utf-8
# after run method finish, Thread finish, with lots of complicated functions

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)
        self.test()
    def test(self):
        print("hello")

if __name__ == "__main__":
    t = MyThread()
    t.start()
    t.test()