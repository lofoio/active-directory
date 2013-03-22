#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import xlrd, xlwt, re
with open( "computers.txt", 'r') as pathfile:
    tlist = pathfile.readlines()
newl = []
for t in tlist:
    newl.append(t.split("%"))
print len(newl)

wbk = xlwt.Workbook()
sheet = wbk.add_sheet("sheet0")
for i, itm in enumerate(newl):
    for j, jtm in enumerate(itm):
        sheet.write(i,j,jtm.decode('cp936'))
        # print jtm,type(jtm)

# with open( "test.txt", 'w') as testfile:
#     testfile.w
wbk.save('output.xls')
