#!/usr/bin/python3
import wikipedia
import threading
import time

def print_links(p=None, links=None, n=None):
    """
    p: the  page to display links from
    n: number of links to show form page
    """
    if p is None and links is None:
        print('ERROR: Please supply either page title or list of links to print');
        exit();

    if links is None:
        import wikipedia
        links = wikipedia.page(p).links

    print(links[0:n])
#    return(links[0:n])

def print_heading(start, target, width):
    x_width = int((width - 12 - len(start)) / 2)
    line1 = '{}   FROM: {}   {}'.format('*' * x_width, start, '*' * x_width)
    x_width = int((width - 10 - len(target)) / 2)
    line2 = '{}   TO: {}   {}'.format('*' * x_width, target, '*' * x_width)

    print('*' * width)
    print(line1)
    print(line2)
    print('*' * width)
    print('')


def print_page_title(decorator, parent, page_name, width):
    import threading
    line1 = '{}\n{} (from: {})\n{}'.format(decorator * width, page_name, parent, decorator * width)

    print('')
    print(threading.current_thread().name)
    print(line1)

def alert_found(link):
    print('\n' + ('*' * 10) + '\a FOUND:  {} '.format(link) + '*' * 10)

def thread_report():
    """ reports open thread information  """
    
    print('-------------');
    print('THREAD REPORT:')
    print('-------------');
    print('open threads: {}'.format(threading.active_count()))
    print(threading.enumerate())

def print_path(path):
    string = ''
    for (i, link) in enumerate(path):
        string += link
        if i < len(path)-1:
            string += ' --> '
    print(string)

def build_path(target, path_nodes):
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

def cleanup():
    """
    waits for all threads to close threads
    that don't self-join are manually joined
    """

    while threading.active_count() > 1:
        print('manually joining threads');
        for thread in threading.enumerate():
            print('joining: {}'.format(thread.name))
            thread_report()
            if thread is not threading.current_thread():
                thread.join()
                time.sleep(1)
        thread_report()
        time.sleep(1)
