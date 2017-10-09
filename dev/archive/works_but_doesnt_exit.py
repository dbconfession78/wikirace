#!/usr/bin/python3
from multiprocessing import Process, Pipe, current_process as cp
import psutil, signal, os, multiprocessing as mp
from wikipedia import page
import wikipedia
import time
from utils import print_links as l
import sys

jobs = []
count = 0
target = sys.argv[2]
did_find = False


class A():
    def __init__(self):
        global did_find
        self.did_find = False
        self.main()

    def pid_info(self):
        print('\n***************')
        print('***************')
        print('{}'.format(cp().name))
        print('pid: {}'.format(cp().pid))
        print('parent pid: {}'.format(cp()._parent_pid))
        print('***************')
        print('***************\n')

    def search(self, links, parent=None):
        """ """
        global jobs, count, target
        #print(links[0:5])
        self.pid_info()

        if target in links:
            self.did_find = True
            print('\a===============\nDID_FIND={}: {}\n==============='.format(self.did_find, target))
            print('EXITING')
            time.sleep(5)
            for p in psutil.Process(p.pid).children(recursive=True):
                child.kill()
            os.kill(p.pid, signal.SIGKILL)
            p.join()
            exit(0)
            for job in jobs:
                print('SHUTTING DOWN: {}'.format(job.name))
                print(job.name)
                time.sleep(1)
                parent.join()
                return
        else:
            print('%%%%%%%%%%%%%%%\nDID_FIND= {}\n%%%%%%%%%%%%%%%'.format(self.did_find))
            if self.did_find == False:
                for link in links:
                    _links = page(link).links
                    p = Process(target=self.search, args=(_links, mp.current_process()))
                    jobs.append(p)
                    p.start()
            #        p.join()
            else:
                return

    def main(self):
        """ """
        print('main process: {}'.format(os.getpid()))
        links = wikipedia.page(sys.argv[1]).links
        print('*********************** STARTING ******************************')
        print(links)
        self.search(links)

if __name__ == "__main__":
    A()
