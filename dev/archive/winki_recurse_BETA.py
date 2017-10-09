#!/usr/bin/python3
import wikipedia
import multiprocessing

w_page = wikipedia.page('Cucumber')
target = 'Mikhail Lazarev'
links = w_page.links
path = []
pos = 0
cyc_count = 0
target_found = False

def start(links):
    for i in range(len(links)):
        p = multiprocessing.Process(target=search, args=(links, pos, cyc_count))
        p.start()

def search(links, pos, cyc_count):        
    page = wikipedia.page(links[0])
    links = page.links
    for i in range(len(links)):
        inc = 5
        cycles = int(len(links) / 5)
        final = len(links) % 5
        last_cyc = len(links)-final
    
        cyc_count += 1
        if (cyc_count == last_cyc):
            new_list = links[pos:final]
        else:
            new_list = links[pos: pos+inc]

        p = multiprocessing.Process(target=search, args=(new_list, pos, cyc_count))
        if (cyc_count == len(links)):
            p.kill()
        p.start()

    # path.append(som) TODO
    if target in links:
        target_found = True;
        return path

    for link in links:
        try:
            n_links = wikipedia.page(link).links
            proc = multiprocessing.Process(target=search(n_links, pos, cyc_count)).start()
        except wikipedia.exceptions.DisambiguationError as e:
            pass
    

class Path():
    def __init__(self, cycle_count, links):
        self.cycle_count = cycle_count

search(links, pos, cyc_count);
