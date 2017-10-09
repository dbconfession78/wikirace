#!/usr/bin/python3
from wikipedia import page
import wikipedia
import multiprocessing

w_page = wikipedia.page('Cucumber')
target = 'Mikhail Lazarev'
links = w_page.links
path = []
pos = 0
cyc_count = 0


def start(links):
    for link in links:
        for sub_link in wikipedia.page(link).links:
            search(sub_link)


def search(links):        
    for i in range(5):
        page_links = wikipedia.page(links[i]).links
        print(page_links)
        if 'bean' in links:
            input('YUP!')

start(links)
# Cucumber, Continent, Antarctica, Mikhail Lazarev
