#!/usr/bin/python3
import os
import psutil
import signal
from sys import argv
from threading import Thread
import threading
import time
import utils
from utils import print_links
from utils import alert_found
from wikipedia import page
import wikipedia

did_find = False
def search(links, target, did_find, parent=None):
    """   """
    if (target in links):
        alert_found(target)
        #        print('\aFOUND: {}'.format(target))
        return

    for link in links:
        print('{}: {}'.format(threading.currentThread().getName(), link))
        _links = page(link).links
        print_links(link, 5)
        if target in _links:
            aler_found(target)
            #            print('\aFOUND: {}'.format(target))
            did_find = True
            break;
        search_thread = Thread(target=search, args=(_links, target, did_find)).start()

def main():
    """   """
    start = argv[1]
    target = argv[2]
    print('Loading links...')
    links = page(start).links
    utils.print_heading(start, target, 50)
    print_links(start, 5)
    search(links, target, False)

if __name__ == '__main__':
    start = argv[1]
    target = argv[2]
    main()
