#! /bin/awk -f
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
print hms2s($0)
} 
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
