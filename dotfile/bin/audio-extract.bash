#!/bin/bash
if [ ! -e "$1" ] 
then
echo "error : wrong file name" 
exit
fi
fname=$1
##${filename%$1}$2 ???
mplayer -ao pcm:file=${fname%.*}.wav -vo null -vc none  $fname
#tip -vc null is too slowly,why?