#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from lxml import etree
from urllib.request import urlopen
import sys, re

class ForumClipper(object):
    def __init__(self, forumn="cjdby"):
        self.headlines = []
        with open( forumn + ".xml", 'r') as pathfile:
            self.pathlist = [ li for li in pathfile.readlines()
                                if not li.startswith("#") and
                                li.strip()]
        self.forumurl = self.pathlist[0]
        self.hpath    = self.pathlist[1]
        self.compath  = self.pathlist[2]
        self.cathpth  = self.pathlist[3]
        self.forumstring = ""
        self.comreg   = re.compile("\s+")

    def popen(self, turl):
        with urlopen(turl) as mypage:
            return etree.HTML(mypage.read())

    def __objfond(self, treeobj, objpath):
        return treeobj.xpath(objpath)

    def getheadlines(self):
        treeobj = self.popen(self.forumurl)
        myas = self.__objfond(treeobj, self.hpath)
        self.headlines = [ (t.text, t.attrib["href"]) for t in myas[7:] ]

    def getcomments(self, turl):
        treeobj = self.popen(turl)
        comments = self.__objfond( treeobj, self.compath)
        comauths = self.__objfond( treeobj, self.cathpth)
        return comauths, comments

    def alltostring(self):
        self.forumstring = "\n".join([ t[0] for t in wd.headlines]) + "\n"
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
        with open('/home/wangdian/cjdby.txt', 'w', encoding='utf-8') as tfile:
            tfile.write(re.sub(self.comreg, " ", self.forumstring))

# wd = ForumClipper()
# wd.getheadlines()
# purl = wd.headlines[10][1]
# a, b = wd.getcomments(purl)
# wd.alltofile()
# for a, c in zip(self.getcomments(t[1])):
if __name__ == '__main__':
    wd = ForumClipper()
    wd.getheadlines()
    wd.alltofile()
