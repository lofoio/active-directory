#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pdb
from docx import Document
doc = Document('test.docx')
# doc.numbering_part
pdb.set_trace()
for t in doc.paragraphs:
    print(t.text)
