#!/bin/bash
#for video in *.avi
#do
#conmon=`echo $video | sed -e 's/F.+E[0-9]{2}//g'`
#${var:pos}
#conmon=`echo $video | sed -e 's/\(F.*E[0-9]\{2\}\).*/\1/g'`
#ls $conmon.ench.srt
#mv -v $conmon.ench.srt ${video%.avi}.srt
#done[00:00:02.002]
#tr '\n' '@'  < $ofile > $ofile.bak
#tr '\n' ' '  < $ofile > $ofile.bak
#sed -e 's/^.*\.lrc://' -e 's/\[[^a-zA-Z]*\]$//' -e 's/^\[[^a-zA-Z]*\]//' $1 > $ofile
#sed -e 's/\[.*\]//' $1 > $ofile
ofile=${1%.*}.txt
sed -e 's/^\[[.0-9:]\+\]//' $1 > $ofile && echo "$ofile Done"y
# sed -e 's/\[.*\]/@/' $1 > $ofile
# awk '{printf "%s", $0 }' $ofile | sed -e 's/@\+/@/g' > $ofile.bak
# mv -v $ofile.bak $ofile