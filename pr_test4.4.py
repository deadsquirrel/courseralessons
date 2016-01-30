# lucky namber
import math
import sys

i = int(sys.argv[1])
n = int(sys.argv[2])
k = 0

num_list = range(i,n+1)

for j in num_list:
    bfj = j%1000
    afj = j/1000
    straj = str(afj)                
    while len(straj) < 3:
        straj = '0' + straj
    strbj = str(bfj)                
    while len(strbj) < 3:
        strbj = '0' + strbj
    a_sum = int(straj[0]) + int(straj[1]) + int(straj[2])
    b_sum = int(strbj[0]) + int(strbj[1]) + int(strbj[2])
    if a_sum == b_sum:
        k = k+1
                                             
print k

