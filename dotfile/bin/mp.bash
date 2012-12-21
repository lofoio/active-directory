#!/bin/bash
mplayer -vf screenshot -loop 0 "$1" > /dev/null 2>&1
