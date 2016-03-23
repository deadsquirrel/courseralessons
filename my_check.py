import re
n = []
def check_l(nnn):
    for line in nnn:
        if re.search('[a-zA-Z0-9\._-]+@[a-z\.]+', line):
#            print line
            p = re.compile('[a-zA-Z0-9\._-]+@[a-z\.]+')
            nn = p.findall(line)
#            print 'nn:', nn
            elem = nn[0][:]
#            print 'elem:', elem
            n.append(elem)
    return n

'''
import re
def check_l(nnn):
    for line in nnn:
        if re.search('[a-zA-Z\._-]+@[a-z\.]+', line):
            print line
            p = re.compile('[a-zA-Z\._-]+@[a-z\.]+')
            n = p.findall(line)
            return n
    
'''
