#!/usr/bin/python3
import multiprocessing as mp
from multiprocessing import Process
import os
import psutil
import signal
import sys
import time
from wikipedia import page, exceptions

target = sys.argv[2]
did_find = False

def main():
    global target, did_find

    links = page(sys.argv[1]).links
    manager = mp.Manager()

    did_find = search(links)
    input('%^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

def search(links, did_find=False):
    print('TOP DID_FIND: {}'.format(did_find))
    if did_find:
        kill_all(mp.current_process())
        mp.current_process().terminate()
        #        return kill_all(mp.current_process())


#    print(links)
    if (target in links):
        print('****************************FOUND *********************************!')
        did_find = True
        _links = []
        
    for (i, link) in enumerate(links):
        if link == '-1 (number)':
            continue
        print('------------> {}'.format(link))
        try:
            _links = page(link).links
        except exceptions.DisambiguationError as e2:
            print("Error: {0}".format(e2))
            continue

        if (target in _links) or did_find:
            print('****************************FOUND *********************************!')
            did_find = True
        print('BOTTOM DID_FIND: {}'.format(did_find))
        #if did_find:
         #   p = Process(target=search, args=([], True))
          #  p.start()
        #else:
        p = Process(target=search, args=(_links, did_find))
        p.start()
#            p.join()

        exit(0)

            


def worker(procnum, return_dict):
    '''worker function'''
    print(str(procnum) + ' represent!')
    return_dict[procnum] = procnum

def kill_all(p):
    for child in psutil.Process(p.pid).children(recursive=True):
        child.kill()
    os.kill(p.pid, signal.SIGKILL)
    p.join()
    

def page_links(p, n=None):
    """ 
    p: the  page to display links from 
    n: number of links to show form page
    """
    import wikipedia
    links = wikipedia.page(p).links
    print(links[0:n])
    return(links[0:n])

if __name__ == '__main__':
    main()

