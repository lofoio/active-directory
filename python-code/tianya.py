#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as BSoup
from urllib.request import urlopen
import subprocess, sys, re

myurl = 'http://bbs.tianya.cn//list-worldlook-1.shtml'
tyadm = 'http://bbs.tianya.cn/'
with urlopen(myurl) as mypage:
    tianya_w = BSoup(mypage.read())
mytds = tianya_w.findAll('td')[0::5]
myas = [ td.a for td in mytds ]

print("Post-list is ready.")
myvstg = ""
i = 0
for t in myas:
    i += 1
    print(i)
    myurl = tyadm + t['href']
    with urlopen(myurl) as mypage:
        tianya_w = BSoup(mypage.read())
    myvstg += t.text
    myvstg += tianya_w.find('div', 'atl-info').find('span').text
    myvstg += tianya_w.find('div', 'atl-content').find('div', 'bbs-content clearfix').text
    postlist = tianya_w('div', { "class" : "atl-item", "id" : True })
    pat = re.compile(".*(----|====|[*]{4}|___)")
    spam = re.compile("前列腺|http:")
    for li in postlist:
        ts = li.find('span').text
        tq = li.find('div', 'bbs-content').text
        if re.search( spam , tq ):
            continue
        myvstg += ts + re.sub( pat, "", tq )

myvstg = re.sub(re.compile('\s+'), '', myvstg)
with open('/home/wangdian/tianya.txt', 'w', encoding='utf-8') as tfile:
    tfile.write(myvstg)

# mycmd = '/usr/bin/ekho'
# myarg = ' -s 60 -f postlist.txt'
# try:
#     retcode = subprocess.call(mycmd + myarg, shell=True)
#     if retcode < 0:
#         print("Child was terminated by signal", -retcode, file=sys.stderr)
#     else:
#         print("Child returned", retcode, file=sys.stderr)
# except OSError as e:
#     print("Execution failed:", e, file=sys.stderr)




















# f.write(u'\u5b57'.encode('utf-8'))
# myurl = 'file:////home/wangdian/tianya.shtml'
# print tianya_w.td ; the first one.
# http://lobstertech.com/python_unicode.html
# encodings前列腺
# hreflist = [ tyadm +  t['href'] for t in myas ]
# postlist = [ t.text for t in myas ]
# with open('postlist.txt', 'w', encoding='utf-8') as tfile:
#     tfile.write('\n'.join(postlist))
