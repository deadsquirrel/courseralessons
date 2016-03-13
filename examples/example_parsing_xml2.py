#!/usr/bin/python
import xml.etree.ElementTree as etree
tree = etree.parse('examples/feed.xml')
root = tree.getroot()
print root.findall('{http://www.w3.org/2005/Atom}entry')
print root.findall('{http://www.w3.org/2005/Atom}feed')
