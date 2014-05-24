#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, sys
# for t in os.listdir('.'):
#     if sys.argv[1] in t:
#         a = os.stat(t).st_size/(1024*1024)
#         print("{:.1f}M".format(a),t)
for t in sys.argv[1:]:
    a = os.stat(t).st_size/(1024*1024)
    print("{:.1f}M".format(a),t)
