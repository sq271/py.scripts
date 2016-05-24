#!/usr/bin/python
#

import socket

HOST = '0.0.0.0'
PORT = 50000

def server():
    print "Starting network server on:", socket.gethostname()

    buffersize = 4 * 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    s.listen(5)

    while True:
        client, address = s.accept()

        data = client.recv(buffersize)
        print "recieved from:", client
        print data

        send_output(client, data)
        client.close()
def send_output(client_socket, in_data):
   #
   # client_socket.send('HTTP/1.1 200 OK\r\n')
   # client_socket.send('Content-type: text/html\r\n\r\n')
   # client_socket.send('Hola!')

server()

