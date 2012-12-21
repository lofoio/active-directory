#!/bin/bash
tempfile=${1%.sub}.srt
sed -e '/^[0-9]\{2\}:.\+/{s/,/ --> /;s/\./,/g}' "$1" > "$tempfile"