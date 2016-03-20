''' Extracting Data from JSON
In this assignment you will write a Python program somewhat similar to 
http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL,
read the JSON data from that URL using urllib and then parse and extract
the comment counts from the JSON data, compute the sum of the numbers
in the file and enter the sum below:
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

#print 'mm',  info[0]

'''
for item in info:
    print item
    sum = sum + 1
'''
