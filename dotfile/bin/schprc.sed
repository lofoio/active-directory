# tr tab to space
y/\t/ /
# del boring win back return
s/\r//
# del leading and trailing spaces
s/^ *//
s/ *$//
# del blank lines ( `d' Delete the pattern 
#space and  immediately start next cycle.)
/^ *$/d
###########################
/[:-]\[[0-9]\{0,2\}:/{x;/^ *$/d;s/\n//g;${P;x};b end}
H
${x;s/\n//g;P}
d
:end
