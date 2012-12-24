#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as BSoup
from urllib.request import urlopen
import sys, re

class ForumSelector(object):
    def __init__(self, forumn):
        self.headlines = {}
        with open( forumn + ".rules", 'r') as rulefile:
            self.forumrules = [ li for li in rulefile.readlines()
                                if not li.startswith("#") and
                                li.strip()]
        self.forumurl = self.forumrules[0]
        self.headrule = self.forumrules[1].split()
        self.comerule = self.forumrules[2].split()
        self.cmauthle = self.forumrules[3].split()

    def __urlopen(self, turl):
        with urlopen(turl) as mypage:
            return BSoup(mypage.read())

    def __objfond(self, bsobj, tname, tclas, *args):
        closure = "lambda tag: "
        wd = [ "tag.name == tname",
              " and tag['class'] == tclas",
              "and tag['id'] == tid"]
        for i in len(args):
            closure += wd[i]
        return bsobj(closure)
        # if len(args) == 1:
        #     tid = args[0]
        #     return bsobj(lambda tag: tag.name == tname and
        #                 "class" in tag.attrs and
        #                  len(tag["class"]) == 1 and
        #                  tag["class"][0] == tclas and
        #                  tag["id"] == tid)
        # elif len(args) == 2:
        #     tid, tpare = args[:2]
        # else
        #     return bsobj(lambda tag: tag.name == tname and
        #                  "class" in tag.attrs and
        #                  len(tag["class"]) == 1 and
        #                  tag["class"][0] == tclas)

    def getheadlines(self):
        bsobj = self.__urlopen(self.forumurl)
        myas = self.__objfond(bsobj, *self.headrule)
        self.headlines = { t.text : t["href"] for t in myas }

    def getcomments(self, turl):
        bsobj = self.__urlopen(turl)
        comments = self.__objfond( bsobj, *self.comerule)
        comauths = self.__objfond( bsobj, *self.cmauthle)
        return comments, comauths
