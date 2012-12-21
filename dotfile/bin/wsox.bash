#!/bin/bash
#TODAY=`date '+%F-%H-%M'`
if [ -z "$1" ]
then
TODAY=`date '+%Y-%m-%d'`
else
TODAY=$1
fi

INPUTFILE=`ls -og --time-style="+%Y-%m-%d" *.wav | awk -v pat="$TODAY" '$4 == pat {print $5}' | sort -t "-" -k 1,1 -k 2,2n`
OUPUTFILE="./join-place/"$TODAY".wav"
if [ -n "$INPUTFILE" ] 
then
echo "joining............"
sox $INPUTFILE "$OUPUTFILE" && echo "Done "$OUPUTFILE""
else
echo "warning: none input files, exit."
echo "USAGE: wsox.bash <xxxx-xx-xx>"
fi
