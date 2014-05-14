#!/bin/bash
#lgug eng chi
infile="$1"
vdadst="subtitles"
if [ -z "$2" ] ; then
whatlang="eng"
elif [ "$2" != "eng" ] && [ "$2" != "chi" ] ; then
echo -n "Please enter a language [eng|chi] :"
read whatlang
else
whatlang="$2"
fi
echo "expected:" $vdadst $whatlang
notrack=`mkvinfo "${infile}" | \
awk -v lopt="$whatlang" -v vusl="$vdadst" \
'BEGIN{myflag = "0"}
END{if (myflag == "0" ) {print tnum, ttyp, lgug}}
/A track/ {tnum = ""; ttyp = ""; lgug = ""}
/Language|(Track (number|type))/ {
if ( $4 == "number:" )   {tnum = $5}
if ( $(NF-1) == "type:" )     {ttyp = $NF}
if ( $(NF-1) == "Language:" ) {lgug = $NF}
if (ttyp == vusl  && lgug == lopt ) {myflag = "1"; print tnum, ttyp, lgug; exit 0}}'`
echo "will get:" $notrack
notrack=${notrack%% *}
oufile="${infile%.mkv}".${notrack}
echo "mkvextract tracks "${infile}" "${notrack}":"${oufile}""
mkvextract tracks "${infile}" "${notrack}":"${oufile}"
