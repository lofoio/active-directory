#!/bin/bash
cd /home/badegg/Movies/english/bbc-news 
INPUTFILES=${1%.*}.mp3
STARTPOINT=`echo $2 \
| awk -F : \
   '{if (NF == 2) {print $1*60+$2} 
else if (NF == 3) {print $1*3600+$2*60+$3}
else if (NF == 1) {print $1*1}}'`
if [ "$3" != "0" ]
then
ENDPOINT=`echo $3 \
| awk -F : \
   '{if (NF == 2) {print $1*60+$2} 
else if (NF == 3) {print $1*3600+$2*60+$3}
else if (NF == 1) {print $1*1}}'`
let ENDPOINT=$ENDPOINT-$STARTPOINT+1
else
ENDPOINT="10"
fi
mplayer -loop 1 -ss $STARTPOINT -endpos $ENDPOINT $INPUTFILES 1> /dev/null