#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as BSoup
from urllib.request import urlopen
import subprocess, sys, re

def headlists(forumname):
    """headlists(forumname) ---> headlines url list.

    Arguments:
    - `forumname`: forum name.
    """
    forumsdir = {"cjdby" : "http://lt.cjdby.net/forum-112-1.html",
                 "tianya" : "" }
    turl = forumsdir[ forumname ]
    with urlopen(turl) as mypage:
        bsobj = BSoup(mypage.read())
    myas = { "cjdby" : lambda bsobj: bsobj('a', 'xst')[7:],
             "default" : lambda bsobj: bsobj('a', 'xst')[7:],
             }.get(forumname, "default")(bsobj)
    return myas

myas = headlists("cjdby")

myvstg = ""
i = 0
allists = "\n".join([ t.text for t in myas ])
print(allists)
for t in myas:
    i += 1
    print(i)
    myurl = t['href']
    with urlopen(myurl) as mypage:
        bsobj = BSoup(mypage.read())
    myvstg += '标题: ' + t.text
    postlist = bsobj('td', { "class" : "t_f", "id" : True })
    authlist = bsobj(lambda tag: tag.name == 'a' and "class" in tag.attrs and len(tag["class"]) == 1 and tag["class"][0] == "xw1")
    for a, p in zip(authlist, postlist):
        ts = "作者: " # + a.text
        tq = ''.join( p.findAll(text=True, recursive=False) )
        myvstg += ts + tq[:200]

myvstg = re.sub(re.compile('\s{2,}'), ' ', myvstg)
with open('/home/wangdian/cjdby.txt', 'w', encoding='utf-8') as tfile:
    tfile.write(allists)
    tfile.write(myvstg)
