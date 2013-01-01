#!/usr/bin/env bash
# -*- coding:utf-8 -*-
cython2 $1.pyx
gcc -c -fPIC -I/usr/include/python2.7/ $1.c
gcc -shared $1.o -o $1.so
