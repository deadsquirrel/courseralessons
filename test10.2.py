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
        keyt = keystr[:2]
        if count.has_key(keyt) == True:
            d2 = {keyt: count[keyt] + 1}
        else:
            d2 = {keyt: 1}
            count.update(d2)
print "Count:",count
            
list_keys = count.keys()
list_keys.sort()
print "List: ",list_keys

for j in list_keys:
    print j, count[j]
