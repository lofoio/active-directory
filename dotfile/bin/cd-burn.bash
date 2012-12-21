#!/bin/bash
infile="$1"
isofile=${infile%/}.iso
mkisofs -Jrv -V BAKUP -o $isofile $infile               &&      \
echo  "      ==== > ISO file is $isofile < ======   "   &&      \
wodim -devices                                          &&      \  
isosize=$(stat -c%s $isofile)
if [ $isosize -gt  700000000 ]
then
burnspd=2
else
burnspd=8
fi
echo "burn speed is x$burnspd"
wodim -v -eject speed=$burnspd  dev=/dev/scd0 $isofile      # dev=1,0,0 
