#!/usr/bin/python3
import os
import psutil
import signal
from sys import argv
from threading import Thread
from multiprocessing import Process
import threading
import time
import utils
from utils import print_links
from utils import alert_found
from wikipedia import page
import wikipedia

target = argv[2]
did_find = False
def search(links, parent=None):
    """   """
    if target in links:
        print('\n**************FOUND******************')
    else:
        for link in links:
            _links = page(link).links
            p = Process(target=search, args=(link))
            p.start()
def main():
    """   """
    start = argv[1]
    target = argv[2]
    print('Loading links...')
    links = page(start).links
    utils.print_heading(start, target, 50)
    print_links(start, 5)

    p1 = Process(target=search, args=(links, False))
    p1.start()

if __name__ == '__main__':
    start = argv[1]
    target = argv[2]
    main()
