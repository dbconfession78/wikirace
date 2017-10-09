#!/usr/bin/python3
from multiprocessing import Process, Pipe, current_process as cp
import psutil, signal, os, multiprocessing as mp
from wikipedia import page
import wikipedia
import time
from my_process import MyProcess
from sys import argv
import utils
import os

os.environ['DID_FIND'] = 'False'
def search(links, target, did_find, parent=None):
    """   """
    print(cp().name)
    if os.getenv('DID_FIND') == 'True':
        return

    if (target in links):
        print('\aFOUND')

    for link in links:
        utils.print_page_name('.', link, 5)
        utils.print_links(link, 5)
        _links = page(link).links
        if target in _links:
            print('\aFOUND')
            #            parent.join()
            #            cp().terminate()
            os.environ['DID_FIND'] = 'True'
            did_find = True
            break;

        # search should return  did_find
        # so that each parent search knows to exit.
        p = Process(target=search, args=(_links, target, did_find, cp()))
        p.start()
        if did_find:
            p.join()


def main():
    """   """
    start = argv[1]
    target = argv[2]
    links = page(start).links
    utils.print_heading(start, target, 50)
    search(links, target, False)

if __name__ == '__main__':
    start = argv[1]
    target = argv[2]
    main()
#    search(start, target)
