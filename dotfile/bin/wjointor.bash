#!/bin/bash
#  May need to save original positional parameters,                             
#+ since they get overwritten.                                                  
#  One way of doing this is to use an array,                                    
#         original_params=("$@")                                                
#ls | sort -t "-" -k 1,1 -k 2,2n
blkrm.bash "$1"
rltfile=${1%.*}.sor
sort -b -u -o "$1" "$1"
awk 'BEGIN{oldna = ""; oldti = ""; oldline = ""}
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

{ FS = "[][]" 
if ( oldna == $1 && hms2s(oldti)+2 > hms2s($2) ) {
oldline = oldline$0
oldti = $(NF-1)
sub(/\[[^[]+lrc:\[[^[]+\]/, " ", oldline)
}
else {
if (NR != 1)
print oldline
oldline = $0
oldna = $1
oldti = $(NF-1)
}
}' "$1" > "$1".bak
mv -v "$1".bak "$1"
sed -e 's/\].\+\[/ /g' \
    -e  's/:\[/ /g' "$1" \
| tee "$rltfile"
#exit 0
exec 6<&0           # Link file descriptor #6 with stdin.
                    # saves stdin.
exec < "$rltfile"   # stdin replaced by file "$inputfile"
while read line
do
~/bin/scratch-audio.bash $line
# set -- $line# echo "$1"# echo "$2"# echo "$3"
done
                                                                                                
echo 
                                                                                                
exec 0<&6 6<&-
##if ( oldna == $1 && oldti == $2) {