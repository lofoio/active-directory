#!/bin/bash
mplayer -alang en -vf screenshot -loop 0 "$1" > /dev/null 2>&1
