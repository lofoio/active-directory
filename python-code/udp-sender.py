#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import socket, sys, os
infile = sys.argv[1]
if not os.path.isfile(os.path.join(os.path.abspath('.'), infile)):
    print "file dose not exist."
    sys.exit()
with open(infile, 'r') as tp:
    ts = tp.read()
sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sc.sendto(ts, ('<broadcast>', 1230))
#ssh -N -L 1061:192.168.5.130:1060 kenaniah
