import math
import sys

inp = sys.argv[1]
opn = 0
cls = 0
y = 0
count = 0

while count < len(inp):
    count = count + 1
    for i in inp:
        if y < 0 or cls > opn:
            break
        elif i == "(":
            opn = opn + 1
            y = opn - cls
        elif i == ")":
            cls = cls + 1
            y = opn - cls
        else: print "error"
if y == 0:
    print "YES"
else: print "NO"
        
