#!/usr/bin/python3
from multiprocessing import Process, Pipe

def my_function(conn):
    """ child process sends inp obj to parent, then parent call it  """
    conn.send(input)

def main():
    parent_conn, child_conn = Pipe()
    p = Process(target=my_function, args=(child_conn, ))
    p.start()
    parent_conn.recv()() # <-- parent recieves input from child and runs as input()
    p.join()

if __name__ == "__main__":
    main()
