''' Extracting Data from JSON
In this assignment you will write a Python program somewhat similar to 
http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL,
read the JSON data from that URL using urllib and then parse and extract
the comment counts from the JSON data, compute the sum of the numbers
in the file and enter the sum below:

Sample data: http://python-data.dr-chuck.net/comments_42.json 
(Sum=2553) 
Actual data: http://python-data.dr-chuck.net/comments_204876.json 
(Sum ends with 78)
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
print data
info = json.loads(data)
#print info

sum = 0
#print json.dumps(info, indent=4)

#print 'mm',  info["comments"][0]
#["count"]



commentators = []
for item in info["comments"]:
#    print item
#    print item["count"]
    sum = sum + item["count"]
    commentators.append(item["name"])

print commentators
print sum
