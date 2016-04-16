# file_search(folder, filename),

import sys
import pr_test5_4_mod
path = sys.argv[1]
print "::", path
path_cut = path[2:-2]
path_list = path_cut.split("', '")

name = sys.argv[2]
print "name = ", name

pr_test5_4_mod.file_search(path_list, name)
    
