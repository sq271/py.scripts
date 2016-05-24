#!/usr/bin/python

# threaded_tcpd.py


import socket
import threading
import sys


if len(sys.argv) != 3:
    print('threaded_tpcd.py <ip> <port>')
    sys.exit(1)


bind_ip = sys.argv[1]
bind_prt = int(sys.argv[2])


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Incoming: " + request.decode())
    client_socket.send(b'ACK')
    client_socket.close()


def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_prt)) 
    server.listen(9)
    print("[*] Listening on %s:%d" % (bind_ip, bind_prt))

    
    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
        client_handler = threading.Thread(target=handle_client, args=(client, ))
        client_handler.start()

if __name__ == '__main__':
    tcp_server()


