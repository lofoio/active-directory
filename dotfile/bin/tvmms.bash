#!/bin/bash
#mplayer -loop 0 -cache 8192 mms://a529.l7906022528.c79060.g.lm.akamaistream.net/D/529/79060/v0001/reflector:22528
if [ -z "$1" ] ; then
mplayer -loop 0 -cache 18192  mms://tv.lzu.edu.cn/tv1
elif [ "$1" == "1" ] ; then
mplayer -loop 0 -cache 18192  mms://tv.lzu.edu.cn/tv3
elif [ "$1" == "5" ] ; then
mplayer -loop 0 -cache 18192  mms://tv.lzu.edu.cn/tv2
else
mplayer -loop 0 -cache 8192 "$1"
fi

#bbc
#mplayer -loop 0 -cache 18192  mms://tv.lzu.edu.cn/tv1
#cctv5
#mplayer -loop 0 -cache 18192  mms://tv.lzu.edu.cn/tv2
#cctv1
#mplayer -loop 0 -cache 18192  mms://tv.lzu.edu.cn/tv3
#-vc null -vo none
#mms://cctv.wm.llnwd.net/cctv_live_cctv9
#mms://live.cctv.com/live19
#mms://cctv-live-cctv1.wm.llnwd.net/cctv_live_cctv9
