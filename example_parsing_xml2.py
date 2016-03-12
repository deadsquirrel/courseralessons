#!/usr/bin/python
import xml.etree.ElementTree as etree
tree = etree.parse('examples/feed.xml')
root = tree.getroot()
root.findall('{http://www.w3.org/2005/Atom}entry')
root.findall('{http://www.w3.org/2005/Atom}feed')
