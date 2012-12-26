#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from lxml import etree
from urllib.request import urlopen
import sys, re
class ForumClipper:
    def __init__(self, turl=""):
        self.forumurl = turl
        self.comreg   = re.compile("\s+")
        self.headlines = []
        self.forumstring = ""

    def setup(self, forumn="cjdby"):
        self.forumn = forumn
        with open( self.forumn + ".xml", 'r') as pathfile:
                self.config = etree.fromstring(pathfile.read())
        self.forumurl = self.config.xpath("/domain")[0].text
        self.hpath    = self.config.xpath("/domain/headlinelist")[0].text
        self.hbase    = self.config.xpath("/domain/headlinelist/hbase")[0].text or ""
        self.ntheads  = int(self.config.xpath("/domain/headlinelist/nthds")[0].text or "0")
        self.compath  = self.config.xpath("/domain/posts/comments")[0].text
        self.cathpth  = self.config.xpath("/domain/posts/authors")[0].text
        print(self.forumurl)

    def __open(self, turl):
        with urlopen(turl) as mypage:
            return etree.HTML(mypage.read())

    def __objfond(self, treeobj, objpath):
        return treeobj.xpath(objpath)

    def getheadlines(self):
        treeobj = self.__open(self.forumurl)
        myas = self.__objfond(treeobj, self.hpath)
        self.headlines = [ (t.text, self.hbase + t.attrib["href"]) for t in myas[self.ntheads:] if t.text ]

    def getcomments(self, turl):
        treeobj = self.__open(turl)
        comments = self.__objfond( treeobj, self.compath)
        comauths = self.__objfond( treeobj, self.cathpth)
        return comauths, comments

    def alltostring(self):
        self.forumstring = "\n".join([ t[0] for t in self.headlines]) + "\n"
        i = 0
        for t in self.headlines:
            i += 1
            print("{}:: {}".format(i, t[0]))
            for a, c in zip(*self.getcomments(t[1])):
                ath = "\n作者: " # + a.text
                com = "".join( c.xpath("text()") )[:200]
                self.forumstring += ath + com

    def alltofile(self):
        self.alltostring()
        outfile = '/home/wangdian/' + self.forumn + '.txt'
        with open(outfile, 'w', encoding='utf-8') as tfile:
            tfile.write(re.sub(self.comreg, " ", self.forumstring))

    def calcxpath(self, turl):
        self.elobj = self.__open(turl)
        tree = etree.ElementTree(self.elobj)
        for i in range(2):
            tstrg = input("请输入搜索内容:")
            e = self.elobj.xpath("//*[text()='{}']".format(tstrg))[0]
            tpath = tree.getpath(e)
            txt = "".join(self.elobj.xpath(tpath + "/text()"))
            print("{}\n{}".format(tpath, txt))

if __name__ == '__main__':
    wd = ForumClipper()
    cfg = sys.argv[-1] if len(sys.argv) == 2 else ''
    if cfg:
        wd.setup(cfg)
    else:
        wd.setup()
    wd.getheadlines()
    wd.alltofile()
