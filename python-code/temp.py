#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as BSoup
from urllib.request import urlopen
import sys, re
html = "<p id='1' >hello</p><h1>hello</h1>"
def f(tag, *args):
    if "id" in tag.attrs:
        print(tag)
a = BSoup(html)
# c = a(f)
code = compile("lambda tag: tag.name == 'p'", '<string>', 'exec')
c = a(lambda tag: tag.name == "p")
