''' 
create fun clean_list(list_to_clean
that takes one argument - list any values (strings, integer and real numbers)
of arbitrary length, and returns a list that consists of the same values, 
but does not repeat elements.

'''

import sys
list4 = [12,9,80,8,7]
#inp_list = sys.argv[1]


def cheklist (arg1, arg2):
    for j in arg2:
        if arg1 != j:
            return arg2.append(arg1)
            print "A"
        else:
            return arg2
            print "B"
        
list = []
for i in list4:
    print list.append(i)

    #    cheklist(i, inp_list(:i))
    
''' example:
def text_prompt(msg):
    try:
        return raw_input(msg)
    except NameError:
        return raw_input(msg) 
'''
