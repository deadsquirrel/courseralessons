# file_search(folder, filename),
# python pr_test5.4.py "['d', 'f', 'fggh', 'tgdfg']" "gg"
#                      path                          name
# -*- coding: utf-8 -*-

import sys
import pr_test5_4_mod
path = sys.argv[1]
print "path::", path
path_cut = path[2:-2]
# subdir nas another structure
path_list = path_cut.split(", ")

name = sys.argv[2]
print "name = ", name

pr_test5_4_mod.file_search(path_list, name)
    
