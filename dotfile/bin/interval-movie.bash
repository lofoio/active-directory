#!/bin/bash
let start=$2*360
mplayer -ss $start -endpos 360 -loop 0 $1 > /dev/null 2>&1