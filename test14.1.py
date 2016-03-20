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
data = uh.read()

info = json.loads(str(data))
print info
