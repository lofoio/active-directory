#!/bin/sed -f
#translate file.srt to file.lrc
#2010-10-31 17:50 by badegg
#2010-12-22 change , into . for compitable, add line 23
# tr tab to space
y/\t/ /
# del boring win back return
s/\r//
 # del leading and trailing spaces
s/^ *//
s/ *$//
# del blank lines ( `d' Delete the pattern space
# and  immediately start next cycle.)
/^[0-9]*$/d
/^[0-9]\{2\}:.\+>/{
	x
	/^$/d
	s/\n/ /g
	s/\,/\./
	s/\,/\./
	#00:00:22.889 --> 00:00:24.151
	#\1          \2   \3          \4
	s/\(^[^ ]*\)\( --> \)\([^ ]\+\)\(.*\)/[\1]\4\n[\3]/
b done}
H
${
	x
	s/\n/ /g
	s/\,/\./
	s/\,/\./
	s/\(^[^ ]*\)\( --> \)\([^ ]\+\)\(.*\)/[\1]\4\n[\3]/
b done}
d
:done
