#!/usr/bin/env python

'''
Read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers. 

'''

import re
fname = raw_input("Enter file name: ")
s = 0
fh = open(fname)
for line in fh:
    
    y = re.findall('[0-9]+', line)

    if y != []:
        for i in y:
            s += int(i)
print 'sum = ',s
