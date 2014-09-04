#coding=utf-8
__author__ = 'samsung'
import threading
import thread
import time

mylock = 1

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.stopstatus = False

    def run(self):
        global ticket
        global mylock
        while not self.stopstatus:
            if mylock == 1:
                mylock = 0
                if ticket > 0:
                    ticket -= 1
                    print '%s 抢到一张票，现在余票%d' % (self.name, ticket)
                mylock = 1
            time.sleep(0)

    def stop(self):
        self.stopstatus = True

if __name__ == '__main__':
    thread1 = MyThread('售票员1')
    thread2 = MyThread('售票员2')
    thread3 = MyThread('售票员3')
    ticket = 100
    thread1.start()
    thread2.start()
    thread3.start()
    time.sleep(5)
    thread1.stop()
    thread2.stop()
    thread3.stop()
