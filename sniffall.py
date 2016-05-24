#!/usr/bin/python

# sniffall.py

import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

while True:
    print(s.recvfrom(65565))
