#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from lxml import etree
with  open( "test.xml", 'r') as f:
    tree = etree.parse(f)
