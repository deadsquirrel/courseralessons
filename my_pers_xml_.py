''' 
my project

check name of the registered people of list_1 in
 list_0 - list of a students of Capital English

'''
import re
import my_check

data = open ('1645_1.csv')
data2 = open('1645_2_1.csv')
for line in data:
    if re.search('[a-zA-Z\._-]+@[a-z\.]+', line):
        print line
        p = re.compile('[a-zA-Z\._-]+@[a-z\.]+')
#        print '___',p
        n = p.findall(line)
        print '--',n
        my_check.check_l(data2)
        print '____'
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
