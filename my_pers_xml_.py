''' 
my project

check name of the registered people of list_1 in
 list_0 - list of a students of Capital English

'''
import re

data = open ('1645_1.csv')
l = []
for line in data:
    if re.search('[a-zA-Z\._-]+@[a-z\.]+', line):
        print line
        
        p = re.compile('[a-zA-Z\._-]+@[a-z\.]+')
        n = p.findall(line)
        print '--',n
        
'''
    at_pos = line.find('@')
    print at_pos
    next_pos = line.find(",", at_pos)
    print next_pos
'''
# call module find email in new_list













'''
import urllib
import json

url = raw_input('Enter location: ')
print 'Retrieving', url

uh = urllib.urlopen(url)
print uh

data = uh.read()
print 'Retrieved',len(data),'characters'
print "----------------"
#print data
info = json.loads(data)

#print info


#print json.dumps(info, indent=4)

#print 'mm',  info["comments"][0]
#["count"]



for item in info["head"]:
#    print item
    print item["meta"]



'''
