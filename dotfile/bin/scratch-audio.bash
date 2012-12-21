#!/bin/bash
workdir="/home/badegg/Movies/english/bbc-news/"
INPUTFILES=$workdir${1%.*}.mp3
STARTPOINT=`echo ${2%.*} \
| awk -F : \
   '{if (NF == 2) {print $1*60+$2} 
else if (NF == 3) {print $1*3600+$2*60+$3}
else if (NF == 1) {print $1}}'`
ENDPOINT=`echo ${3%.*} \
| awk -F : \
   '{if (NF == 2) {print $1*60+$2} 
else if (NF == 3) {print $1*3600+$2*60+$3}
else if (NF == 1) {print $1}}'`
[ $STARTPOINT -gt 1 ] && let STARTPOINT=$STARTPOINT-1

if [ $ENDPOINT -eq 0 ]
then
ENDPOINT="12"
else
let ENDPOINT=$ENDPOINT-$STARTPOINT+1
fi
echo $INPUTFILES $STARTPOINT $ENDPOINT
OUPUTFILES="${INPUTFILES%.*}-$STARTPOINT-$ENDPOINT.wav"
if [ -e $OUPUTFILES ] 
then
echo "$OUPUTFILES already exists."
else
mplayer -srate 44100 -ss $STARTPOINT -endpos $ENDPOINT -vc null -vo none    \
-ao pcm:file="$OUPUTFILES" "$INPUTFILES" </dev/null >/dev/null              \
&& echo "$OUPUTFILES done"
fi