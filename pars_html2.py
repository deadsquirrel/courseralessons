# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

name_list = ['A']
N = 1
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
#    print tag.get('href', None)
#    print tag.contents[0]
    name_list.append(tag.contents[0])
print name_list
while count > 0:
    for name in name_list:
        print name_list[(pos)*N]
        count = count - 1
        N += 1
