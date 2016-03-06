# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))
name = None
# Retrieve all of the anchor tags

while count > 0:
    name_list = []
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        print tag.get('href', None)
        print 'names', tag.contents[0]
        name_list.append(tag.get('href', None))

    count = count - 1
    
    url = name_list[pos-1]
#    name = url.contents[0]
    print 'count:', count, '---url---', url
print '===', name
   
