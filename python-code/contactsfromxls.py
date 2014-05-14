#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import vobject, xlrd, xlwt, re

def create_vcard( name, mobile_number ):
    j = vobject.vCard()
    j.add('n')
    j.n.value = vobject.vcard.Name( family=name[0], given=name[1:] )
    j.add('fn')
    j.fn.value = name

    tel = j.add("tel")
    tel.type_param = "CELL"
    tel.value = mobile_number

    return j.serialize()

data = xlrd.open_workbook('t.xls')
sh0 = data.sheets()[0]
nrows = sh0.nrows
ncols = sh0.ncols

ns = sh0.col_values(0)
tels = sh0.col_values(1)
shortels = sh0.col_values(2)
with open( "new.vcf", 'w') as outfile:
    for n, t in zip(ns,tels):
        if not t:
            continue
        outfile.write(create_vcard(n, str(int(t))))

    for n, t in zip(ns,shortels):
        if not t:
            continue
        # print n, n + u"短号"
        outfile.write(create_vcard(n + u"短号", str(int(t))))
