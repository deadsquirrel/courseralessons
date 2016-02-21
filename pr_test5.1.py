''' 
create fun clean_list(list_to_clean
that takes one argument - list any values (strings, integer and real numbers)
of arbitrary length, and returns a list that consists of the same values, 
but does not repeat elements.

'''

import sys

inp_list = sys.argv[1]

def clean_list(inp_list):
    for i in inp_list:
        cheklist(i, inp_list(:i))
        
def cheklist (arg1, arg2):
    for j in arg2:
        if arg1 != j:
        return arg2.append(arg1)
        print "A"
        else:
            return print arg2

''' example:
def text_prompt(msg):
    try:
        return raw_input(msg)
    except NameError:
        return raw_input(msg) 
'''
