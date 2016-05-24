#!/usr/bin/python

# socket_client.py

import socket

def raw_http_get(host, port):
    #request = "GET / HTTP/1.1\nHost: " + host + "\nUser-Agent:Mozilla 5.0\n\n"
    request = raw_input('>> ')

    # creat a socket and connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # send out request in the HTTP prtocol
    s.send(request)

    response = s.recv(1024)
    while response:
        print response,
        response = s.recv(1024)


    s.close()

raw_http_get("192.168.1.184", 50000)


