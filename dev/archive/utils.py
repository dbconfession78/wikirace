#!/usr/bin/python3
import wikipedia

def print_links(p, n=None):
    """
    p: the  page to display links from
    n: number of links to show form page
    """
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


def page_title(decorator, page_name, width):
    line1 = '{} {} {}'.format(decorator * width, page_name, decorator * width)

    print('')
    print(line1)

def alert_found(link):
    print(('*' * 10) + '\aFOUND:  {}'.format(target) + '*' * 10)
