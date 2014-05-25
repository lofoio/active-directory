#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# import pdb
# pdb.set_trace()
try:
    from lxml import etree, html
except ImportError:
    import xml.etree.ElementTree as etree
from urllib.request import urlopen
import sys, re
class ForumClipper:
    def __init__(self, turl=""):
        self.forumurl = turl
        self.comreg   = re.compile("\s+")
        self.headlines = []
        self.forumstring = ""

    def setup(self, forumn):
        self.forumn = forumn or "cjdby"
        with open( self.forumn + ".xml", 'r') as pathfile:
                self.config = etree.parse(pathfile)
        self.forumurl = self.config.xpath("/domain")[0].text
        self.hpath    = self.config.xpath("/domain/headlinelist")[0].text
        self.hbase    = self.config.xpath("/domain/headlinelist/hbase")[0].text or ""
        self.ntheads  = int(self.config.xpath("/domain/headlinelist/nthds")[0].text or "0")
        self.lzcom    = self.config.xpath("/domain/posts/lzcom")[0].text or ""
        self.lzauth   = self.config.xpath("/domain/posts/lzauth")[0].text or ""
        self.compath  = self.config.xpath("/domain/posts/comments")[0].text
        self.cathpth  = self.config.xpath("/domain/posts/authors")[0].text
        self.trash = ""
        self.spams = ""
        print(self.forumurl)

    def __open(self, turl):
        with urlopen(turl) as mypage:
            return html.parse(mypage)

    def __objfond(self, treeobj, objpath):
        return treeobj.xpath(objpath)

    def getheadlines(self):
        treeobj = self.__open(self.forumurl)
        myas = self.__objfond(treeobj, self.hpath)
        self.headlines = [ (t.text, self.hbase + t.attrib["href"]) for t in myas[self.ntheads:] if t.text ]

    def getcomments(self, turl):
        treeobj = self.__open(turl)
        comments = self.__objfond( treeobj, self.lzcom)  if self.lzcom else []
        comauths = self.__objfond( treeobj, self.lzauth) if self.lzcom else []
        comments += self.__objfond( treeobj, self.compath)
        comauths += self.__objfond( treeobj, self.cathpth)
        return comauths, comments

    def alltostring(self):
        self.forumstring = "\n".join([ t[0] for t in self.headlines]) + "\n"
        for i, t in enumerate(self.headlines):
            print("{}:: {}".format(i, t[0]))
            for a, c in zip(*self.getcomments(t[1])):
                ath = "\n作者: " # + a.text
                com = "".join( c.xpath("text()") )[:200]
                self.forumstring += ath + com

    def alltofile(self):
        self.alltostring()
        outfile = '/home/lofoio/' + self.forumn + '.txt'
        with open(outfile, 'w', encoding='utf-8') as tfile:
            tfile.write(re.sub(self.comreg, " ", self.forumstring))

    def getpathbytext(self, turl):
        self.elobj = self.__open(turl)
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
    wd = ForumClipper() ## Note () here.
    cfg = sys.argv[-1] if len(sys.argv) == 2 else ''
    wd.setup(cfg)
    wd.getheadlines()
    wd.alltofile()
# e = self.elobj.xpath("//*[text()='{}']".format(tstrg))[0]
