#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pdb
import urllib
from urllib.request import urlopen
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = 'http://bbs.hupu.com/'
password_mgr.add_password(None, top_level_url, 'roover', '020919')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open('http://bbs.hupu.com/kfq')
urllib.request.install_opener(opener)
