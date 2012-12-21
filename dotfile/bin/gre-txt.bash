#!/bin/bash
gb2utf8.bash $1
blkrm.bash ${1%.*}.utf
sed -e 's/^[^a-zA-Z]*\]//' -e 's/[ \t]*\[.*\]//' ${1%.*}.utf \
 | awk 'BEGIN{oldline = ""}
 {
 if ( $0 ~ /^[a-z]*$/ ) { oldline = $0 }
 else { printf "%-20s %s\n", oldline , $0 }
 }' \
> ${1%.*}.txt
rm -rf ${1%.*}.utf
echo " $1 ----> ${1%.*}.txt "
# if ( $0 ~ /^[a-z]*$/ ) { oldline = $0 }
# else { printf "%-20s %s\n", oldline , $0 }