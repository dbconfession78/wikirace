def search(links, target, obj):
    obj = Obj()
    for link in links:
        if (target in links):
            obj.path.appen(link)
            return
        n_links = wikipedia.page.links(link)
        p = multiprocessor.Process(target=search(n_links, target, obj))
        if (target_found):
            p.stop()
        else:
            p.start()

        obj.path.append(link)

class Obj():
    path = []
