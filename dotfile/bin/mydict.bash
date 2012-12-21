#!/usr/bin/env bash
# -*- coding:utf-8 -*-
sdcv -u 'Merriam-Webster Collegiate Dictionary' -n "$1" | sed 's/\(.*\)\(<TABLE.*<\/TABLE>\)\(.*\)/\3\2/' | w3m -dump -T text/html