#!/usr/bin/python
import lxml.etree                                                               
tree = lxml.etree.parse('examples/feed.xml')
tree.findall('//{http://www.w3.org/2005/Atom}*[@href]')
tree.findall("//{http://www.w3.org/2005/Atom}*[@href='http://diveintomark.org/']")
tree.findall('//{NS}author[{NS}uri]'.format(NS=NS)) 
