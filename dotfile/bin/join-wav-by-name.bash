#!/bin/bash
if [ $# == "1" ]
then
echo "USAGE: wsox.bash files (at least 2 files)"
exit
fi
INPUTFILE=`echo "$@" | sed 's/ /\n/g' | sort -t "-" -k 1,1 -k 2,2n`
OUPUTFILE="./join-place/"${1%%-*}_${!#%%-*}.wav
if [ -n "$INPUTFILE" ] 
then
echo "joining............"
sox $INPUTFILE "$OUPUTFILE" && echo "Done "$OUPUTFILE""
fi
