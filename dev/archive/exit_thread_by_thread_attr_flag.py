#!/usr/bin/python3
from threading import Thread
import threading
import time


def main():
    t = Thread(target=func1, args=('A_JOB', ))
    t.start();
    time.sleep(5)
    t.do_run = False
    t.join();


def func1(arg):
    _t = threading.currentThread();
    while getattr(_t, 'do_run', True):
        print('working on: {}'.format(arg));
        time.sleep(1);

if __name__ == '__main__':
     main();
