#!/usr/bin/python3
from wikipedia import page
import wikipedia
import multiprocessing
import threading
from multiprocessing import Process
import sys
import time
from multiprocessing import current_process as current

jobs = []
top_job = ''
pool = multiprocessing.Pool
def search(links, node, target, i, flag, parent=None):
    """   """
    if parent is not None:
        parent.join()
    this_p = multiprocessing.current_process()
    for link in links:           
        print(links)
        p_name = multiprocessing.current_process().name
        print('Worker: {}'.format(p_name))
        set = wikipedia.page(link).links
        p = Process(target=search, args=(set, node, target, i, flag, this_p))
        jobs.append(p);
        if target in set:
            this_p.join()
        else:
            p.start()

def kill_all_jobs():
    for job in jobs:
        job.join()

def start():
    flag = 0
    search(links, sys.argv[1], sys.argv[2], i, flag)

if __name__ == '__main__':
    links = wikipedia.page(sys.argv[1]).links
    jobs = []
    i = 0;
#    main_handle = Process(target=start)
    top_job = "main_handle.name"
#    main_handle.start()
    start()

