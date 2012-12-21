#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import socket, sys, datetime
PORT = 1230
MAX = 65535
SERVERADDR = sys.argv[-1] if len(sys.argv) == 2 else ''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print "udp socket init", s.getsockname() #('0.0.0.0', 0)
print 'PORT is set to %d' % PORT, ", So"
s.bind((SERVERADDR, PORT))
print "after bind", s.getsockname() #('0.0.0.0', PORT)
while True:
    data, clientaddr = s.recvfrom(MAX)
    print "!!! Server can obtain data and address of client by recvfrom().\n", repr(data), clientaddr, "that can be used to reply." #('127.0.0.1', 45335)
    tf = open(datetime.datetime.now().strftime("%d-%H-%M-%S"), 'w')
    tf.write(data)
    tf.close()

#usage: client command: sc.sendto('hello from sc', ('', 1230))
#sc.connect() is optional for convenience.
