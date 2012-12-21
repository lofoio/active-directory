#!/usr/bin/env python
# -*- coding:utf-8 -*-
abnormallist = ["\n", "\t", " ", "\r\n"]
cleanlist = [elem.strip() for elem in abnormallist if elem.strip()]
templist = [elem.strip() or None  for elem in abnormallist]
t1 = [elem.strip() and None  for elem in abnormallist]
