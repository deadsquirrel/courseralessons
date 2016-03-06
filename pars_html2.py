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
    c_pos = pos
    name_list = []
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
#        print tag.get('href', None)
#        print 'names', tag.contents[0]
        name_list.append(tag.get('href', None))
        if c_pos == 1:
            name = tag.contents[0]
            print "//////////-=-=-=-=-=-", name
        c_pos = c_pos - 1
    count = count - 1
    
    url = name_list[pos-1]
    print 'count:', count, '---url---', url
#name = soup.head.parent.parent.__class__.__name__
#name = tag.string
print '===', name


'''
http://python-data.dr-chuck.net/known_by_Fikret.html

'''
   
