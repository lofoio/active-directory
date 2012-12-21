#!/bin/bash
if [ -z "$1" ] || [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
echo "Usage: blkrm.bash <file to be refined>"
exit 0
fi
if [ ! -e "$1" ] ; then
echo "file does not exist."
exit 0
fi
sed -e 'y/\t/ /' \
    -e 's/\r//'  \
    -e '/^ *$/d' \
    -e 's/^ *//' \
    -e 's/ *$//' \
"$1" > "$1.bak"
mv "$1.bak" "$1"
echo ""$1" done."
#awk 'NF > 0' data kill blank lines
#          awk 'END { print NR }' data
#          awk 'NR % 2 == 0' data