#!/usr/bin/env bash
# -*- coding:utf-8 -*-
xargs -t -I{} cp -r {} . < $1 && echo "DONE"