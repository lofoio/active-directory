#!/bin/bash
    wd=11
    var0=6                                                                            
    LIMIT=13                                                                          
    while [ "$wd" -lt "12" ]                                                    
    do
	while [ "$var0" -lt "$LIMIT" ]                                                    
	do                                                                                
	    join-wav-by-name.bash  20`printf "%02d\n" $wd``printf "%02d\n" $var0`*BBC*.wav
	    let "var0 += 1"
	done               
	let "wd += 1"
    done
##for wd in *.lrc ; do cat $wd | iconv -f gbk -t utf8 | sed 's/（/(/g' | grep '(' | sed -e 's/^.*(/(/g' > ${wd%.lrc}p2.txt ; done