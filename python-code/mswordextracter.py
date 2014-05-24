#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from docx import Document
doc = Document('test.docx')
# doc.numbering_part
for t in doc.paragraphs:
    print(t.text)
