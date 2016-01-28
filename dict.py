import sys

name = str(sys.argv[1])

counts = dict()
counts['raz'] = 3
counts['dva'] = 5
counts['tri'] = 7
print counts

'''
if name in counts:
    print counts[name]
else:
    print "nothing"
'''

print counts.get(name,0)
print counts.get(name,'nothing in counts')
