''' 
create fun clean_list(list_to_clean
that takes one argument - list any values (strings, integer and real numbers)
of arbitrary length, and returns a list that consists of the same values, 
but does not repeat elements.

'''

import sys
inp_list = sys.argv[1]
t_list = []
next_list = []

for i in inp_list:
    if i.isdigit():
        t_list.append(i)
        print t_list

for c, i in enumerate(t_list):
    new_list = t_list[c+1:]
    for count, j in enumerate(new_list):
        if j == i:
            print j, " ==  ", i
            t_list.insert(c, t_list.pop(count+1))
        else:
            print "j:",j,"i: ", i
print "uniq number of list:", t_list
                    
