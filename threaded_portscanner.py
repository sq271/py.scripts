#!/usr/bin/python

# threaded_portscanner.py

import socket
import sys
import threading
from queue import Queue

if len(sys.argv) != 2:
    print("usage: threaded_portscaner.py <target>")
    sys.exit(1)


lock = threading.Lock()
target = sys.argv[1]


def prtscn(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        con = s.connect((target, port))
        with lock:
            print('port', port, 'is open')
        con.close()
    except:
        pass


def threader():
    while True:
        thread = q.get()
        prtscn(thread)
        q.task_done()


q = Queue()


for x in range(200):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()


for port in range(1, 65535):
    q.put(port)


q.join()




