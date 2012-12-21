#!/bin/bash
#blkrm.bash "$1"
#sed  -n -e '/^\[[0-9:.,]+\]/{x;s/\n//g;p;d}' -e 'H' "$1"
sed  -n -e '/^\[[0-9:.,]+\]/{x;s/\n//g;p;d}'  "$1"