#!/opt/sage/sage -python

import sys
from sage.all import *

if len(sys.argv) != 2:
    print "Usage: %s <n>"%sys.argv[0]
    print "Outputs the prime factorization of n."
    sys.exit(1)

var('x y')

print factor(sage_eval(sys.argv[1],locals={'x':x, 'y':y}))

c = circle((0,0), 1, rgbcolor=(1,1,0))
c.show()
