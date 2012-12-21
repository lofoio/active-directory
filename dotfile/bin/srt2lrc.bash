#!/bin/bash
[ -z "${@}" ] && {
echo $"Usage: ./srt2lrc.bash < file.srt >" >&2
    exit 1
}
fname="$1"
##for fname in "$@"
##do
otname=${fname%.srt}.lrc
[[ $fname == *.srt && -s $fname ]] && {
#iconv -c -f GB18030 -t UTF-8 "$fname"                 \
cat "$fname" \
| sed -f ~/bin/srt2lrc.sed                            \
| awk 'BEGIN{FS = "[][]"; oldline = ""; oldti = ""}
END{print oldline; exit 0}
function hms2s(hms,    na,    scds)
{
sub(/[^0-9:].+/, "", hms)
na = split(hms, arr, ":")
if      (na == 2) {scds =  arr[1]*60+arr[2]} 
else if (na == 3) {scds =  arr[1]*3600+arr[2]*60+arr[3]}
else if (na == 1) {scds =  arr[1]*1}
return scds
}
{
if ( oldline !~ /]$/ || hms2s(oldti)+1 < hms2s($2) ) { if (NR != 1) {print oldline} }
oldline = $0
oldti = $2
}' > "$otname"

echo "$otname DONE"
}
##done
