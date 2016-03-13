import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)

data = uh.read()

tree = ET.fromstring(data)
counts = tree.findall('.//comment')
#print 'my count:', counts
#print 'my count len:', len(counts)

sum = 0
for item in counts:
#    print item
#    print 'Name', item.find('name').text
#    print 'Count', item.find('count').text
    count_n = int(item.find('count').text)
    sum = sum + count_n

print sum
    #'Count', item.find('count').text
