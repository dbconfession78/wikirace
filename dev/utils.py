#!/usr/bin/python3
import wikipedia

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


def page_title(decorator, parent, page_name, width):
    line1 = '{}\n{} (from: {})\n{}'.format(decorator * width, page_name, parent, decorator * width)

    print('')
    print(line1)

def alert_found(link):
    print(('*' * 10) + '\aFOUND:  {}'.format(link) + '*' * 10)
