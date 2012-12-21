#!/bin/bash
chmod -x *.rar
for wd in *.rar 
do 
rar d "$wd" \*.txt \*.url
rar e "$wd"
done
p-rename.perl 's/[^0-9a-zA-Z-.]/-/g' *pdf
p-rename.perl 's/-+/-/g' *pdf
p-rename.perl 's/-\.pdf/\.pdf/g' *pdf