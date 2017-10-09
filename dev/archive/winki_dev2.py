#!/usr/bin/python3
from multiprocessing import Process, current_process as this_p
import multiprocessing as mp
from wikipedia import page
import sys
import time
import os
import random

os.environ['FOUND'] = 'FALSE'
jobs = []
def search(links, target, i, did_find=False, parent=None):
    """   """
    if os.getenv('FOUND') == 'TRUE':
        parent.terminate()
        this_p.join()
    if did_find == True:
        pass
    i += 1
    print(links)
    for link in links:
        p_name = this_p().name
        print('P_NAME: {}'.format(p_name))
        _links = page(link).links
        print(_links)
        if target in _links:
            did_find = True
            os.environ['FOUND'] = 'TRUE'
            print('FOUND\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nFOUND')
            raise Exception
            for i in range(len(jobs)):
                try:
                    jobs[i].terminate()
                    this_p().terminate()
                    sys.exit(0)
                except:
                    sys.exit(0)
                
        if did_find == False:
            #        if os.getenv('FOUND') == 'FALSE':
            jobs.append(this_p())
            p = Process(target=search, args=(_links, target, i, did_find, this_p())).start()            
            #            p.start()
        else:
            print('??????????????????????????????????????????????????? DID_FIND = {}'.format(did_find))
            try:
                this_p().terminate()
            except:
                return

def start(start, target):
    """   """
    i = 0

    ncpu = mp.cpu_count()
    p = mp.Pool(ncpu)
    print('STARTING****************************************************************')
    links = page(start).links
    did_find = False
#    for i in range(ncpu):
#        p.apply_async(search, args=(links, target, i, did_find), callback=quit)
#    p.close()
#    p.join()

    search(links, target, i, did_find)

def worker(i):
    print ("%d started" % i)
    while True:
        x = random.random()
        print ('%d found %g' % (i, x))
        if x > 0.95:
            return x # triggers callback
        sleep(0.5)

def quit(arg):
    print("quitting with {}".format(arg))
    # note: p is visible because it's global in __main__
    arg.terminate()  # kill all pool workers

if __name__ == '__main__':
    start(sys.argv[1], sys.argv[2])
