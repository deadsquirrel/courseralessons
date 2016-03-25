''' 
my project

check name of the registered people of list_1 in
 list_0 - list of a students of Capital English

'''
import re
import my_check

data = open ('1645_1.csv')
#create list from spisok groups
list_gr = my_check.check_l(data)
print '------------------'
print list_gr
print '------------------'

out_list = []
out_list2 = []
data2 = open('1645_2_1.csv')
for line in data2:
    if re.search('[a-zA-Z0-9\._-]+@[a-z\.]+', line):
        print "LINE:", line
        p = re.compile('[a-zA-Z0-9\._-]+@[a-z\.]+')
#        print '___',p
        n = p.findall(line)
        print '--',n
        for i in list_gr:
            print "i:", i
            if i == n[0][:]:
                print "Ok"
                out_list.append(i)
                out_list2.append(line)
#            else: print "No"
        print '____'
print out_list
print out_list2
print 'the end'







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
