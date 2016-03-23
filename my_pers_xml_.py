''' 
my project

check name of the registered people of list_1 in
 list_0 - list of a students of Capital English

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




