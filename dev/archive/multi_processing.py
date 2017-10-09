#!/usr/bin/python3
import multiprocessing

def worker():
    """worker function"""
    name = multiprocessing.current_process().name
    print ('Worker: {}'.format(name))
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()

