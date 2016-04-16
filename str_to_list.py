# strint to list

import sys

path = str(sys.argv[1])
print "::", path
path_cut = path[2:-2]
path_list = path_cut.split("', '")
print '--',path_list

    
for i in path_list:
       print 'i|', i
