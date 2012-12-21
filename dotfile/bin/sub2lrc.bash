#!/bin/bash
tempfile=${1%.sub}.srt
sed -e '/^\[[A-Z]\+\]/d' -e '/^[0-9]\{2\}:.\+/{s/,/ --> /;s/\./,/g}' "$1" > "$tempfile"
srt2lrc.bash "$tempfile"
rm -rf "$tempfile"