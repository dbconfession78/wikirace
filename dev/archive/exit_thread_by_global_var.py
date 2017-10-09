#!/usr/bin/python3
from threading import Thread
import threading
import time


# getattr(_t, 'do_run', True):
# t.do_run = Falae
def main():
    global should_run
    should_run = True;
    t = Thread(target=func1, args=())
    t.peace = 'hi';
    t.start();
    time.sleep(3);
    should_run = False;


def func1():
    ct = threading.currentThread();
    if (should_run):
        print(ct.getName())
        _t = Thread(target=func1, args=()).start();
    

if __name__ == '__main__':
    should_run = False;
    main();
