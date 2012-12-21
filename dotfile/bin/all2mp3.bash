#!/bin/bash
# infile="$1"
# oufile=${infile%.avi}.mp3
# mplayer -vc null -vo none -ao pcm:file="temp.wav" ${infile}
#!/bin/bash
# [ -z "${CONFIG}" ] && {
#     echo $"Usage: ifup <device name>" >&2
#     exit 1
# }
infile="$1"
if [ -z "$1" ]
then
echo "Usage: all2wav.bash infile(any subfix)"
exit
fi
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

oufile=${infile%.*}.wav

mplayer ${startpoint} ${endpoint} -vc null -vo none -alang eng -ao pcm:file="${oufile}" "${infile}"
lame -b 64 "${oufile}"  "${oufile%.*}.mp3"  && rm -rf  "${oufile}"
#ffmpeg -i audio1.aac -ab 64k -map_meta_data audio1.mp3:audio1.aac audio1.mp3