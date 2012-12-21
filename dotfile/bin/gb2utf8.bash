#!/bin/bash
iconv -c -f GB18030 -t UTF-8 -o ${1%.*}.utf  $1