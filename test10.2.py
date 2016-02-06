'''
 You can pull the hour out from the 'From ' line by finding the time and 
 then splitting the string a second time using a colon. 
'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
val = 1

for line in handle:
    if not line.startswith('From '): continue
    else:
        str = line.split()
        keystr = str [5]
        print "KS:",keystr
        key = keystr[:2]
        val = val + 1
        print key, val
        
