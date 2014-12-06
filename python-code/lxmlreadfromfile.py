#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys, pdb
from lxml import etree
class xmlfilesolver:
    def __init__(self, infile):
        self._infile = infile
        with open( self._infile, 'r') as f:
            self.elobj = etree.parse(f)
    def getpathbytext(self):
        while True:
            tstrg = input("请输入搜索内容:")
            if tstrg == "EOF":
                break
            for e in self.elobj.xpath("//*"):
                t = "".join(e.xpath("text()"))
                if tstrg in t:
                    break
            tpath = self.elobj.getpath(e)
            txt = "".join(self.elobj.xpath(tpath + "/text()"))
            print("{}\n{}".format(tpath, txt))

if __name__ == '__main__':
    # wd = xmlfilesolver(sys.argv[-1]) ## Note () here.
    wd = xmlfilesolver("test.xml")
    pdb.set_trace()
    wd.getpathbytext()
