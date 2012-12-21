#!/bin/bash
# [ -z "${CONFIG}" ] && {
#     echo $"Usage: ifup <device name>" >&2
#     exit 1
# }
infile="$1"

if [ -z "$2" ]
then
startpoint=""
else
startpoint="-ss $2"
fi

if [ -z "$3" ]
then
endpoint=""
else
endpoint="-endpos $3"
fi

oufile=${infile%.*}.mp3
if [ -e "$oufile" ]
then
echo "$oufile" already exists.
exit 0
fi
mencoder ${startpoint} ${endpoint} -o "$oufile"  -ovc frameno -oac mp3lame -of rawaudio -lameopts cbr:br=56 "$infile"
#mencoder ${startpoint} ${endpoint} -o "$oufile" -vc null -ovc frameno -oac mp3lame -of rawaudio -lameopts cbr:br=56 "$infile"
#mplayer -vc null -vo none -ao pcm:file=- $1
#mplayer -vc null -vo none -ao pcm:fast:file="star-war-temp.wav" Star.Wars.Episode.I.The.Phantom.Menace.1999.HDTVRiP.X264.2Audio.AAC.HALFCD-NORM.avi