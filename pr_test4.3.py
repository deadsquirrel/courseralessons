import math
import sys

inp = sys.argv[1]
opn = 0
cls = 0


for i in inp:
    if i == "(":
        opn = opn + 1
    elif i == ")":
        cls = cls + 1
    else: print "error"
    
if opn - cls == 0:
    print "YES"
else: print "NO"
