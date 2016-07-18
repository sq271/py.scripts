#!/usr/bin/python

# httpget.py

import socket
import sys


if len(sys.argv) != 2:
    print("httpget.py <target>")
    sys.exit(1)


host = sys.argv[1]
port = 80
data = "GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % host


def get(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(data.encode())
    response = s.recv(4096)
    print(response)


if __name__ == '__main__':
    get(host, port)

