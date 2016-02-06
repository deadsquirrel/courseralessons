'''
 You can pull the hour out from the 'From ' line by finding the time and 
 then splitting the string a second time using a colon. 
'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
val = 0
count = {}
print "==",count
for line in handle:
    if not line.startswith('From '): continue
    else:
        str = line.split()
        keystr = str [5]
#        print "KS:",keystr
        key = keystr[:2]
        print "Key:",key
#        count[key] = 1
        for i in count:
            print "1:", i
            if i == key:
                count[i] = count[key] +1
            else:
                count[i] = 1
print count.items()
