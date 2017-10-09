#!/usr/bin/python3
from threading import Thread
import threading
import time
from sys import argv as args
from utils import print_links as l
from utils import *
import wikipedia
from wikipedia import page

def main():
    global did_find
    global start
    global target
    global searched_links
    global path_nodes

    did_find = False;
    start = args[1];
    target = args[2];
    searched_links = [];
    links = page(start).links;
    mt = Thread(target=start_search, args=(links, ));
    path_nodes = {}

    print_heading(start, target, 50)
    mt.start();
    while did_find == False:
        time.sleep(0)

#    print('OPEN THREADS: {}'.format(threading.enumerate()))
    path = build_path()
    print_path(path)

def start_search(links):
    t = Thread(target=search, args=(start, links, target))
    t.start();
    t.join();

def search(node, links, target, parent=None):
    global did_find

    if did_find:
        return;
    if node not in searched_links and did_find == False:
        searched_links.append(node);
        page_title('=', parent, node, len(node))
        path_nodes[node] = parent
        if did_find:
            return
        if target in links:
            did_find = True;
            alert_found(target)
            path_nodes[target] = parent
            print(path_nodes)
            return;
        else:
            for link in links:
                if did_find:
                    return;
                try:
                    _links = page(link).links
                except wikipedia.exceptions.DisambiguationError as e:
                    continue
                time.sleep(1)
                t = Thread(target=search, args=(link, _links, target, node));
                if did_find:
                    return;
                t.start()
                # TODO: add listener here to join or exit this thread when did_find == true

def print_path(path):
    string = ''
    for (i, link) in enumerate(path):
        string += link
        if i < len(path)-1:
            string += ' --> '

    print(string)

def build_path():
    rev_path = []
    node = target
    while node is not None:
        rev_path.append(node)
        parent = path_nodes[node]
        node = parent
    path = []
    for i in range(len(rev_path)):
        path.append(rev_path[-1-i])
    return path;
    
if __name__ == '__main__':
    main();
