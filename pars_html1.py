# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
summ = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'TD:',tag.get('td', None)
    summ = summ + int(tag.contents[0])
#    print 'Attrs:',tag.attrs

print summ
