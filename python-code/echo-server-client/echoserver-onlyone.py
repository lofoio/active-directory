#!/usr/bin/env python

"""
An echo server that can only serve one client at a time
"""

import socket

host = ''
port = 500005
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    running = 1
    while running:
        data = client.recv(size)
        if data:
            client.send(data)
        else:
            running = 0
    client.close()
