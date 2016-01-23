fname = raw_input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
stuff = list()

for line in fh:
    if not line.startswith('From '): continue
    count = count + 1
#        print line
    str = line.split()
    print str[1]

#        stuff.append(str[1])
#        print stuff
#print stuff
print "There were", count, "lines in the file with From as the first word"
