#!/usr/bin/python3
from threading import Thread
import threading
import time

exitFlag = 1;

class MyThread(Thread):
    def __init__(self, threadID, name, counter):
        Thread.__init__(self)
        self.threadID = threadID;
        self.name = name;
        self.counter = counter;
    def run(self):
        print('Starting {}'.format(self.name));
        print_time(self.name, self.counter, 5);
        print('Exiting {}'.format(self.name));

def print_time(threadName, delay, counter):
    while (counter):
        if exitFlag:
            print('----------------------------------');
            self.exit()
        time.sleep(delay);
        print('{}: {}'.format(threadName, time.ctime(time.time())));
        counter -= 1;


thread1 = MyThread(1, "Thread-1", 1);
thread2 = MyThread(2, "Thread-2", 2);
thread1.start();
thread2.start();
thread1.join();
thread2.join();
print('Exiting Main Thread');

# def main():
  #  t = Thread(target=func1, args=())
  #  t.start();
  #  print(threading.activeCount())
  #  print(threading.currentThread())
  #  print(threading.enumerate())
  #  print('YUP!')

def func1():
    count = 0;
    while (count < 3):
        print(threading.currentThread().name);
        threading.currentThread().terminate();


# if __name__ == '__main__':
#     main();
