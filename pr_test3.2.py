# N number Fibonacci Sequence
import math
import sys

n = int(sys.argv[1])
j = 0
k = 0


for i in range(n+1):
    print "-i:  ",i
    print "j=",j
    print "k=",k
    if i == 1:
        result = j + i
    else:
        result = j + k
    print " - - - - -R=",result
    j = k
    print "j2=",j
    k = result
    print "k2=",k
print ":::::::::::::::",result
    
