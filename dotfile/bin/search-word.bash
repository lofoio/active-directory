#!/bin/bash
cd /home/badegg/Movies/english/bbc-news 
grep -Ei -m 3 -B 10 -A 10 "$1" *.lrc   \
| sed  -f /home/badegg/bin/schprc.sed  \
| sed -n -e /"$1"/'{$!N;p}' #short for | sed -n -e /"$1"/'{${p;b end};N;p;:end}' \
                            #$! negates $
