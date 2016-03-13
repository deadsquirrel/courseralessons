import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)

data = uh.read()

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print 'my count:', counts
print 'my count len:', len(counts)

for item in counts:
    print item

    #'Count', item.find('count').text
