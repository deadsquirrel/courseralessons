'''
 You can pull the hour out from the 'From ' line by finding the time and 
 then splitting the string a second time using a colon. 
without update method
'''
    
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = {}
for line in handle:
    if not line.startswith('From '): continue
    else:
        str = line.split()
        keystr = str [5]
        keyt = keystr[:2]
        if count.has_key(keyt) == True:
            count[keyt] = count[keyt] +1
        else:
            count[keyt] = 1	
            
list_keys = count.keys()
list_keys.sort()

for j in list_keys:
    print j, count[j]
