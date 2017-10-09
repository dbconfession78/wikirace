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
    try:
        links = page(start).links;
    except:
        print('ERROR: unable to get links')
        exit(1)
    run_thread = Thread(target=run, args=(links, ));
    path_nodes = {}

    print_heading(start, target, 50)
    run_thread.start();
    while did_find == False:
        time.sleep(0)

    path = build_path(target, path_nodes)
    print_path(path)
    print('\nCleaning up...')
    time.sleep(5)
    print('Exiting...')
    exit(0)

def run(links):
    t = Thread(target=search, args=(start, links, target))
    t.start();
    t.join();

def search(node, links, target, parent=None):
    global did_find

    if did_find:
        return;
    if node not in searched_links and did_find == False:
        searched_links.append(node);
        print_page_title('=', parent, node, len(node))
        path_nodes[node] = parent
        if did_find:
            return
        if target in links:
            did_find = True;
            alert_found(target)
            path_nodes[target] = parent
            return;
        else:
            for link in links:
                if did_find:
                    return;
                try:
                    _links = page(link).links
                except wikipedia.exceptions.DisambiguationError as e:
                    continue
                except ConnectionError as e:
                    time.sleep(2)
                    _links = page(links).links
                time.sleep(0.8)
                t = Thread(target=search, args=(link, _links, target, node));
                if did_find:
                    return;
                t.start()
    
if __name__ == '__main__':
    main();
