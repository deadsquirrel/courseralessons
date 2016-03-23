import re
nnn = open('1645_2_1.csv')
n = []
for line in nnn:
    if re.search('[a-zA-Z0-9\._-]+@[a-z\.]+', line):
        print line
        p = re.compile('[a-zA-Z0-9\._-]+@[a-z\.]+')
        nn = p.findall(line)
        print 'nn:', nn
        elem = nn[0][:]
        print 'elem:', elem
        n.append(elem)
print '-=-=:', n
    
